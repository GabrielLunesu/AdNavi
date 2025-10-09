"use client";
import { Download } from "lucide-react";
import { useState } from "react";

export default function TopBar({ onPeriodChange, compareEnabled, onCompareToggle }) {
  const [selectedPeriod, setSelectedPeriod] = useState('this-month');

  const periods = [
    { id: 'this-month', label: 'This Month' },
    { id: 'last-month', label: 'Last Month' },
    { id: 'custom', label: 'Custom' },
  ];

  const handlePeriodClick = (id) => {
    setSelectedPeriod(id);
    onPeriodChange?.(id);
  };

  return (
    <div className="sticky top-6 z-30 mb-8">
      <div className="glass-bar rounded-3xl border border-black/5 shadow-2xl p-8 relative overflow-hidden">
        {/* Cyan divider glow */}
        <div className="absolute bottom-0 left-0 right-0 h-0.5 bg-gradient-to-r from-transparent via-cyan-400 to-transparent opacity-40"></div>
        
        <div className="flex items-center justify-between mb-6">
          <div>
            <h1 className="text-4xl font-semibold tracking-tight text-black">Finance & P&L Overview</h1>
            <div className="h-0.5 w-24 bg-gradient-to-r from-cyan-400 to-transparent mt-3"></div>
          </div>
          
          <div className="flex items-center gap-3">
            {/* Period Selector */}
            <div className="flex items-center gap-2 px-1 py-1 rounded-full bg-white/60 border border-black/5">
              {periods.map((period) => (
                <button
                  key={period.id}
                  onClick={() => handlePeriodClick(period.id)}
                  className={`px-5 py-2 rounded-full text-sm font-medium transition-all ${
                    selectedPeriod === period.id
                      ? 'bg-white text-cyan-600 border border-cyan-400/40 shadow-sm'
                      : 'text-neutral-600 hover:bg-white'
                  }`}
                >
                  {period.label}
                </button>
              ))}
            </div>
            
            {/* Export Button */}
            <button className="px-5 py-2.5 rounded-full bg-black text-white text-sm font-medium border border-cyan-400/40 shadow-lg shadow-cyan-500/20 hover:shadow-cyan-500/40 transition-all flex items-center gap-2 relative overflow-hidden group">
              <span className="relative z-10">Export</span>
              <Download className="w-4 h-4 relative z-10" strokeWidth={1.5} />
              <div className="absolute inset-0 bg-gradient-to-r from-transparent via-cyan-400/20 to-transparent shimmer-effect opacity-0 group-hover:opacity-100"></div>
            </button>
          </div>
        </div>
        
        {/* Comparison Toggle */}
        <div className="flex items-center gap-3">
          <label className="flex items-center gap-3 cursor-pointer group">
            <div className="relative w-12 h-6 bg-white/60 rounded-full border border-black/5 transition-all">
              <input
                type="checkbox"
                className="sr-only peer"
                checked={compareEnabled}
                onChange={(e) => onCompareToggle?.(e.target.checked)}
              />
              <div className={`absolute top-0.5 left-0.5 w-5 h-5 bg-cyan-500 rounded-full transition-all shadow-sm ${compareEnabled ? 'translate-x-6' : ''}`}></div>
            </div>
            <span className="text-sm font-medium text-neutral-600 group-hover:text-black transition-all">Compare vs previous period</span>
          </label>
        </div>
      </div>
    </div>
  );
}

