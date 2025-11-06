// WHAT: Deterministic hierarchical layout for Canvas
// WHY: Keep campaign → ad set → ad in clear columns without overlap
// REFERENCES: docs/canvas/01-functional-spec.md

const SIZES = {
  campaign: { w: 260, h: 160 },
  adset: { w: 180, h: 120 },
  ad: { w: 140, h: 120 },
};

/**
 * Arrange nodes into three columns (campaign → ad set → ad) with consistent spacing.
 * @param {Array} nodes
 * @param {Array} edges
 * @param {Object} opts
 * @returns {{nodes: Array, edges: Array}}
 */
export function arrangeHierarchy(nodes, edges, opts = {}) {
  const startX = opts.startX ?? 80;
  const startY = opts.startY ?? 40;
  const columnGap = opts.columnGap ?? 320;
  const rowGap = opts.rowGap ?? 80;
  const groupGap = opts.groupGap ?? 240;
  const groupStride =
    opts.groupStride ??
    (SIZES.campaign.w + SIZES.adset.w + SIZES.ad.w + columnGap * 2 + groupGap);

  const byId = new Map(nodes.map((node) => [node.id, { ...node }]));
  const childMap = new Map();

  edges.forEach((edge) => {
    if (!childMap.has(edge.source)) {
      childMap.set(edge.source, []);
    }
    childMap.get(edge.source).push(edge.target);
  });

  const campaigns = nodes.filter((node) => node.type === "campaign");

  campaigns.forEach((campaign, idx) => {
    const adsetIds = childMap.get(campaign.id) || [];
    const adsets = adsetIds
      .map((id) => byId.get(id))
      .filter(Boolean)
      .filter((node) => node.type === "adset");

    if (adsets.length === 0) {
      byId.set(campaign.id, {
        ...campaign,
        position: { x: startX + idx * groupStride, y: startY },
      });
      return;
    }

    const campaignX = startX + idx * groupStride;
    const adsetX = campaignX + SIZES.campaign.w + columnGap;
    const adX = adsetX + SIZES.adset.w + columnGap;
    const groupTop = startY;

    let laneCursor = groupTop;
    const lanes = [];

    adsets.forEach((adset) => {
      const adIds = childMap.get(adset.id) || [];
      const ads = adIds
        .map((id) => byId.get(id))
        .filter(Boolean)
        .filter((node) => node.type === "ad");

      const adsCount = ads.length;
      const adsStackHeight = adsCount > 0 ? adsCount * (SIZES.ad.h + rowGap) - rowGap : 0;
      const laneHeight = Math.max(SIZES.adset.h, adsStackHeight || SIZES.adset.h);
      const adsetTop = laneCursor + (laneHeight - SIZES.adset.h) / 2;

      byId.set(adset.id, {
        ...adset,
        position: { x: adsetX, y: Math.round(adsetTop) },
      });

      if (adsCount > 0) {
        const adsTop = laneCursor + (laneHeight - adsStackHeight) / 2;
        ads.forEach((ad, index) => {
          const y = adsTop + index * (SIZES.ad.h + rowGap);
          byId.set(ad.id, {
            ...ad,
            position: { x: adX, y: Math.round(y) },
          });
        });
      }

      lanes.push(laneHeight);
      laneCursor += laneHeight + rowGap;
    });

    const totalLaneHeight =
      lanes.reduce((acc, height, index) => acc + height + (index === lanes.length - 1 ? 0 : rowGap), 0) ||
      SIZES.campaign.h;
    const campaignY = groupTop + (totalLaneHeight - SIZES.campaign.h) / 2;

    byId.set(campaign.id, {
      ...campaign,
      position: { x: campaignX, y: Math.round(campaignY) },
    });
  });

  return { nodes: Array.from(byId.values()), edges };
}

export default arrangeHierarchy;
