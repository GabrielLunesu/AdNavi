// WHAT: Legends for statuses/metrics
// WHY: Provide quick context for colors/symbols used on the canvas
// REFERENCES: docs/canvas/01-functional-spec.md

import React from "react";

export default function Legends() {
  const items = [
    { color: "bg-green-500", label: "Active" },
    { color: "bg-amber-500", label: "Paused" },
    { color: "bg-neutral-400", label: "Unknown" },
  ];
  return (
    <div className="flex items-center gap-3 text-xs text-neutral-600">
      {items.map((i) => (
        <span key={i.label} className="flex items-center gap-2">
          <span className={`w-2 h-2 rounded-full ${i.color}`}></span>
          {i.label}
        </span>
      ))}
    </div>
  );
}

