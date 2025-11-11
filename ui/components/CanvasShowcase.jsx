"use client";

import React, { useMemo, useState, useCallback } from "react";
import dynamic from "next/dynamic";
import { motion, AnimatePresence } from "framer-motion";
import { GitBranch, X } from "lucide-react";
import { Handle, Position } from "@xyflow/react";
import { entitiesToNodesAndEdges } from "@/features/canvas/lib/mapping";
import { arrangeHierarchy } from "@/features/canvas/lib/layout";

// Dynamically import FlowViewport to avoid SSR issues
const FlowViewport = dynamic(() => import("@/features/canvas/components/FlowViewport"), { ssr: false });

// Custom Campaign Node - Shows only revenue, popup on click
const ShowcaseCampaignNode = ({ data, selected }) => {
  const { name, status, kpis = {}, platform } = data || {};
  const revenue = kpis.revenue || "$0";
  
  return (
    <div className="glass-card rounded-2xl border border-neutral-200/40 shadow-lg hover:shadow-xl transition-all cursor-pointer w-[260px] h-[160px] overflow-hidden">
      <Handle type="target" position={Position.Left} className="w-2 h-2 !bg-[#B9C7F5]" />
      <Handle type="source" position={Position.Right} className="w-2 h-2 !bg-[#B9C7F5]" />
      <div className="p-4 relative h-full flex flex-col">
        <div className="flex items-start justify-between mb-3">
          <h3 className="text-sm font-medium text-[#111] tracking-tight truncate flex-1 pr-2">{name || "—"}</h3>
          <div className={`w-2 h-2 rounded-full flex-shrink-0 ${status === "active" ? "bg-green-500" : "bg-neutral-400"}`}></div>
        </div>
        <div className="flex-1 flex items-center justify-center">
          <div className="text-center">
            <div className="text-[10px] text-neutral-500 uppercase tracking-wide mb-1">Revenue</div>
            <div className="text-2xl font-semibold text-[#111]">{revenue}</div>
          </div>
        </div>
        <div className="flex items-center justify-between pt-2 mt-auto border-t border-neutral-200/40 text-[10px] text-neutral-500 flex-shrink-0">
          <span className="px-2 py-0.5 rounded-full bg-white/60 border border-neutral-200/60 truncate max-w-[100px]">{platform || "—"}</span>
        </div>
      </div>
    </div>
  );
};

// Custom AdSet Node - Shows only revenue, popup on click
const ShowcaseAdSetNode = ({ data, selected }) => {
  const { name, status, kpis = {} } = data || {};
  const revenue = kpis.revenue || "$0";
  
  return (
    <div className="glass-card rounded-2xl border border-neutral-200/40 shadow-lg hover:shadow-xl transition-all cursor-pointer w-[180px] h-[120px] overflow-hidden">
      <Handle type="target" position={Position.Left} className="w-2 h-2 !bg-[#B9C7F5]" />
      <Handle type="source" position={Position.Right} className="w-2 h-2 !bg-[#B9C7F5]" />
      <div className="p-3 relative h-full flex flex-col">
        <div className="flex items-start justify-between mb-2 flex-shrink-0">
          <h4 className="text-xs font-medium text-[#111] truncate flex-1 pr-2">{name || "—"}</h4>
          <div className={`w-1.5 h-1.5 rounded-full flex-shrink-0 ${status === "active" ? "bg-green-500" : "bg-neutral-400"}`}></div>
        </div>
        <div className="flex-1 flex items-center justify-center">
          <div className="text-center">
            <div className="text-[9px] text-neutral-500 uppercase tracking-wide mb-1">Revenue</div>
            <div className="text-xl font-semibold text-[#111]">{revenue}</div>
          </div>
        </div>
      </div>
    </div>
  );
};

// Custom Ad Node - Shows only revenue, popup on click
const ShowcaseAdNode = ({ data, selected }) => {
  const { name, kpis = {} } = data || {};
  const revenue = kpis.revenue || "$0";
  
  return (
    <div className="glass-card rounded-2xl border border-neutral-200/40 shadow-lg hover:shadow-xl transition-all cursor-pointer w-[140px] h-[120px] overflow-hidden">
      <Handle type="target" position={Position.Left} className="w-2 h-2 !bg-[#B9C7F5]" />
      <div className="p-3 relative h-full flex flex-col">
        <div className="flex items-center justify-between mb-2 flex-shrink-0">
          <span className="text-xs font-medium text-[#111] truncate">{name || "—"}</span>
        </div>
        <div className="flex-1 flex items-center justify-center">
          <div className="text-center">
            <div className="text-[8px] text-neutral-500 uppercase tracking-wide mb-1">Revenue</div>
            <div className="text-lg font-semibold text-[#111]">{revenue}</div>
          </div>
        </div>
      </div>
    </div>
  );
};

