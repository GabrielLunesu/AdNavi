"use client";
import { useState } from "react";
import TopToolbar from "./components/TopToolbar";
import CampaignTableHeader from "./components/CampaignTableHeader";
import CampaignRow from "./components/CampaignRow";
import ActiveRulesPanel from "./components/ActiveRulesPanel";

// Mock campaign data - replace with real API data
const mockCampaigns = [
  {
    id: 1,
    name: 'Summer Sale 2024',
    created: 'Mar 15, 2024',
    platform: 'Meta',
    revenue: 4280,
    spend: 991,
    roas: 4.32,
    conversions: 612,
    cpc: 0.64,
    ctr: 3.2,
    status: 'Active',
    sparklineData: [3.8, 3.9, 4.1, 4.0, 4.2, 4.3, 4.32],
    detailChartData: {
      labels: ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5', 'Day 6', 'Day 7', 'Day 8', 'Day 9', 'Day 10', 'Day 11', 'Day 12', 'Day 13', 'Day 14'],
      data: [3.8, 3.9, 4.1, 4.0, 4.2, 4.3, 4.1, 4.4, 4.5, 4.2, 4.3, 4.4, 4.3, 4.32]
    },
    adSets: [
      { name: 'LAL 2% — US', status: 'Active', spend: 389, roas: 4.8, sparklineData: [3.2, 3.5, 3.8, 3.6, 4.0, 4.2, 4.8] },
      { name: 'Interest — Fashion', status: 'Active', spend: 412, roas: 4.1, sparklineData: [3.1, 3.4, 3.7, 3.5, 3.9, 4.0, 4.1] },
      { name: 'Retargeting — 30d', status: 'Active', spend: 190, roas: 3.9, sparklineData: [3.0, 3.2, 3.5, 3.4, 3.7, 3.8, 3.9] },
    ]
  },
  {
    id: 2,
    name: 'Spring Collection Launch',
    created: 'Apr 2, 2024',
    platform: 'Google',
    revenue: 3847,
    spend: 986,
    roas: 3.90,
    conversions: 528,
    cpc: 0.78,
    ctr: 2.8,
    status: 'Active',
    sparklineData: [3.5, 3.6, 3.7, 3.8, 3.9, 3.85, 3.90],
    detailChartData: {
      labels: ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5', 'Day 6', 'Day 7', 'Day 8', 'Day 9', 'Day 10', 'Day 11', 'Day 12', 'Day 13', 'Day 14'],
      data: [3.5, 3.6, 3.7, 3.75, 3.8, 3.85, 3.82, 3.88, 3.92, 3.87, 3.90, 3.88, 3.89, 3.90]
    },
    adSets: []
  },
  {
    id: 3,
    name: 'Brand Awareness — TikTok',
    created: 'Apr 10, 2024',
    platform: 'TikTok',
    revenue: 2946,
    spend: 921,
    roas: 3.20,
    conversions: 441,
    cpc: 0.89,
    ctr: 2.4,
    status: 'Active',
    sparklineData: [2.8, 2.9, 3.0, 3.1, 3.15, 3.18, 3.20],
    detailChartData: {
      labels: ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5', 'Day 6', 'Day 7', 'Day 8', 'Day 9', 'Day 10', 'Day 11', 'Day 12', 'Day 13', 'Day 14'],
      data: [2.8, 2.9, 3.0, 3.05, 3.1, 3.12, 3.15, 3.14, 3.17, 3.18, 3.19, 3.18, 3.19, 3.20]
    },
    adSets: []
  },
  {
    id: 4,
    name: 'Q2 Retargeting',
    created: 'Mar 28, 2024',
    platform: 'Meta',
    revenue: 2184,
    spend: 568,
    roas: 3.84,
    conversions: 312,
    cpc: 0.71,
    ctr: 2.9,
    status: 'Paused',
    sparklineData: [3.4, 3.5, 3.6, 3.7, 3.75, 3.80, 3.84],
    detailChartData: {
      labels: ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5', 'Day 6', 'Day 7', 'Day 8', 'Day 9', 'Day 10', 'Day 11', 'Day 12', 'Day 13', 'Day 14'],
      data: [3.4, 3.5, 3.55, 3.6, 3.65, 3.7, 3.72, 3.75, 3.78, 3.80, 3.82, 3.83, 3.84, 3.84]
    },
    adSets: []
  },
  {
    id: 5,
    name: 'Holiday Pre-Launch',
    created: 'Apr 5, 2024',
    platform: 'Google',
    revenue: 1923,
    spend: 614,
    roas: 3.13,
    conversions: 276,
    cpc: 0.92,
    ctr: 2.2,
    status: 'Active',
    sparklineData: [2.9, 3.0, 3.05, 3.08, 3.10, 3.12, 3.13],
    detailChartData: {
      labels: ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5', 'Day 6', 'Day 7', 'Day 8', 'Day 9', 'Day 10', 'Day 11', 'Day 12', 'Day 13', 'Day 14'],
      data: [2.9, 2.95, 3.0, 3.02, 3.05, 3.07, 3.08, 3.09, 3.10, 3.11, 3.12, 3.12, 3.13, 3.13]
    },
    adSets: []
  }
];

export default function CampaignsPage() {
  const [campaigns] = useState(mockCampaigns);

  const handlePlatformChange = (platform) => {
    console.log('Platform filter:', platform);
    // TODO: Filter campaigns by platform
  };

  const handleStatusChange = (status) => {
    console.log('Status filter:', status);
    // TODO: Filter campaigns by status
  };

  const handleSortChange = (sort) => {
    console.log('Sort by:', sort);
    // TODO: Sort campaigns
  };

  const handleTimeRangeChange = (timeRange) => {
    console.log('Time range:', timeRange);
    // TODO: Fetch data for time range
  };

  return (
    <div>
      {/* Floating Control Toolbar */}
      <TopToolbar
        onPlatformChange={handlePlatformChange}
        onStatusChange={handleStatusChange}
        onSortChange={handleSortChange}
        onTimeRangeChange={handleTimeRangeChange}
      />

      {/* Campaign Table */}
      <div className="space-y-0">
        {/* Table Header */}
        <CampaignTableHeader />

        {/* Table Body */}
        <div className="space-y-2 pb-2">
          {campaigns.map((campaign, index) => (
            <CampaignRow
              key={campaign.id}
              campaign={campaign}
              index={index}
              isLast={index === campaigns.length - 1}
            />
          ))}
        </div>
      </div>

      {/* Rules Section */}
      <ActiveRulesPanel />
    </div>
  );
}
