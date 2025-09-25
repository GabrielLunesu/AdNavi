import { ChevronDown } from 'lucide-react';

const options = ['All','Meta Ads','Google Ads','TikTok Ads','LinkedIn Ads'];

export default function PlatformFilter({ value='All', onChange }) {
  return (
    <div className="relative">
      <button className="rounded-full px-3 py-1.5 text-sm border border-slate-600/40 bg-slate-900/35 flex items-center gap-2">
        <span>Platform: {value}</span>
        <ChevronDown size={16} className="text-slate-400" />
      </button>
      {/* Static menu omitted for brevity; use parent onChange with custom UI if desired */}
    </div>
  );
}
