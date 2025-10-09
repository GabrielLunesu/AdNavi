"use client";
import { useState } from "react";
import { ArrowRight, DollarSign, TrendingUp, Activity } from "lucide-react";
// import { Mic } from "lucide-react"; // Commented out for now

const suggestedQuestions = [
  { icon: DollarSign, text: "How much revenue last week?" },
  { icon: TrendingUp, text: "Show my conversions vs last week" },
  { icon: Activity, text: "What's my ROAS on Google last month?" },
];

export default function ChatConsole({ onSubmit, disabled }) {
  const [input, setInput] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!input.trim() || disabled) return;
    onSubmit(input.trim());
    setInput("");
  };

  const handleQuestionClick = (question) => {
    if (disabled) return;
    onSubmit(question);
  };

  return (
    <div className="fixed bottom-8 left-72 right-8 z-50 px-8">
      <div className="max-w-5xl mx-auto">
        {/* Suggested Questions */}
        <div className="flex items-center gap-3 mb-4 justify-center">
          {suggestedQuestions.map((q, idx) => {
            const Icon = q.icon;
            return (
              <button
                key={idx}
                onClick={() => handleQuestionClick(q.text)}
                disabled={disabled}
                className="px-5 py-2.5 rounded-full glass-card border border-neutral-200/60 text-neutral-700 text-sm font-medium hover:bg-white hover:border-cyan-400/40 transition-all flex items-center gap-2 disabled:opacity-50 disabled:cursor-not-allowed"
              >
                <Icon className="w-4 h-4" strokeWidth={1.5} />
                {q.text}
              </button>
            );
          })}
        </div>
        
        {/* Chat Input Console */}
        <form onSubmit={handleSubmit}>
          <div className="glass-console rounded-full border border-neutral-200/60 shadow-2xl px-6 py-4 flex items-center gap-4 relative overflow-hidden">
            <div className="absolute bottom-0 left-0 right-0 h-px bg-gradient-to-r from-transparent via-cyan-400 to-transparent opacity-40 pulse-glow"></div>
            
            {/* Mic icon commented out for now */}
            {/* <div className="w-10 h-10 rounded-full bg-gradient-to-br from-cyan-400 to-cyan-600 flex items-center justify-center flex-shrink-0 pulse-dot">
              <Mic className="w-5 h-5 text-white" strokeWidth={1.5} />
            </div> */}
            
            <input 
              type="text"
              value={input}
              onChange={(e) => setInput(e.target.value)}
              disabled={disabled}
              placeholder="Ask me anything about your marketing performance…" 
              className="flex-1 bg-transparent border-none outline-none text-base text-neutral-900 placeholder-neutral-400 disabled:opacity-50"
            />
            
            <button
              type="submit"
              disabled={disabled || !input.trim()}
              className="px-6 py-2.5 rounded-full bg-neutral-900 text-white text-sm font-medium hover:bg-neutral-800 transition-all shadow-lg hover:shadow-cyan-500/20 flex items-center gap-2 disabled:opacity-50 disabled:cursor-not-allowed"
            >
              Send
              <ArrowRight className="w-4 h-4" strokeWidth={1.5} />
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}

