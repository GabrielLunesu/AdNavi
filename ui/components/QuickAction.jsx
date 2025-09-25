// Reusable quick action pill button (non-functional)
export default function QuickAction({ label }) {
  return (
    <button className="rounded-full border border-slate-800/60 px-3 py-1.5 text-xs text-slate-300 hover:text-white hover:bg-slate-800/40">
      {label}
    </button>
  );
}
