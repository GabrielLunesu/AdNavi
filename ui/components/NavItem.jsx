// Navigation item used in the sidebar
// Props: href, label, icon (React node), active (bool)
import Link from "next/link";
import { cn } from "../lib/cn";

export default function NavItem({ href, label, icon, active }) {
  return (
    <Link
      href={href}
      className={cn(
        "flex items-center gap-3 px-3 py-2 rounded-lg text-sm transition-colors",
        active
          ? "bg-slate-800/60 text-white"
          : "text-slate-400 hover:text-white hover:bg-slate-800/40"
      )}
      aria-current={active ? "page" : undefined}
    >
      <span className="shrink-0">{icon}</span>
      <span>{label}</span>
    </Link>
  );
}
