export default function SnapshotHeader() {
  return (
    <div className="mb-12 fade-up">
      <div className="flex items-start justify-between mb-8">
        <h2 className="text-5xl font-semibold tracking-tight text-neutral-900 leading-tight">
          Here's a quick snapshot<br/>of your performance.
        </h2>
        
        {/* Context Synced Indicator */}
        <div className="flex items-center gap-2 px-4 py-2 rounded-full bg-white/60 border border-cyan-400/30">
          <div className="w-2 h-2 rounded-full bg-cyan-400 pulse-dot"></div>
          <span className="text-sm font-medium text-neutral-700">Context synced</span>
        </div>
      </div>
      
      {/* Key Stats Row */}
      <div className="grid grid-cols-2 gap-6 mb-8 fade-up fade-up-delay-1">
        {/* Revenue Today */}
        <div className="glass-card rounded-3xl p-8 border border-neutral-200/60 cyan-glow-card relative overflow-hidden">
          <div className="glow-line"></div>
          <p className="text-sm font-medium text-neutral-500 mb-2 uppercase tracking-wide">Revenue Today</p>
          <p className="text-5xl font-semibold text-neutral-900 mb-1">$12,847</p>
          <span className="inline-block px-3 py-1 rounded-full bg-green-50 text-green-600 text-sm font-medium">+24.3% vs yesterday</span>
          <div className="absolute -right-10 -bottom-10 w-32 h-32 bg-cyan-400 rounded-full blur-[60px] opacity-10 pulse-glow"></div>
        </div>
        
        {/* ROAS Yesterday */}
        <div className="glass-card rounded-3xl p-8 border border-neutral-200/60 cyan-glow-card relative overflow-hidden">
          <div className="glow-line" style={{ animationDelay: '1s' }}></div>
          <p className="text-sm font-medium text-neutral-500 mb-2 uppercase tracking-wide">ROAS Yesterday</p>
          <p className="text-5xl font-semibold text-neutral-900 mb-1">4.32x</p>
          <span className="inline-block px-3 py-1 rounded-full bg-green-50 text-green-600 text-sm font-medium">+0.8x improvement</span>
          <div className="absolute -right-10 -bottom-10 w-32 h-32 bg-cyan-400 rounded-full blur-[60px] opacity-10 pulse-glow" style={{ animationDelay: '1.5s' }}></div>
        </div>
      </div>
      
      {/* Summary Box */}
      <div className="glass-card rounded-3xl p-8 border border-neutral-200/60 relative overflow-hidden fade-up fade-up-delay-2">
        <div className="absolute inset-0 shimmer-bg"></div>
        <h3 className="text-lg font-semibold text-neutral-900 mb-4 relative z-10">Summary</h3>
        <p className="text-base text-neutral-700 leading-relaxed mb-3 relative z-10">
          Revenue is trending up, driven by stable CPC and higher AOV from new bundle ads.
        </p>
        <p className="text-base text-neutral-700 leading-relaxed relative z-10">
          Your top-performing segment: <span className="font-medium text-cyan-600">Meta LAL 2%</span> (CTR <span className="font-medium text-cyan-600">+6%</span>)
        </p>
        <div className="mt-6 h-px bg-gradient-to-r from-cyan-400 via-cyan-300 to-transparent relative z-10"></div>
      </div>
    </div>
  );
}

