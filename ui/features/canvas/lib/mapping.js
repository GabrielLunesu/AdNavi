// WHAT: Mapping helpers from unified entities (Campaigns API adapter) → Canvas nodes/edges
// WHY: Keep layout/presentation decoupled from backend contracts
// REFERENCES: ui/lib/campaignsAdapter.js, ui/lib/campaignsApiClient.js

const nodeId = (prefix, id) => `${prefix}:${id}`;

/** Map adapted campaign/adset/ad rows to Canvas nodes */
export function entitiesToNodesAndEdges({ campaigns, children = [], adsByAdset = new Map(), filters = {} }) {
  const nodes = [];
  const edges = [];

  const includeAds = filters.showAds !== false;
  const hideEdges = filters.showEdges === false;

  const campaignRows = campaigns.rows || [];
  campaignRows.forEach((c) => {
    const id = nodeId("campaign", c.id);
    nodes.push({
      id,
      type: "campaign",
      position: { x: 0, y: 0 },
      data: buildNodeData(c),
    });
  });

  children.forEach((childAdapter, idx) => {
    const campaign = campaignRows[idx];
    if (!campaign) return;
    const campaignNodeId = nodeId("campaign", campaign.id);

    (childAdapter.rows || []).forEach((row) => {
      const adsetId = nodeId("adset", row.id);
      nodes.push({
        id: adsetId,
        type: "adset",
        position: { x: 0, y: 0 },
        data: buildNodeData(row),
      });

      edges.push(makeEdge(campaignNodeId, adsetId, hideEdges));

      if (!includeAds) {
        return;
      }

      const ads = adsByAdset.get(row.id);
      (ads?.rows || []).forEach((adRow) => {
        const adType = inferLeafType(adRow);
        const adNodeId = nodeId(adType, adRow.id);
        nodes.push({
          id: adNodeId,
          type: "ad",
          position: { x: 0, y: 0 },
          data: buildNodeData(adRow),
        });

        edges.push(makeEdge(adsetId, adNodeId, hideEdges));
      });
    });
  });

  return { nodes, edges };
}

function inferLeafType(row) {
  if (row.level === "creative") return "ad";
  if (row.level === "ad") return "ad";
  if (row.level === "adset") return "adset";
  return "ad";
}

function buildNodeData(row) {
  return {
    name: row.name,
    status: row.status,
    platform: row.platform,
    kpis: {
      spend: row.display?.spend,
      roas: row.display?.roas,
      ctr: row.display?.ctr,
    },
  };
}

function makeEdge(source, target, hidden = false) {
  return {
    id: `${source}->${target}`,
    source,
    target,
    type: "bezier",
    animated: true,
    hidden,
    style: { stroke: "#B9C7F5", strokeWidth: 1.5, opacity: 0.85 },
  };
}
