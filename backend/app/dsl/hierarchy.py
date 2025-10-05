"""
Hierarchy Utilities
===================
Resolve ancestors for entities using parentId chains.

WHY:
- MetricFact rows may be tied to leaf entities (ad/adset).
- When user asks for breakdown at "campaign" level, we must
  roll up all leaf facts to their campaign ancestor.
- We do this with a Postgres recursive CTE (no schema change).

Used by:
- dsl/executor.py breakdown branch

EXAMPLE HIERARCHY:
  Campaign A (id=1, parent_id=null, level='campaign')
    ├── AdSet A1 (id=2, parent_id=1, level='adset')
    │   ├── Ad A1.1 (id=3, parent_id=2, level='ad')
    │   └── Ad A1.2 (id=4, parent_id=2, level='ad')
    └── AdSet A2 (id=5, parent_id=1, level='adset')
        └── Ad A2.1 (id=6, parent_id=5, level='ad')

If MetricFact rows are stored at Ad level (3,4,6), and user asks for
"breakdown by campaign", we need to roll up all metrics to Campaign A.

The CTE traverses: Ad → AdSet → Campaign, then groups by Campaign.
"""

from sqlalchemy import literal, union_all, and_
from sqlalchemy.orm import aliased
from app import models


def campaign_ancestor_cte(session):
    """
    Build a WITH RECURSIVE CTE that maps every entity (leaf) to its campaign ancestor (if exists).
    
    Returns a CTE with columns:
      - leaf_id: The original entity ID
      - ancestor_id: The campaign ancestor ID (or self if entity is a campaign)
      - ancestor_name: The campaign ancestor name
    
    Notes:
    - This works regardless of where MetricFact is attached (ad/adset/campaign).
    - If an entity is itself a campaign, it maps to itself.
    - If an entity has no campaign ancestor (orphaned), it won't appear in results.
    
    SQL equivalent:
    ```sql
    WITH RECURSIVE entity_tree AS (
        -- Base case: start with all entities
        SELECT 
            id as leaf_id,
            id as current_id,
            name as current_name,
            level as current_level,
            parent_id
        FROM entities
        
        UNION ALL
        
        -- Recursive case: walk up the parent chain
        SELECT 
            et.leaf_id,
            e.id as current_id,
            e.name as current_name,
            e.level as current_level,
            e.parent_id
        FROM entity_tree et
        JOIN entities e ON e.id = et.parent_id
        WHERE et.parent_id IS NOT NULL
    )
    SELECT DISTINCT ON (leaf_id)
        leaf_id,
        current_id as ancestor_id,
        current_name as ancestor_name
    FROM entity_tree
    WHERE current_level = 'campaign'
    ORDER BY leaf_id;
    ```
    """
    E = models.Entity
    
    # Base case: start at every entity; its current ancestor is itself
    base = session.query(
        E.id.label("leaf_id"),
        E.id.label("current_id"),
        E.name.label("current_name"),
        E.level.label("current_level"),
        E.parent_id.label("parent_id")
    )
    
    # Create the recursive CTE
    entity_tree = base.cte(name="entity_tree", recursive=True)
    
    # Recursive case: join to parent
    parent = aliased(E)
    recursive_step = session.query(
        entity_tree.c.leaf_id,
        parent.id.label("current_id"),
        parent.name.label("current_name"),
        parent.level.label("current_level"),
        parent.parent_id.label("parent_id"),
    ).join(
        parent, 
        and_(
            parent.id == entity_tree.c.parent_id,
            entity_tree.c.parent_id != None
        )
    )
    
    # Union base and recursive cases
    entity_tree = entity_tree.union_all(recursive_step)
    
    # Select only the campaign-level ancestors
    # Use DISTINCT ON to get one row per leaf_id (in case of multiple paths)
    campaign_ancestors = (
        session.query(
            entity_tree.c.leaf_id,
            entity_tree.c.current_id.label("ancestor_id"),
            entity_tree.c.current_name.label("ancestor_name"),
        )
        .distinct(entity_tree.c.leaf_id)
        .filter(entity_tree.c.current_level == "campaign")
        .order_by(entity_tree.c.leaf_id)
    )
    
    return campaign_ancestors.cte(name="leaf_to_campaign")


def adset_ancestor_cte(session):
    """
    Similar to campaign_ancestor_cte, but maps entities to their adset ancestor.
    
    Used when breakdown="adset" is requested.
    
    Returns a CTE with columns:
      - leaf_id: The original entity ID
      - ancestor_id: The adset ancestor ID (or self if entity is an adset)
      - ancestor_name: The adset ancestor name
    """
    E = models.Entity
    
    # Base case: start at every entity
    base = session.query(
        E.id.label("leaf_id"),
        E.id.label("current_id"),
        E.name.label("current_name"),
        E.level.label("current_level"),
        E.parent_id.label("parent_id")
    )
    
    entity_tree = base.cte(name="entity_tree", recursive=True)
    
    # Recursive case
    parent = aliased(E)
    recursive_step = session.query(
        entity_tree.c.leaf_id,
        parent.id.label("current_id"),
        parent.name.label("current_name"),
        parent.level.label("current_level"),
        parent.parent_id.label("parent_id"),
    ).join(
        parent, 
        and_(
            parent.id == entity_tree.c.parent_id,
            entity_tree.c.parent_id != None
        )
    )
    
    entity_tree = entity_tree.union_all(recursive_step)
    
    # Select only the adset-level ancestors
    adset_ancestors = (
        session.query(
            entity_tree.c.leaf_id,
            entity_tree.c.current_id.label("ancestor_id"),
            entity_tree.c.current_name.label("ancestor_name"),
        )
        .distinct(entity_tree.c.leaf_id)
        .filter(entity_tree.c.current_level == "adset")
        .order_by(entity_tree.c.leaf_id)
    )
    
    return adset_ancestors.cte(name="leaf_to_adset")


# Future optimization (document for later):
# If performance becomes an issue with recursive CTEs at scale, consider:
# 1. Denormalized columns on MetricFact: campaign_id, adset_id (populated at ingest)
# 2. Materialized view with pre-computed ancestor mappings
# 3. Application-level caching of entity hierarchy
# 
# Current approach is clean and requires no schema changes, which is perfect for MVP.
