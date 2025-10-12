import TrendSparkline from "./TrendSparkline";

export default function EntityRow({ row, onClick }) {
  const display = row.display || {};
  const hasChildren = row.level !== 'ad'; // Ads are leaf nodes
  
  return (
    <div className="flex items-stretch px-6 py-4 text-sm group hover:bg-gradient-to-r hover:from-white/[0.08] hover:via-white/[0.05] hover:to-transparent transition-all duration-300 border-b border-slate-900/10 hover:border-slate-900/15 relative overflow-hidden">
      {/* Glossy shine effect on hover */}
      <div className="absolute inset-0 bg-gradient-to-r from-transparent via-white/[0.03] to-transparent translate-x-[-100%] group-hover:translate-x-[100%] transition-transform duration-700 pointer-events-none"></div>
      
      <div className="w-[300px] flex flex-col gap-1 relative z-10 px-4 border-r border-slate-900/20">
        <span className="text-slate-900 font-semibold tracking-wide group-hover:text-black transition-colors duration-300">{row.name}</span>
        <span className="text-xs text-slate-600 group-hover:text-slate-700 transition-colors duration-300">{display.subtitle}</span>
      </div>
      <CellText value={display.revenue} width="w-[120px]" hasBorder />
      <CellText value={display.spend} width="w-[120px]" hasBorder />
      <CellText value={display.roas} width="w-[100px]" hasBorder />
      <CellText value={display.conversions} width="w-[130px]" hasBorder />
      <CellText value={display.cpc} width="w-[100px]" hasBorder />
      <CellText value={display.ctr} width="w-[100px]" hasBorder />
      <div className="w-[120px] relative z-10 px-4 border-r border-slate-900/20 flex items-center">
        <span className={`text-xs px-3 py-1.5 rounded-full font-medium backdrop-blur-sm transition-all duration-300 inline-block ${
          row.status === 'active'
            ? 'bg-emerald-400/15 text-emerald-700 border border-emerald-400/30 shadow-[0_0_12px_rgba(52,211,153,0.15)] group-hover:shadow-[0_0_20px_rgba(52,211,153,0.25)] group-hover:border-emerald-400/50'
            : 'bg-amber-400/15 text-amber-700 border border-amber-400/30 shadow-[0_0_12px_rgba(251,191,36,0.15)] group-hover:shadow-[0_0_20px_rgba(251,191,36,0.25)] group-hover:border-amber-400/50'
        }`}>
          {row.status}
        </span>
      </div>
      <div className="w-[120px] relative z-10 px-4 border-r border-slate-900/20 flex items-center"><TrendSparkline data={row.trend?.map(point => point.value ?? 0) || []} /></div>
      <div className="flex-1 relative z-10 px-4 flex items-center">
        {hasChildren && onClick ? (
          <button 
            onClick={() => onClick(row.id)}
            className="px-4 py-2 text-xs font-semibold rounded-full border border-slate-300/60 bg-white/40 backdrop-blur-md hover:bg-white/60 hover:border-cyan-400/60 hover:shadow-[0_0_20px_rgba(34,211,238,0.2)] hover:scale-105 transition-all duration-300 cursor-pointer text-slate-900"
          >
            View
          </button>
        ) : (
          <span className="px-4 py-2 text-xs text-slate-400">—</span>
        )}
      </div>
    </div>
  );
}

function CellText({ value, width, hasBorder = false }) {
  return (
    <div className={`${width} tabular-nums font-medium text-slate-800 group-hover:text-black transition-colors duration-300 relative z-10 flex items-center ${hasBorder ? 'px-4 border-r border-slate-900/20' : 'px-4'}`}>
      {value ?? '—'}
    </div>
  );
}
