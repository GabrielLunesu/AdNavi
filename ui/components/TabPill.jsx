import { cn } from "../lib/cn";

export default function TabPill({ active, children, className, ...props }) {
  return (
    <button
      className={cn(
        "px-3 py-1.5 text-sm rounded-full",
        active ? "bg-slate-800/60" : "hover:bg-slate-800/40",
        className
      )}
      {...props}
    >
      {children}
    </button>
  );
}
