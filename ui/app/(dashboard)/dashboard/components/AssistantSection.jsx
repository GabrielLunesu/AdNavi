"use client";
import { useState } from "react";
import { useRouter } from "next/navigation";
import { TrendingUp, Lightbulb, Target, Send } from 'lucide-react';

export default function AssistantSection({ workspaceId }) {
  const [inputValue, setInputValue] = useState("");
  const [isTransitioning, setIsTransitioning] = useState(false);
  const router = useRouter();

  const quickActions = [
    { icon: TrendingUp, text: "Show me what's working" },
    { icon: Lightbulb, text: "Suggest my next campaign" },
    { icon: Target, text: "Improve my budget efficiency" },
  ];

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!inputValue.trim() || isTransitioning) return;
    
    // Trigger exit animation
    setIsTransitioning(true);
    
    // Navigate after animation completes
    setTimeout(() => {
      router.push(`/copilot?q=${encodeURIComponent(inputValue.trim())}&ws=${workspaceId}`);
    }, 300); // Match animation duration
  };

  const handleQuickAction = (text) => {
    // Trigger exit animation
    setIsTransitioning(true);
    
    // Navigate after animation completes
    setTimeout(() => {
      router.push(`/copilot?q=${encodeURIComponent(text)}&ws=${workspaceId}`);
    }, 300);
  };

  return (
    <div className={`mb-12 ${isTransitioning ? 'chat-exit' : ''}`}>
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
              disabled={isTransitioning}
            />
            <button
              type="submit"
              disabled={isTransitioning}
              className="w-10 h-10 rounded-full bg-cyan-500 hover:bg-cyan-600 text-white flex items-center justify-center transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
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
              disabled={isTransitioning}
              className="px-5 py-3 rounded-full bg-white/80 backdrop-blur-xl border border-neutral-200/60 hover:border-cyan-400/60 text-sm font-medium text-neutral-900 shadow-sm hover:shadow-md hover:shadow-cyan-500/10 transition-all flex items-center gap-2 disabled:opacity-50 disabled:cursor-not-allowed"
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

