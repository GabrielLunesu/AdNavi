import { ChevronDown } from 'lucide-react';
import { sortOptions } from "../../data/campaigns/sorters";

export default function SortDropdown({ value='ROAS', onChange }) {
  return (
    <div className="relative">
      <button className="rounded-full px-3 py-1.5 text-sm border border-slate-600/40 bg-slate-900/35 flex items-center gap-2">
        <span>Sort by {value}</span>
        <ChevronDown size={16} className="text-slate-400" />
      </button>
    </div>
  );
}
