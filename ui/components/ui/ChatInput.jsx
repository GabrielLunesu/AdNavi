"use client";
import { useState } from "react";
import { useRouter } from "next/navigation";

// WHY: Dumb input that redirects to /copilot with question as query param.
// The Copilot page itself will handle the API call.

export default function ChatInput({ workspaceId }) {
  const [val, setVal] = useState("");
  const router = useRouter();

  const handleSubmit = (e) => {
    e.preventDefault();
    const question = val.trim();
    if (!question) return;
    router.push(`/copilot?q=${encodeURIComponent(question)}&ws=${workspaceId}`);
  };

  return (
    <form onSubmit={handleSubmit} className="flex items-center gap-2 w-full">
      <input
        type="text"
        value={val}
        onChange={(e) => setVal(e.target.value)}
        placeholder="Ask anything about your marketing data…"
        className="flex-1 rounded-lg bg-neutral-900 border border-neutral-700 px-4 py-2 text-sm focus:outline-none focus:ring-1 focus:ring-emerald-500"
      />
      <button
        type="submit"
        className="px-4 py-2 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white text-sm"
      >
        Ask
      </button>
    </form>
  );
}


