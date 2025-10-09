"use client";
import { useState } from "react";
import { TrendingUp, Lightbulb, Target } from 'lucide-react';

export default function AssistantSection({ workspaceId }) {
  const [selectedRange, setSelectedRange] = useState('30d');

  const quickActions = [
    { icon: TrendingUp, text: "Show me what's working" },
    { icon: Lightbulb, text: "Suggest my next campaign" },
    { icon: Target, text: "Improve my budget efficiency" },
  ];

  const timeRanges = [
    { id: 'today', label: 'Today' },
    { id: '7d', label: '7d' },
    { id: '30d', label: '30d' },
    { id: 'custom', label: 'Custom' },
  ];

  return (
    <div className="mb-12">
      <div className="flex items-start justify-between mb-8">
        <div>
          <h2 className="text-5xl font-semibold tracking-tight mb-4 gradient-text">
            Hi there. What can I help you achieve today?
          </h2>
          <div className="flex items-center gap-3 mt-6">
            {quickActions.map((action, idx) => {
              const Icon = action.icon;
              return (
                <button
                  key={idx}
                  className="px-5 py-3 rounded-full bg-white/80 backdrop-blur-xl border border-neutral-200/60 hover:border-cyan-400/60 text-sm font-medium text-neutral-900 shadow-sm hover:shadow-md hover:shadow-cyan-500/10 transition-all flex items-center gap-2"
                >
                  <Icon className="w-4 h-4" strokeWidth={1.5} />
                  {action.text}
                </button>
              );
            })}
          </div>
        </div>
        <div className="flex items-center gap-2 glass-card px-4 py-2 rounded-full border border-neutral-200/60 shadow-sm">
          {timeRanges.map((range) => (
            <button
              key={range.id}
              onClick={() => setSelectedRange(range.id)}
              className={`px-3 py-1.5 text-xs font-medium transition-colors ${
                selectedRange === range.id
                  ? 'bg-cyan-500 text-white rounded-full'
                  : 'text-neutral-600 hover:text-neutral-900'
              }`}
            >
              {range.label}
            </button>
          ))}
        </div>
      </div>
    </div>
  );
}

