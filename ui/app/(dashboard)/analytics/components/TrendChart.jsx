"use client";
import { useState } from "react";

export default function TrendChart() {
  const [selectedMetric, setSelectedMetric] = useState('revenue');
  const [normalize, setNormalize] = useState(false);
  const [compare, setCompare] = useState(true);

  const metrics = [
    { id: 'revenue', label: 'Revenue' },
    { id: 'spend', label: 'Spend' },
    { id: 'roas', label: 'ROAS' },
    { id: 'ctr', label: 'CTR' },
    { id: 'cpa', label: 'CPA' },
  ];

  // Simple placeholder chart visualization
  return (
    <div className="mx-8 mb-8">
      <div className="glass-card rounded-3xl p-8 border border-neutral-200/60 shadow-lg relative overflow-hidden">
        <div className="absolute inset-0 bg-gradient-to-br from-cyan-50/30 via-transparent to-transparent pointer-events-none"></div>
        
        {/* Header with Tabs */}
        <div className="flex items-center justify-between mb-6 relative z-10">
          <div className="flex items-center gap-1 bg-white/60 rounded-2xl p-1 border border-neutral-200/60">
            {metrics.map((metric) => (
              <button
                key={metric.id}
                onClick={() => setSelectedMetric(metric.id)}
                className={`px-4 py-2 rounded-xl text-sm font-medium transition-all relative ${
                  selectedMetric === metric.id
                    ? 'bg-cyan-500 text-white shadow-sm'
                    : 'text-neutral-600 hover:bg-white/80'
                }`}
              >
                {metric.label}
                {selectedMetric === metric.id && (
                  <div className="absolute bottom-0 left-1/2 -translate-x-1/2 w-1/2 h-0.5 bg-cyan-300 rounded-full"></div>
                )}
              </button>
            ))}
          </div>
          
          <div className="flex items-center gap-4">
            <label className="flex items-center gap-2 cursor-pointer">
              <div
                onClick={() => setNormalize(!normalize)}
                className={`relative w-10 h-5 rounded-full transition-colors ${
                  normalize ? 'bg-cyan-500' : 'bg-neutral-200 hover:bg-neutral-300'
                }`}
              >
                <div
                  className={`absolute top-0.5 w-4 h-4 bg-white rounded-full shadow-sm transition-transform ${
                    normalize ? 'right-0.5' : 'left-0.5'
                  }`}
                ></div>
              </div>
              <span className="text-sm font-light text-neutral-600">Normalize by spend</span>
            </label>
            <label className="flex items-center gap-2 cursor-pointer">
              <div
                onClick={() => setCompare(!compare)}
                className={`relative w-10 h-5 rounded-full transition-colors ${
                  compare ? 'bg-cyan-500' : 'bg-neutral-200 hover:bg-neutral-300'
                }`}
              >
                <div
                  className={`absolute top-0.5 w-4 h-4 bg-white rounded-full shadow-sm transition-transform ${
                    compare ? 'right-0.5' : 'left-0.5'
                  }`}
                ></div>
              </div>
              <span className="text-sm font-light text-neutral-600">Compare vs last period</span>
            </label>
          </div>
        </div>
        
        {/* Chart Placeholder */}
        <div className="relative z-10 h-80 flex items-center justify-center bg-gradient-to-br from-cyan-50/20 to-transparent rounded-2xl border border-neutral-100">
          <p className="text-neutral-400 text-sm">Chart visualization (Chart.js integration needed)</p>
        </div>
      </div>
    </div>
  );
}