// Popup component for showing full metrics - animated node above clicked node
const MetricsPopup = ({ node, position, onClose }) => {
  if (!node || !position) return null;
  
  const { name, kpis = {}, platform, status } = node.data || {};
  
  return (
    <motion.div
      initial={{ opacity: 0, scale: 0.8, y: 20 }}
      animate={{ opacity: 1, scale: 1, y: 0 }}
      exit={{ opacity: 0, scale: 0.8, y: 20 }}
      transition={{ duration: 0.2, ease: "easeOut" }}
      className="absolute z-50 glass-card rounded-2xl border border-neutral-200/60 shadow-2xl p-4 min-w-[220px] backdrop-blur-sm"
      style={{
        left: `${position.x}px`,
        top: `${position.y}px`,
        transform: 'translateX(-50%) translateY(-100%)',
        marginTop: '-12px'
      }}
    >
      {/* Close button */}
      <button 
        onClick={onClose}
        className="absolute top-2 right-2 text-neutral-400 hover:text-neutral-600 transition-colors p-1 rounded-full hover:bg-neutral-100"
      >
        <X className="w-3.5 h-3.5" />
      </button>
      
      {/* Header */}
      <div className="mb-3 pr-6">
        <h4 className="text-sm font-semibold text-[#111] truncate">{name}</h4>
      </div>
      
      {/* Metrics */}
      <div className="space-y-2">
        <MetricRow label="Revenue" value={kpis.revenue || "—"} />
        <MetricRow label="Spend" value={kpis.spend || "—"} />
        <MetricRow label="ROAS" value={kpis.roas || "—"} />
        <MetricRow label="CTR" value={kpis.ctr || "—"} />
        <MetricRow label="CPA" value={kpis.cpa || "—"} />
      </div>
      
      {/* Footer */}
      {platform && (
        <div className="mt-3 pt-3 border-t border-neutral-200/40">
          <span className="text-[10px] text-neutral-500">{platform}</span>
        </div>
      )}
    </motion.div>
  );
};

const MetricRow = ({ label, value }) => (
  <div className="flex items-center justify-between">
    <span className="text-[10px] text-neutral-500 uppercase tracking-wide">{label}</span>
    <span className="text-sm font-medium text-[#111]">{value}</span>
  </div>
);

// Hardcoded Meta ecommerce campaign data
const mockCampaigns = {
  rows: [
    {
      id: 1,
      name: "Black Friday CBO - Scale",
      status: "active",
      platform: "Meta",
      level: "campaign",
      display: {
        revenue: "$89.2K",
        spend: "$24.5K",
        roas: "3.63x",
        ctr: "2.1%",
        cpa: "$12.50",
      },
    },
  ],
};

const mockChildren = [
  {
    rows: [
      {
        id: 2,
        name: "50% off site wide",
        status: "active",
        platform: "Meta",
        level: "adset",
        display: {
          revenue: "$45.8K",
          spend: "$12.2K",
          roas: "3.75x",
          ctr: "2.3%",
          cpa: "$11.20",
        },
      },
      {
        id: 3,
        name: "Free shipping over $50",
        status: "active",
        platform: "Meta",
        level: "adset",
        display: {
          revenue: "$28.4K",
          spend: "$8.1K",
          roas: "3.51x",
          ctr: "1.9%",
          cpa: "$14.30",
        },
      },
      {
        id: 4,
        name: "New arrivals",
        status: "active",
        platform: "Meta",
        level: "adset",
        display: {
          revenue: "$15.0K",
          spend: "$4.2K",
          roas: "3.57x",
          ctr: "2.0%",
          cpa: "$13.80",
        },
      },
    ],
  },
];

const mockAdsByAdset = new Map([
  [
    2,
    {
      rows: [
        {
          id: 5,
          name: "Video Ad - 50% Sale",
          status: "active",
          platform: "Meta",
          level: "ad",
          display: {
            revenue: "$22.5K",
            spend: "$6.1K",
            roas: "3.69x",
            ctr: "2.5%",
            cpa: "$10.90",
          },
        },
        {
          id: 6,
          name: "Carousel - Products",
          status: "active",
          platform: "Meta",
          level: "ad",
          display: {
            revenue: "$23.3K",
            spend: "$6.1K",
            roas: "3.82x",
            ctr: "2.1%",
            cpa: "$11.50",
          },
        },
      ],
    },
  ],
  [
    3,
    {
      rows: [
        {
          id: 7,
          name: "Static - Free Shipping",
          status: "active",
          platform: "Meta",
          level: "ad",
          display: {
            revenue: "$28.4K",
            spend: "$8.1K",
            roas: "3.51x",
            ctr: "1.9%",
            cpa: "$14.30",
          },
        },
      ],
    },
  ],
  [
    4,
    {
      rows: [
        {
          id: 8,
          name: "Story Ad - New Items",
          status: "active",
          platform: "Meta",
          level: "ad",
          display: {
            revenue: "$15.0K",
            spend: "$4.2K",
            roas: "3.57x",
            ctr: "2.0%",
            cpa: "$13.80",
          },
        },
      ],
    },
  ],
]);

const nodeTypes = {
  campaign: ShowcaseCampaignNode,
  adset: ShowcaseAdSetNode,
  ad: ShowcaseAdNode,
};

