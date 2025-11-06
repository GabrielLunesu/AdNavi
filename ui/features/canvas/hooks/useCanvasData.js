// WHAT: Fetch + map campaign/adset/ad/creative into Canvas nodes/edges (memoized)
// WHY: Keep data layer isolated from presentation; enable mock fallback
// REFERENCES: ui/lib/campaignsApiClient.js, ui/lib/campaignsAdapter.js, ./lib/mapping.js

import { useCallback, useEffect, useMemo, useState } from "react";
import { fetchEntityPerformance, invalidateEntityPerformanceCache } from "../../../lib/campaignsApiClient";
import { adaptEntityPerformance } from "../../../lib/campaignsAdapter";
import { entitiesToNodesAndEdges } from "../lib/mapping";
import { arrangeHierarchy } from "../lib/layout";

/**
 * useCanvasData
 * @param {Object} params
 * @param {string} params.workspaceId
 * @param {Object} params.filters - timeframe, platform, status
 * @param {boolean} params.useMock - when true, load mock dataset (no network)
 */
export default function useCanvasData({ workspaceId, filters = {}, useMock = false }) {
  const [loading, setLoading] = useState(!!workspaceId && !useMock);
  const [error, setError] = useState(null);
  const [data, setData] = useState({ nodes: [], edges: [] });
  const [lastSyncedAt, setLastSyncedAt] = useState(null);
  const [refreshIndex, setRefreshIndex] = useState(0);

  const {
    timeframe = "7d",
    status = "active",
    platform = null,
    showEdges = true,
    showAds = true,
  } = filters;

  useEffect(() => {
    let active = true;
    async function load() {
      if (useMock) {
        try {
          const mock = await import("../mock/demo-canvas.json");
          if (!active) return;
          let { nodes, edges } = { nodes: mock.default.nodes || [], edges: mock.default.edges || [] };
          // Apply horizontal layout to mock data as well
          ({ nodes, edges } = arrangeHierarchy(nodes, edges));
          setData({ nodes, edges });
          setLastSyncedAt(new Date());
          setLoading(false);
        } catch (e) {
          if (!active) return;
          setError("Failed to load mock data");
          setLoading(false);
        }
        return;
      }

      if (!workspaceId) return;
      setLoading(true);
      setError(null);
      try {
        // 1) Campaigns list
        const campaignsRes = await fetchEntityPerformance({
          workspaceId,
          entityLevel: "campaign",
          timeframe,
          platform,
          status,
          page: 1,
          pageSize: 50,
          sortBy: "roas",
          sortDir: "desc",
        });
        const campaigns = adaptEntityPerformance(campaignsRes);

        // 2) For each campaign, fetch children (ad sets → maybe ad/creative)
        const childrenBatches = await Promise.all(
          (campaigns.rows || []).map((row) =>
            fetchEntityPerformance({
              workspaceId,
              parentId: row.id,
              timeframe,
              platform,
              status,
              page: 1,
              pageSize: 50,
              sortBy: "roas",
              sortDir: "desc",
            })
          )
        );

        const adaptedChildren = childrenBatches.map(adaptEntityPerformance);

        const adsByAdset = new Map();
        if (showAds) {
          const adsetDescriptors = [];
          adaptedChildren.forEach((childAdapter) => {
            (childAdapter.rows || []).forEach((row) => {
              if (row.level === "adset") {
                adsetDescriptors.push({ adsetId: row.id });
              }
            });
          });

          if (adsetDescriptors.length > 0) {
            const adsResponses = await Promise.all(
              adsetDescriptors.map(({ adsetId }) =>
                fetchEntityPerformance({
                  workspaceId,
                  parentId: adsetId,
                  timeframe,
                  platform,
                  status,
                  page: 1,
                  pageSize: 50,
                  sortBy: "roas",
                  sortDir: "desc",
                })
              )
            );

            adsResponses
              .map(adaptEntityPerformance)
              .forEach((adapted, index) => {
                const descriptor = adsetDescriptors[index];
                if (descriptor) {
                  adsByAdset.set(descriptor.adsetId, adapted);
                }
              });
          }
        }

        let { nodes, edges } = entitiesToNodesAndEdges({
          campaigns,
          children: adaptedChildren,
          adsByAdset,
          filters: { showEdges, showAds },
        });
        // Deterministic hierarchical layout (campaign → ad set → ad columns)
        ({ nodes, edges } = arrangeHierarchy(nodes, edges));
        if (!active) return;
        setData({ nodes, edges });
        setLastSyncedAt(new Date());
      } catch (e) {
        if (!active) return;
        setError(e?.message || "Failed to load canvas data");
      } finally {
        if (active) setLoading(false);
      }
    }

    load();
    return () => {
      active = false;
    };
  }, [workspaceId, timeframe, status, platform, showEdges, showAds, useMock, refreshIndex]);

  const reload = useCallback(() => {
    if (!useMock && !workspaceId) {
      return;
    }
    invalidateEntityPerformanceCache();
    setRefreshIndex((idx) => idx + 1);
  }, [workspaceId, useMock]);

  return useMemo(
    () => ({ ...data, loading, error, reload, lastSyncedAt }),
    [data, loading, error, reload, lastSyncedAt]
  );
}
