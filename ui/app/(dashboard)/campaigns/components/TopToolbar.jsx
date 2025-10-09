"use client";
import { useState } from "react";
import { ChevronDown, ArrowDownUp, Download, SlidersHorizontal } from "lucide-react";

export default function TopToolbar({ onPlatformChange, onStatusChange, onSortChange, onTimeRangeChange }) {
  const [selectedPlatform, setSelectedPlatform] = useState('all');
  const [selectedStatus, setSelectedStatus] = useState('all');
  const [selectedSort, setSelectedSort] = useState('roas');
  const [selectedTime, setSelectedTime] = useState('7d');

  const timeRanges = [
    { id: '7d', label: '7d' },
    { id: '30d', label: '30d' },
    { id: 'custom', label: 'Custom' },
  ];

  const statusOptions = ['all', 'active', 'paused'];

  const handleTimeChange = (id) => {
    setSelectedTime(id);
    onTimeRangeChange?.(id);
  };

  const handleStatusClick = (status) => {
    setSelectedStatus(status);
    onStatusChange?.(status);
  };

  return (
    <div className="sticky top-6 z-30 mb-8">
      <div className="glass-toolbar rounded-3xl border border-neutral-200/60 shadow-xl p-6 relative overflow-hidden">
        <div className="sync-pulse"></div>
        
        <div className="flex items-center justify-between mb-6">
          <div>
            <h1 className="text-4xl font-semibold tracking-tight text-neutral-900 mb-2">Campaigns</h1>
            <div className="h-0.5 w-20 bg-gradient-to-r from-cyan-400 to-transparent"></div>
          </div>
          
          {/* Time Range */}
          <div className="flex items-center gap-2">
            {timeRanges.map((range) => (
              <button
                key={range.id}
                onClick={() => handleTimeChange(range.id)}
                className={`px-4 py-2 rounded-full text-sm font-medium border transition-all ${
                  selectedTime === range.id
                    ? 'bg-white text-neutral-900 border-cyan-400/40 shadow-sm'
                    : 'bg-white/40 text-neutral-600 border-neutral-200/40 hover:border-cyan-400/40 hover:bg-white'
                }`}
              >
                {range.label}
              </button>
            ))}
          </div>
        </div>
        
        <div className="flex items-center gap-4 justify-between">
          {/* Left Filters */}
          <div className="flex items-center gap-3">
            {/* Platform Filter */}
            <div className="relative">
              <select
                value={selectedPlatform}
                onChange={(e) => {
                  setSelectedPlatform(e.target.value);
                  onPlatformChange?.(e.target.value);
                }}
                className="px-4 py-2.5 pr-10 rounded-full bg-white/60 text-neutral-900 text-sm font-medium border border-neutral-200/60 hover:border-cyan-400/40 transition-all appearance-none cursor-pointer"
              >
                <option value="all">All Platforms</option>
                <option value="meta">Meta</option>
                <option value="google">Google</option>
                <option value="tiktok">TikTok</option>
              </select>
              <ChevronDown className="w-4 h-4 absolute right-3 top-1/2 -translate-y-1/2 text-neutral-500 pointer-events-none" strokeWidth={1.5} />
            </div>
            
            {/* Status Filter */}
            <div className="flex items-center gap-2 px-1 py-1 rounded-full bg-white/60 border border-neutral-200/60">
              {statusOptions.map((status) => (
                <button
                  key={status}
                  onClick={() => handleStatusClick(status)}
                  className={`px-4 py-1.5 rounded-full text-sm font-medium transition-all capitalize ${
                    selectedStatus === status
                      ? 'bg-white text-cyan-600 border border-cyan-400/40 shadow-sm'
                      : 'text-neutral-600 hover:bg-white'
                  }`}
                >
                  {status}
                </button>
              ))}
            </div>
          </div>
          
          {/* Right Actions */}
          <div className="flex items-center gap-3">
            {/* Sort */}
            <div className="relative">
              <select
                value={selectedSort}
                onChange={(e) => {
                  setSelectedSort(e.target.value);
                  onSortChange?.(e.target.value);
                }}
                className="px-4 py-2.5 pr-10 rounded-full bg-white/60 text-neutral-900 text-sm font-medium border border-neutral-200/60 hover:border-cyan-400/40 transition-all appearance-none cursor-pointer"
              >
                <option value="roas">Sort by ROAS</option>
                <option value="revenue">Sort by Revenue</option>
                <option value="spend">Sort by Spend</option>
                <option value="conversions">Sort by Conversions</option>
              </select>
              <ArrowDownUp className="w-4 h-4 absolute right-3 top-1/2 -translate-y-1/2 text-neutral-500 pointer-events-none" strokeWidth={1.5} />
            </div>
            
            {/* Export & Customize */}
            <button className="w-10 h-10 rounded-full bg-white/60 border border-neutral-200/60 hover:border-cyan-400/40 hover:bg-white transition-all flex items-center justify-center">
              <Download className="w-4 h-4 text-neutral-600" strokeWidth={1.5} />
            </button>
            <button className="w-10 h-10 rounded-full bg-white/60 border border-neutral-200/60 hover:border-cyan-400/40 hover:bg-white transition-all flex items-center justify-center">
              <SlidersHorizontal className="w-4 h-4 text-neutral-600" strokeWidth={1.5} />
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}

