export default function OrbHeader() {
  return (
    <div className="relative px-4 pt-5">
      <div className="mx-auto w-16 h-16 rounded-full shadow-[0_0_40px_10px_rgba(56,189,248,0.25)] ring-1 ring-cyan-400/20 relative"
           style={{ background: 'radial-gradient(circle at 40% 40%, rgba(34,211,238,0.85) 0%, rgba(167,139,250,0.55) 40%, rgba(20,184,166,0.45) 70%, rgba(2,6,23,0) 72%)' }}>
        <span className="absolute inset-0 rounded-full border border-cyan-400/30 animate-ping" style={{ animationDelay: '1.5s' }} />
        {/* <span className="absolute inset-0 rounded-full border border-violet-400/30 animate-ping" style={{ animationDelay: '2.6s' }} />
        <span className="absolute inset-0 rounded-full border border-teal-400/30 animate-ping" style={{ animationDelay: '1.2s' }} /> */}
        <div className="absolute inset-2 rounded-full bg-gradient-to-br from-cyan-300/30 via-violet-300/20 to-teal-300/20 blur-md" />
      </div>
      <div className="mt-2 text-center text-[14px] text-bold text-slate-400">AdNavi Copilot</div>
    </div>
  );
}
