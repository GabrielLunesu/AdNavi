"use client";
import { useState } from "react";
import { useRouter } from "next/navigation";
import { TrendingUp, Lightbulb, Target, Send } from 'lucide-react';

export default function AssistantSection({ workspaceId }) {
  const [inputValue, setInputValue] = useState("");
  const router = useRouter();

  const quickActions = [
    { icon: TrendingUp, text: "Show me what's working" },
    { icon: Lightbulb, text: "Suggest my next campaign" },
    { icon: Target, text: "Improve my budget efficiency" },
  ];

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!inputValue.trim()) return;
    router.push(`/copilot?q=${encodeURIComponent(inputValue.trim())}&ws=${workspaceId}`);
  };

  const handleQuickAction = (text) => {
    router.push(`/copilot?q=${encodeURIComponent(text)}&ws=${workspaceId}`);
  };

  return (
    <div className="mb-12">
      {/* Header */}
      <div className="mb-8">
        <h2 className="text-5xl font-semibold tracking-tight gradient-text text-center">
          Hi there. What can I help you achieve today?
        </h2>
      </div>

      {/* Chat Input */}
      <div className="max-w-3xl mx-auto mb-6">
        <form onSubmit={handleSubmit}>
          <div className="glass-card rounded-full border border-neutral-200/60 shadow-lg px-6 py-4 flex items-center gap-3">
            <input
              type="text"
              value={inputValue}
              onChange={(e) => setInputValue(e.target.value)}
              placeholder="Ask me anything about your campaigns..."
              className="flex-1 bg-transparent outline-none text-neutral-900 placeholder:text-neutral-400"
            />
            <button
              type="submit"
              className="w-10 h-10 rounded-full bg-cyan-500 hover:bg-cyan-600 text-white flex items-center justify-center transition-colors"
            >
              <Send className="w-4 h-4" strokeWidth={1.5} />
            </button>
          </div>
        </form>
      </div>

      {/* Quick Actions */}
      <div className="flex items-center justify-center gap-3">
        {quickActions.map((action, idx) => {
          const Icon = action.icon;
          return (
            <button
              key={idx}
              onClick={() => handleQuickAction(action.text)}
              className="px-5 py-3 rounded-full bg-white/80 backdrop-blur-xl border border-neutral-200/60 hover:border-cyan-400/60 text-sm font-medium text-neutral-900 shadow-sm hover:shadow-md hover:shadow-cyan-500/10 transition-all flex items-center gap-2"
            >
              <Icon className="w-4 h-4" strokeWidth={1.5} />
              {action.text}
            </button>
          );
        })}
      </div>
    </div>
  );
}

