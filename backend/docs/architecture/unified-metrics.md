# Unified Metrics Architecture

**Version**: 1.0  
**Last Updated**: 2025-10-14  
**Status**: Implementation Phase

## Overview

The Unified Metrics Architecture centralizes all metric aggregation logic into a single service (`UnifiedMetricService`) that powers QA, KPI, entity performance, finance, and metrics endpoints. This eliminates data mismatches and ensures consistent calculations across the entire system.

## Problem Statement

### Current Issues
- **Data Mismatches**: QA shows 6.29× ROAS while KPI shows 5.92× ROAS for same query
- **Multiple Implementations**: 5 different aggregation paths with inconsistent filtering
- **Maintenance Burden**: Changes require updates in multiple files
- **Testing Complexity**: Each endpoint needs separate validation

### Root Causes
1. **Different Default Filters**: QA includes all entities, KPI defaults to active entities
2. **Inconsistent Level Filtering**: Some use `MF.level`, others use `E.level`
3. **Provider Enum Handling**: Mixed string vs enum formats
4. **Status Filter Logic**: Different default behaviors across endpoints

## Solution Architecture

### Core Components

```
┌─────────────────────────────────────────────────────────────┐
│                    UnifiedMetricService                     │
├─────────────────────────────────────────────────────────────┤
│ • Single source of truth for all metric calculations       │
│ • Consistent filtering logic across all endpoints          │
│ • Standardized input/output contracts                      │
│ • Built-in divide-by-zero guards                           │
│ • Workspace-scoped security                                │
└─────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────┐
│                    Filter Contract                         │
├─────────────────────────────────────────────────────────────┤
│ • MetricFilters dataclass for standardized inputs          │
│ • Provider enum normalization                              │
│ • Default behavior: ALL entities unless explicitly filtered│
│ • Validation and type safety                               │
└─────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────┐
│                    Metrics Registry                         │
├─────────────────────────────────────────────────────────────┤
│ • Existing app/metrics/registry.py                         │
│ • Single source of truth for formulas                      │
│ • Divide-by-zero guards                                     │
│ • 24 supported metrics (10 base + 14 derived)             │
└─────────────────────────────────────────────────────────────┘
```

### Service Interface

```python
class UnifiedMetricService:
    def get_summary(
        self,
        workspace_id: str,
        metrics: List[str],
        time_range: TimeRange,
        filters: MetricFilters,
        compare_to_previous: bool = False
    ) -> MetricSummary
    
    def get_timeseries(
        self,
        workspace_id: str,
        metrics: List[str],
        time_range: TimeRange,
        filters: MetricFilters
    ) -> List[MetricTimePoint]
    
    def get_breakdown(
        self,
        workspace_id: str,
        metric: str,
        time_range: TimeRange,
        filters: MetricFilters,
        breakdown_dimension: str,
        top_n: int = 5,
        sort_order: str = "desc"
    ) -> List[MetricBreakdownItem]
    
    def get_workspace_average(
        self,
        workspace_id: str,
        metric: str,
        time_range: TimeRange
    ) -> Optional[float]
```

### Filter Contract

```python
@dataclass
class MetricFilters:
    provider: Optional[str] = None
    level: Optional[str] = None
    status: Optional[str] = None  # Default: None (include all)
    entity_ids: Optional[List[str]] = None
    entity_name: Optional[str] = None
    metric_filters: Optional[List[MetricFilter]] = None
    
    def normalize_provider(self) -> Optional[str]:
        """Normalize provider enum format to string."""
        if not self.provider:
            return None
        if self.provider.startswith("ProviderEnum."):
            return self.provider.split(".")[1]
        return self.provider
```

## Migration Strategy

### Phase 1: Service Implementation ✅
- [x] Create `UnifiedMetricService` with core methods
- [x] Implement `MetricFilters` dataclass
- [x] Add comprehensive unit tests
- [x] Document API contracts

### Phase 2: Backend Migration (Big Bang)
- [ ] Refactor QA executor to use service
- [ ] Refactor KPI endpoint to use service
- [ ] Refactor entity performance to use service
- [ ] Refactor finance P&L to use service
- [ ] Refactor metrics endpoint to use service
- [ ] Remove old aggregation logic

### Phase 3: Client Updates
- [ ] Update UI clients for new defaults
- [ ] Update QA prompts for new behavior
- [ ] Add structured outputs to OpenAI calls

### Phase 4: Validation & Documentation
- [ ] Integration tests comparing all endpoints
- [ ] Performance benchmarks
- [ ] Update architecture documentation
- [ ] Update build log with changes

## Default Behaviors

### Entity Filtering
- **Default**: Include ALL entities (active + inactive)
- **Rationale**: Inactive campaigns still generated revenue
- **Override**: Explicit `status="active"` filter when needed

### Provider Filtering
- **Default**: Include all providers
- **Normalization**: Handle both `"meta"` and `"ProviderEnum.meta"` formats
- **Override**: Explicit provider filter when needed

### Level Filtering
- **Default**: Include all levels
- **Implementation**: Always use `E.level` (Entity table), never `MF.level`
- **Override**: Explicit level filter when needed

## Security Guarantees

### Workspace Isolation
```python
# All queries automatically scoped
query = query.filter(E.workspace_id == workspace_id)
```

### SQL Injection Prevention
- SQLAlchemy ORM only (no raw SQL)
- Parameterized queries
- Input validation via Pydantic

### Data Validation
- Metric names validated against registry
- Time ranges validated (1-365 days)
- Filter values validated against enums

## Performance Considerations

### Query Optimization
- Single aggregation query per metric
- Efficient JOINs with proper indexing
- Minimal data transfer (only required fields)

### Caching Strategy
- Workspace averages cached per time range
- Breakdown results cached for common queries
- TTL-based expiration

### Monitoring
- Query execution time tracking
- Cache hit/miss ratios
- Error rate monitoring

## Testing Strategy

### Unit Tests
- Service method validation
- Filter normalization
- Edge cases (divide-by-zero, empty results)
- Security (workspace isolation)

### Integration Tests
- End-to-end QA vs KPI consistency
- Cross-endpoint validation
- Performance benchmarks
- Error handling

### Test Data
- Use existing seed data
- Add edge case scenarios
- Validate against known good values

## Breaking Changes

### API Changes
- KPI endpoint: `only_active` parameter behavior change
- QA endpoint: Default entity filtering behavior change
- All endpoints: Consistent provider enum handling

### Migration Notes
- Update UI clients to handle new defaults
- Update documentation for new behaviors
- Add deprecation warnings for old parameters

## Future Enhancements

### Phase 2 Features
- Advanced caching with Redis
- Real-time metric updates
- Custom metric definitions
- Performance analytics

### Phase 3 Features
- Machine learning insights
- Anomaly detection
- Predictive metrics
- Advanced visualizations

## References

- **Current Implementation**: `app/dsl/executor.py`, `app/routers/kpis.py`
- **Metrics Registry**: `app/metrics/registry.py`
- **Formulas**: `app/metrics/formulas.py`
- **Models**: `app/models.py`
- **Schemas**: `app/schemas.py`

## Changelog

### 2025-10-14 - Initial Implementation
- Created UnifiedMetricService architecture
- Defined filter contracts and interfaces
- Documented migration strategy
- Identified breaking changes and security considerations
