import { Layers, Target, ChevronDown, SwitchCamera, Download, Save } from 'lucide-react';
import PillButton from "../../components/PillButton";

export default function AnalyticsControls({ platform = 'Meta Ads', campaign = 'Prospecting — Lookalike 2%' }) {
  return (
    <div className="flex flex-col gap-4 lg:flex-row lg:items-center lg:justify-between mb-6">
      {/* Left selectors */}
      <div className="flex flex-col md:flex-row md:items-center gap-3">
        <div className="rounded-full px-3 py-2 border border-slate-600/40 bg-slate-900/35">
          <div className="flex items-center gap-2">
            <Layers size={16} className="text-cyan-300" aria-hidden />
            <button className="text-sm text-white/90 hover:text-white flex items-center gap-2">
              <span>{platform}</span>
              <ChevronDown size={16} className="text-slate-400" aria-hidden />
            </button>
          </div>
        </div>
        <div className="rounded-full px-3 py-2 border border-slate-600/40 bg-slate-900/35">
          <div className="flex items-center gap-2">
            <Target size={16} className="text-violet-300" aria-hidden />
            <button className="text-sm text-white/90 hover:text-white flex items-center gap-2">
              <span>{campaign}</span>
              <ChevronDown size={16} className="text-slate-400" aria-hidden />
            </button>
          </div>
        </div>
      </div>
      {/* Right actions */}
      <div className="flex items-center gap-3">
        <div className="flex items-center gap-1 rounded-full px-1.5 py-1 border border-slate-600/40 bg-slate-900/35">
          <TabBtn>Today</TabBtn>
          <TabBtn active>7d</TabBtn>
          <TabBtn>30d</TabBtn>
          <TabBtn>Custom</TabBtn>
        </div>
        <PillButton title="Toggle vs last period"><SwitchCamera size={16} className="text-cyan-300" /> <span className="ml-1">vs last period</span></PillButton>
        <div className="w-px h-6 bg-white/10" />
        <PillButton><Download size={16} /> <span className="ml-1">Export</span></PillButton>
        <button className="rounded-full px-3 py-1.5 text-sm flex items-center gap-2 bg-gradient-to-r from-teal-500/80 to-cyan-500/80 hover:from-teal-500 hover:to-cyan-500 shadow-[0_0_20px_rgba(34,211,238,0.25)]">
          <Save size={16} /> <span>Save Report</span>
        </button>
      </div>
    </div>
  );
}

function TabBtn({ active, children }) {
  return (
    <button className={`px-3 py-1.5 text-sm rounded-full ${active ? 'bg-slate-800/60' : 'hover:bg-slate-800/40'}`}>{children}</button>
  );
}
