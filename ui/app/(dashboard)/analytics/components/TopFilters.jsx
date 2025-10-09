"use client";
import { useEffect, useState } from "react";
import { fetchWorkspaceProviders } from "../../../../lib/api";

export default function TopFilters({
  selectedProvider,
  availableProviders,
  setAvailableProviders,
  selectedTimeframe,
  rangeDays,
  workspaceId,
  onProviderChange,
  onTimeframeChange,
  onCustomDateApply
}) {
  const [loading, setLoading] = useState(true);
  const [showDatePicker, setShowDatePicker] = useState(false);
  const [startDate, setStartDate] = useState('');
  const [endDate, setEndDate] = useState('');

  // Fetch available providers on mount
  useEffect(() => {
    if (!workspaceId) return;
    
    let mounted = true;
    setLoading(true);
    
    fetchWorkspaceProviders({ workspaceId })
      .then((data) => {
        if (!mounted) return;
        setAvailableProviders(data.providers || []);
        setLoading(false);
      })
      .catch((err) => {
        console.error('Failed to fetch providers:', err);
        if (mounted) setLoading(false);
      });
    
    return () => { mounted = false; };
  }, [workspaceId, setAvailableProviders]);

  const timeframeOptions = [
    { id: '7d', label: '7d', days: 7 },
    { id: '30d', label: '30d', days: 30 },
    { id: 'custom', label: 'Custom', days: 0 }
  ];

  const handleTimeframeClick = (option) => {
    if (option.id === 'custom') {
      setShowDatePicker(true);
      onTimeframeChange(option.id, option.days);
    } else {
      setShowDatePicker(false);
      onTimeframeChange(option.id, option.days);
    }
  };

  const handleCustomDateApply = () => {
    if (startDate && endDate) {
      const start = new Date(startDate);
      const end = new Date(endDate);
      const diffTime = Math.abs(end - start);
      const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24)) + 1;
      
      onTimeframeChange('custom', diffDays);
      onCustomDateApply(startDate, endDate);
      setShowDatePicker(false);
    }
  };

  return (
    <div className="sticky top-0 z-10 bg-white/80 backdrop-blur-md border-b border-neutral-200/60 px-8 py-6 mb-8">
      <div className="flex items-center justify-between">
        {/* Provider Filter Buttons */}
        <div className="flex items-center gap-3">
          <span className="text-sm font-medium text-neutral-600 mr-2">Platform:</span>
          
          {loading ? (
            <div className="flex gap-2">
              {[1, 2, 3, 4].map(i => (
                <div key={i} className="w-20 h-9 bg-neutral-200 animate-pulse rounded-full"></div>
              ))}
            </div>
          ) : (
            <>
              {/* All button */}
              <button
                onClick={() => onProviderChange('all')}
                className={`px-4 py-2 rounded-full text-sm font-medium transition-all ${
                  selectedProvider === 'all'
                    ? 'bg-cyan-500 text-white shadow-lg'
                    : 'bg-neutral-100 text-neutral-700 hover:bg-neutral-200'
                }`}
              >
                All
              </button>
              
              {/* Dynamic provider buttons */}
              {availableProviders.map((provider) => (
                <button
                  key={provider}
                  onClick={() => onProviderChange(provider)}
                  className={`px-4 py-2 rounded-full text-sm font-medium transition-all capitalize ${
                    selectedProvider === provider
                      ? 'bg-cyan-500 text-white shadow-lg'
                      : 'bg-neutral-100 text-neutral-700 hover:bg-neutral-200'
                  }`}
                >
                  {provider}
                </button>
              ))}
            </>
          )}
        </div>

        {/* Timeframe Filter */}
        <div className="flex items-center gap-3">
          <span className="text-sm font-medium text-neutral-600 mr-2">Timeframe:</span>
          
          {timeframeOptions.map((option) => (
            <button
              key={option.id}
              onClick={() => handleTimeframeClick(option)}
              className={`px-4 py-2 rounded-full text-sm font-medium transition-all ${
                selectedTimeframe === option.id
                  ? 'bg-cyan-500 text-white shadow-lg'
                  : 'bg-neutral-100 text-neutral-700 hover:bg-neutral-200'
              }`}
            >
              {option.label}
            </button>
          ))}
        </div>
      </div>

      {/* Custom Date Picker */}
      {showDatePicker && (
        <div className="mt-6 glass-card rounded-3xl p-6 border border-neutral-200/60 shadow-lg animate-fade-up">
          <h3 className="text-sm font-semibold text-neutral-900 mb-4">Select Custom Date Range</h3>
          <div className="flex items-end gap-4">
            <div className="flex-1">
              <label className="block text-xs font-medium text-neutral-600 mb-2">Start Date</label>
              <input
                type="date"
                value={startDate}
                onChange={(e) => setStartDate(e.target.value)}
                className="w-full px-4 py-2 rounded-2xl border border-neutral-200 text-sm focus:outline-none focus:border-cyan-400 focus:ring-2 focus:ring-cyan-400/20"
              />
            </div>
            <div className="flex-1">
              <label className="block text-xs font-medium text-neutral-600 mb-2">End Date</label>
              <input
                type="date"
                value={endDate}
                onChange={(e) => setEndDate(e.target.value)}
                min={startDate}
                className="w-full px-4 py-2 rounded-2xl border border-neutral-200 text-sm focus:outline-none focus:border-cyan-400 focus:ring-2 focus:ring-cyan-400/20"
              />
            </div>
            <button
              onClick={handleCustomDateApply}
              disabled={!startDate || !endDate}
              className="px-6 py-2 rounded-2xl bg-cyan-500 text-white text-sm font-medium hover:bg-cyan-600 transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
            >
              Apply
            </button>
            <button
              onClick={() => setShowDatePicker(false)}
              className="px-6 py-2 rounded-2xl bg-neutral-100 text-neutral-700 text-sm font-medium hover:bg-neutral-200 transition-colors"
            >
              Cancel
            </button>
          </div>
        </div>
      )}
    </div>
  );
}

