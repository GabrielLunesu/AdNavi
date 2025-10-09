"use client";
import { Download } from "lucide-react";
import { useState } from "react";

export default function TopBar({ onPlatformChange, onTimeChange }) {
  const [selectedPlatform, setSelectedPlatform] = useState('all');
  const [selectedTime, setSelectedTime] = useState('30d');

  const platforms = [
    { id: 'all', label: 'All' },
    { id: 'meta', label: 'Meta' },
    { id: 'google', label: 'Google' },
    { id: 'tiktok', label: 'TikTok' },
  ];

  const timeRanges = [
    { id: '7d', label: '7d' },
    { id: '30d', label: '30d' },
    { id: 'custom', label: 'Custom' },
  ];

  const handlePlatformClick = (id) => {
    setSelectedPlatform(id);
    onPlatformChange?.(id);
  };

  const handleTimeClick = (id) => {
    setSelectedTime(id);
    onTimeChange?.(id);
  };

  return (
    <div className="sticky top-4 z-40 mb-8 mx-8">
      <div className="glass-card rounded-3xl border border-neutral-200/60 shadow-lg px-8 py-5 flex items-center justify-between">
        <h2 className="text-4xl font-semibold tracking-tight text-neutral-900">Analytics</h2>
        
        <div className="flex items-center gap-4">
          {/* Platform Filters */}
          <div className="flex items-center gap-2">
            {platforms.map((platform) => (
              <button
                key={platform.id}
                onClick={() => handlePlatformClick(platform.id)}
                className={`px-4 py-2 rounded-full text-sm font-medium transition-all ${
                  selectedPlatform === platform.id
                    ? 'bg-cyan-500 text-white shadow-sm shadow-cyan-500/30'
                    : 'bg-white/60 border border-neutral-200/60 text-neutral-700 hover:bg-white hover:border-cyan-400/40'
                }`}
              >
                {platform.label}
              </button>
            ))}
          </div>
          
          <div className="w-px h-6 bg-neutral-200"></div>
          
          {/* Time Filters */}
          <div className="flex items-center gap-2">
            {timeRanges.map((range) => (
              <button
                key={range.id}
                onClick={() => handleTimeClick(range.id)}
                className={`px-4 py-2 rounded-full text-sm font-medium transition-all ${
                  selectedTime === range.id
                    ? 'bg-cyan-500 text-white shadow-sm shadow-cyan-500/30'
                    : 'bg-white/60 border border-neutral-200/60 text-neutral-700 hover:bg-white hover:border-cyan-400/40'
                }`}
              >
                {range.label}
              </button>
            ))}
          </div>
          
          <div className="w-px h-6 bg-neutral-200"></div>
          
          {/* Export Button */}
          <button className="px-5 py-2 rounded-full bg-neutral-900 text-white text-sm font-medium transition-all hover:bg-neutral-800 flex items-center gap-2">
            <Download className="w-4 h-4" strokeWidth={1.5} />
            Export
          </button>
        </div>
      </div>
    </div>
  );
}

