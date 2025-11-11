"use client";
import { useState, useEffect } from "react";
import { ChevronDown, ArrowDownUp } from "lucide-react";
import { fetchWorkspaceProviders } from "@/lib/api";

export default function TopToolbar({ meta, filters, onPlatformChange, onStatusChange, onSortChange, onTimeRangeChange, loading, workspaceId, availableProviders, setAvailableProviders }) {
  const [providersLoading, setProvidersLoading] = useState(true);
  
  // Use filters from parent, with defaults
  // Note: platform is null for "all", so we need to convert it
  const selectedPlatform = filters?.platform === null || filters?.platform === 'all' ? 'all' : filters.platform;
  const selectedStatus = filters?.status || 'all';
  const selectedSort = filters?.sortBy || 'roas';
  const selectedTime = filters?.timeframe || '7d';

  // Fetch available providers on mount
  useEffect(() => {
    if (!workspaceId) return;
    
    let mounted = true;
    setProvidersLoading(true);
    
    fetchWorkspaceProviders({ workspaceId })
      .then((data) => {
        if (!mounted) return;
        if (setAvailableProviders) {
          setAvailableProviders(data.providers || []);
        }
        setProvidersLoading(false);
      })
      .catch((err) => {
        console.error('Failed to fetch providers:', err);
        if (mounted) setProvidersLoading(false);
      });
    
    return () => { mounted = false; };
  }, [workspaceId, setAvailableProviders]);

  const timeRanges = [
    { id: '7d', label: '7d' },
    { id: '30d', label: '30d' },
    { id: 'custom', label: 'Custom' },
  ];

  const statusOptions = ['all', 'active', 'paused'];

  const handleTimeChange = (id) => {
    onTimeRangeChange?.(id);
  };

  const handleStatusClick = (status) => {
    onStatusChange?.(status);
  };

  const handlePlatformClick = (platform) => {
    // Convert 'all' to null for parent component
    onPlatformChange?.(platform === 'all' ? null : platform);
  };

  return (
    <div className="sticky top-6 z-30 mb-8">
      <div className="glass-toolbar rounded-3xl border border-neutral-200/60 shadow-xl p-6 relative overflow-hidden">
        <div className="sync-pulse"></div>
        
        <div className="flex items-center justify-between mb-6">
          <div>
            <div className="flex items-center gap-2">
              <h1 className="text-4xl font-semibold tracking-tight text-neutral-900 mb-2">{meta?.title || 'Campaigns'}</h1>
              {loading ? <span className="text-xs text-cyan-400">Loading…</span> : null}
            </div>
            <p className="text-xs text-neutral-500">{meta?.subtitle || 'Last updated —'}</p>
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
            {/* Platform Filter - Dynamic buttons like Analytics */}
            <div className="flex items-center gap-2">
              {providersLoading ? (
                <div className="flex gap-2">
                  {[1, 2, 3].map(i => (
                    <div key={i} className="w-20 h-9 bg-neutral-200 animate-pulse rounded-full"></div>
                  ))}
                </div>
              ) : (
                <>
                  {/* All button */}
                  <button
                    onClick={() => handlePlatformClick('all')}
                    className={`px-4 py-2 rounded-full text-sm font-medium transition-all capitalize ${
                      selectedPlatform === 'all'
                        ? 'bg-cyan-500 text-white shadow-lg'
                        : 'bg-white/60 border border-neutral-200/60 text-neutral-700 hover:bg-white hover:border-cyan-400/40'
                    }`}
                  >
                    All
                  </button>
                  
                  {/* Dynamic provider buttons */}
                  {availableProviders && availableProviders.map((provider) => (
                    <button
                      key={provider}
                      onClick={() => handlePlatformClick(provider)}
                      className={`px-4 py-2 rounded-full text-sm font-medium transition-all capitalize ${
                        selectedPlatform === provider
                          ? 'bg-cyan-500 text-white shadow-lg'
                          : 'bg-white/60 border border-neutral-200/60 text-neutral-700 hover:bg-white hover:border-cyan-400/40'
                      }`}
                    >
                      {provider}
                    </button>
                  ))}
                </>
              )}
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
                  onSortChange?.(e.target.value, filters?.sortDir || 'desc');
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
            {/* <button className="w-10 h-10 rounded-full bg-white/60 border border-neutral-200/60 hover:border-cyan-400/40 hover:bg-white transition-all flex items-center justify-center">
              <Download className="w-4 h-4 text-neutral-600" strokeWidth={1.5} />
            </button>
            <button className="w-10 h-10 rounded-full bg-white/60 border border-neutral-200/60 hover:border-cyan-400/40 hover:bg-white transition-all flex items-center justify-center">
              <SlidersHorizontal className="w-4 h-4 text-neutral-600" strokeWidth={1.5} />
            </button> */}
          </div>
        </div>
      </div>
    </div>
  );
}

