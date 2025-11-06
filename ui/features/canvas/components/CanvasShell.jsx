// WHAT: Canvas feature frame (toolbar + left/right sidebars + main viewport slot)
// WHY: Provide a consistent layout shell without coupling to routing
// REFERENCES: docs/canvas/01-functional-spec.md, ui/app/globals.css

import React, { cloneElement } from "react";

export default function CanvasShell({
  toolbar,
  leftSidebar,
  rightSidebar,
  showLeftSidebar = true,
  showRightSidebar = true,
  immersive = false,
  children,
}) {
  const leftContent = leftSidebar ? cloneElement(leftSidebar, { key: "left" }) : null;
  const rightContent = rightSidebar ? cloneElement(rightSidebar, { key: "right" }) : null;

  return (
    <div
      className={`relative flex flex-col bg-[#F9FAFB] antialiased ${
        immersive ? "min-h-screen" : "rounded-3xl min-h-[720px]"
      } p-0 overflow-hidden`}
    >
      {/* Decorative aura background */}
      <div className="pointer-events-none absolute inset-0 overflow-hidden" aria-hidden>
        <div className="absolute top-[-20%] left-[-10%] w-[720px] h-[720px] bg-[#B9C7F5] rounded-full blur-[200px] opacity-10"></div>
        <div className="absolute bottom-[-30%] right-[-10%] w-[780px] h-[780px] bg-[#A5B4FC] rounded-full blur-[220px] opacity-10"></div>
      </div>

      <div className="relative z-10 flex flex-col h-full">
        {/* Toolbar */}
        <div className="sticky top-0 z-20">
          <div className="glass-card border-b border-neutral-200/40 px-6 py-4 flex items-center justify-between gap-4">
            {toolbar}
          </div>
        </div>

        {/* Content area (viewport full), panels overlay on top */}
        <div className="relative flex-1 min-h-0 px-6 pb-6 pt-4">
          {/* Viewport */}
          <section className="relative w-full h-full">{children}</section>

          {/* Overlays */}
          {showLeftSidebar && leftContent && (
            <div className="pointer-events-auto absolute left-6 top-6 w-72 max-h-[80vh] overflow-hidden bg-white rounded-3xl border border-neutral-200 shadow-xl p-5 hidden md:block z-50">
              {leftContent}
              {typeof toolbar?.props?.onToggleFilters === 'function' && (
                <button
                  onClick={toolbar.props.onToggleFilters}
                  aria-label="Close filters"
                  className="absolute top-3 right-3 w-6 h-6 rounded-full border border-neutral-200 text-neutral-500 hover:text-neutral-700"
                >×</button>
              )}
            </div>
          )}
          {showRightSidebar && rightContent && (
            <div className="pointer-events-auto absolute right-6 top-6 w-96 max-h-[80vh] overflow-hidden bg-white rounded-3xl border border-neutral-200 shadow-xl p-0 hidden md:flex flex-col z-50">
              {rightContent}
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
