"use client";
import { useState } from "react";
import Sparkline from "./Sparkline";
import ExpandedDetail from "./ExpandedDetail";

function PlatformBadge({ platform }) {
  const config = {
    meta: { color: 'bg-blue-500', letter: 'M', label: 'Meta' },
    google: { color: 'bg-red-500', letter: 'G', label: 'Google' },
    tiktok: { color: 'bg-black', letter: 'T', label: 'TikTok' },
  };
  
  const { color, letter, label } = config[platform.toLowerCase()] || config.meta;
  
  return (
    <span className="inline-flex items-center gap-1.5 text-sm text-neutral-700">
      <div className={`w-5 h-5 rounded ${color} flex items-center justify-center text-white text-xs font-semibold`}>
        {letter}
      </div>
      {label}
    </span>
  );
}

function StatusPill({ status }) {
  const isActive = status.toLowerCase() === 'active';
  return (
    <span className={`inline-flex px-3 py-1 rounded-full text-xs font-medium ${isActive ? 'pill-active' : 'pill-paused'}`}>
      {status}
    </span>
  );
}

export default function CampaignRow({ campaign, index, isLast }) {
  const [isExpanded, setIsExpanded] = useState(false);

  return (
    <div
      className={`campaign-row glass-card border border-neutral-200/60 ${isLast && !isExpanded ? 'rounded-b-3xl' : ''} px-8 py-6 cursor-pointer relative overflow-hidden fade-up-in`}
      style={{ animationDelay: `${index * 40}ms` }}
      onClick={() => setIsExpanded(!isExpanded)}
    >
      <div className="glow-edge-hover"></div>
      <div className="grid grid-cols-12 gap-4 items-center">
        <div className="col-span-3">
          <p className="text-base font-semibold text-neutral-900">{campaign.name}</p>
          <p className="text-sm text-neutral-500 mt-0.5">Created {campaign.created}</p>
        </div>
        <div className="col-span-1">
          <PlatformBadge platform={campaign.platform} />
        </div>
        <div className="col-span-1 text-right">
          <p className="text-base font-semibold text-neutral-900">${campaign.revenue.toLocaleString()}</p>
        </div>
        <div className="col-span-1 text-right">
          <p className="text-base font-medium text-neutral-700">${campaign.spend.toLocaleString()}</p>
        </div>
        <div className="col-span-1 text-right">
          <p className="text-base font-semibold text-cyan-600">{campaign.roas}x</p>
        </div>
        <div className="col-span-1 text-right">
          <p className="text-base font-medium text-neutral-700">{campaign.conversions}</p>
        </div>
        <div className="col-span-1 text-right">
          <p className="text-sm font-medium text-neutral-700">${campaign.cpc}</p>
        </div>
        <div className="col-span-1 text-right">
          <p className="text-sm font-medium text-neutral-700">{campaign.ctr}%</p>
        </div>
        <div className="col-span-1">
          <StatusPill status={campaign.status} />
        </div>
        <div className="col-span-1">
          <Sparkline data={campaign.sparklineData} />
        </div>
      </div>
      
      {/* Expanded Section */}
      {isExpanded && (
        <ExpandedDetail campaign={campaign} />
      )}
    </div>
  );
}

