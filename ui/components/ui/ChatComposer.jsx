"use client";
import { useEffect, useMemo, useRef, useState } from "react";
import { ArrowUpRight, Mic, Plus, Sparkles } from "lucide-react";

// WHY: Dedicated inline composer for the Copilot page. Keeps the page clean and
// lets us reuse this input in other contexts later without navigation.
export default function ChatComposer({
  onSubmit,
  disabled = false,
  placeholderRotations = [
    "Ask me about your revenue today…",
    "Why did ROAS change last week?",
    "Show me my top converting ad set.",
    "What’s my profit after costs?",
  ],
}) {
  const [value, setValue] = useState("");
  const [idx, setIdx] = useState(0);
  const inputRef = useRef(null);

  // Subtle rotating placeholder to guide users toward useful prompts
  useEffect(() => {
    const id = setInterval(() => {
      setIdx((i) => (i + 1) % placeholderRotations.length);
    }, 3500);
    return () => clearInterval(id);
  }, [placeholderRotations.length]);

  const placeholder = placeholderRotations[idx];

  const handleSubmit = (e) => {
    e.preventDefault();
    const q = value.trim();
    if (!q || disabled) return;
    onSubmit?.(q);
    setValue("");
    inputRef.current?.focus();
  };

  return (
    <form onSubmit={handleSubmit} className="w-full">
      <div className="flex items-center gap-2">
        <div className="flex-1 rounded-full border border-slate-700/40 bg-slate-900/40 backdrop-blur px-3 py-2.5 flex items-center gap-2 ring-1 ring-white/5 focus-within:ring-cyan-400/30 transition">
          <Sparkles className="w-4 h-4 text-cyan-300" />
          <input
            ref={inputRef}
            type="text"
            value={value}
            onChange={(e) => setValue(e.target.value)}
            placeholder={placeholder}
            className="w-full bg-transparent outline-none text-sm placeholder-slate-500 text-slate-200"
            disabled={disabled}
          />
          <div className="flex items-center gap-1">
            <button type="button" className="p-1.5 rounded-full hover:bg-slate-800/60 border border-transparent hover:border-slate-700/50 transition" aria-label="Attach" disabled={disabled}>
              <Plus className="w-4 h-4 text-slate-300" />
            </button>
            <button type="button" className="p-1.5 rounded-full hover:bg-slate-800/60 border border-transparent hover:border-slate-700/50 transition" aria-label="Voice" disabled={disabled}>
              <Mic className="w-4 h-4 text-slate-300" />
            </button>
            <button type="submit" className="p-1.5 rounded-full bg-cyan-500/20 hover:bg-cyan-500/30 ring-1 ring-cyan-400/40 transition disabled:opacity-60" aria-label="Send" disabled={disabled || !value.trim()}>
              <ArrowUpRight className="w-4 h-4 text-cyan-300" />
            </button>
          </div>
        </div>
      </div>
    </form>
  );
}