export const CanvasShowcase = () => {
  const [selectedNode, setSelectedNode] = useState(null);
  const [popupPosition, setPopupPosition] = useState(null);

  // Use the same mapping and layout utilities as the real canvas
  const { nodes: rawNodes, edges: rawEdges } = useMemo(() => {
    return entitiesToNodesAndEdges({
      campaigns: mockCampaigns,
      children: mockChildren,
      adsByAdset: mockAdsByAdset,
      filters: { showAds: true, showEdges: true },
    });
  }, []);

  const { nodes, edges } = useMemo(() => {
    const arranged = arrangeHierarchy(rawNodes, rawEdges, {
      startX: 80,
      startY: 40,
      columnGap: 320,
      rowGap: 80,
    });
    
    // Add onNodeClick handler and ensure revenue is in kpis
    return {
      nodes: arranged.nodes.map(node => {
        // Get original data from mock data to include all display fields
        const nodeId = node.id.split(':')[1];
        let originalData = null;
        
        // Find original data from mock structures
        if (node.type === 'campaign') {
          originalData = mockCampaigns.rows.find(r => r.id.toString() === nodeId);
        } else if (node.type === 'adset') {
          originalData = mockChildren[0]?.rows.find(r => r.id.toString() === nodeId);
        } else if (node.type === 'ad') {
          for (const [adsetId, adData] of mockAdsByAdset.entries()) {
            const found = adData.rows.find(r => r.id.toString() === nodeId);
            if (found) {
              originalData = found;
              break;
            }
          }
        }
        
        return {
          ...node,
          data: {
            ...node.data,
            kpis: {
              ...node.data.kpis,
              revenue: originalData?.display?.revenue || node.data.kpis?.revenue,
              cpa: originalData?.display?.cpa || node.data.kpis?.cpa,
            },
          },
        };
      }),
      edges: arranged.edges,
    };
  }, [rawNodes, rawEdges]);

  const handleNodeClick = useCallback((event, node) => {
    setSelectedNode(node);
    // Get click position relative to container
    const container = document.querySelector('[data-canvas-container]');
    if (container && event) {
      const rect = container.getBoundingClientRect();
      // Position popup above the clicked node
      setPopupPosition({
        x: event.clientX - rect.left,
        y: event.clientY - rect.top,
      });
    }
  }, []);

  const handlePaneClick = useCallback(() => {
    setSelectedNode(null);
    setPopupPosition(null);
  }, []);

  return (
    <div className="relative w-full h-[500px] bg-white/40 rounded-2xl border border-neutral-200/40 overflow-hidden" data-canvas-container>
      {/* Header */}
      <div className="absolute top-4 left-4 flex items-center gap-2 z-10 backdrop-blur-sm bg-white/60 px-3 py-1.5 rounded-full border border-neutral-200/60">
        <GitBranch className="w-4 h-4 text-cyan-600" strokeWidth={1.5} />
        <span className="text-xs font-medium text-neutral-700">Campaign Canvas</span>
      </div>

      {/* Metrics Popup */}
      <AnimatePresence>
        {selectedNode && popupPosition && (
          <MetricsPopup
            key={selectedNode.id}
            node={selectedNode}
            position={popupPosition}
            onClose={() => {
              setSelectedNode(null);
              setPopupPosition(null);
            }}
          />
        )}
      </AnimatePresence>

      {/* FlowViewport - uses the same component as the real canvas */}
      <FlowViewport
        className="h-full"
        initialNodes={nodes}
        initialEdges={edges}
        nodeTypes={nodeTypes}
        options={{
          fitView: true,
          fitViewOptions: { padding: 0.2, maxZoom: 1 },
          defaultViewport: { x: 0, y: 0, zoom: 0.9 },
          minZoom: 0.5,
          maxZoom: 1.5,
          defaultEdgeOptions: {
            type: "bezier",
            animated: true,
            style: { stroke: "#B9C7F5", strokeWidth: 1.5, opacity: 0.85 },
          },
          panOnDrag: true,
          snapGrid: [10, 10],
          snapToGrid: true,
        }}
        onNodeClick={handleNodeClick}
        onPaneClick={handlePaneClick}
      />

      {/* Legend */}
      <div className="absolute bottom-4 left-4 flex items-center gap-4 text-[10px] text-neutral-600 backdrop-blur-sm bg-white/60 px-3 py-2 rounded-full border border-neutral-200/60">
        <div className="flex items-center gap-1.5">
          <div className="w-3 h-3 rounded bg-white border border-neutral-300 shadow-sm"></div>
          <span className="font-medium">Campaign</span>
        </div>
        <div className="flex items-center gap-1.5">
          <div className="w-3 h-3 rounded bg-white border border-neutral-300 shadow-sm"></div>
          <span className="font-medium">Ad Set</span>
        </div>
        <div className="flex items-center gap-1.5">
          <div className="w-3 h-3 rounded bg-white border border-neutral-300 shadow-sm"></div>
          <span className="font-medium">Ad</span>
        </div>
      </div>
    </div>
  );
};

