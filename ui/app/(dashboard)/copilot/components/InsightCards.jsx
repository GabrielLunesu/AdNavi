import { TrendingUp, Image as ImageIcon, BarChart2, Lightbulb } from "lucide-react";

function MetricBadge({ children }) {
  return (
    <span className="metric-badge px-2 py-1 rounded-lg font-medium text-cyan-600">
      {children}
    </span>
  );
}

export default function InsightCards() {
  return (
    <div className="space-y-6 mb-12">
      {/* Performance Insight */}
      <div className="glass-card rounded-3xl p-8 border border-neutral-200/60 cyan-glow-card relative overflow-hidden fade-up fade-up-delay-3">
        <div className="flex items-start gap-6">
          <div className="w-12 h-12 rounded-2xl bg-gradient-to-br from-cyan-400 to-cyan-600 flex items-center justify-center flex-shrink-0 shadow-lg shadow-cyan-500/30">
            <TrendingUp className="w-6 h-6 text-white" strokeWidth={1.5} />
          </div>
          <div className="flex-1">
            <h4 className="text-xl font-semibold text-neutral-900 mb-3">Performance Insight</h4>
            <p className="text-base text-neutral-700 leading-relaxed mb-4">
              Spend <MetricBadge>↓ 4.2%</MetricBadge> while ROAS <MetricBadge>↑ 9.1%</MetricBadge> — efficiency improved this week.
            </p>
            <div className="w-full h-32 bg-white/40 rounded-2xl p-4 border border-neutral-200/40 flex items-center justify-center">
              <p className="text-neutral-400 text-sm">Chart visualization</p>
            </div>
          </div>
        </div>
        <div className="absolute -right-20 -bottom-20 w-40 h-40 bg-cyan-400 rounded-full blur-[80px] opacity-10"></div>
      </div>

      {/* Creative Insight */}
      <div className="glass-card rounded-3xl p-8 border border-neutral-200/60 cyan-glow-card relative overflow-hidden fade-up fade-up-delay-4">
        <div className="flex items-start gap-6">
          <div className="w-12 h-12 rounded-2xl bg-gradient-to-br from-cyan-400 to-cyan-600 flex items-center justify-center flex-shrink-0 shadow-lg shadow-cyan-500/30">
            <ImageIcon className="w-6 h-6 text-white" strokeWidth={1.5} />
          </div>
          <div className="flex-1">
            <h4 className="text-xl font-semibold text-neutral-900 mb-3">Creative Insight</h4>
            <div className="flex items-center gap-4 mb-4">
              <div className="w-20 h-20 rounded-xl bg-gradient-to-br from-neutral-800 to-red-600 flex items-center justify-center text-white text-2xl font-bold">
                N
              </div>
              <div className="flex-1">
                <p className="text-base text-neutral-700 leading-relaxed">
                  This creative generated <MetricBadge>31% more conversions</MetricBadge> than average.
                </p>
                <p className="text-sm text-neutral-500 mt-1">Video: Product Demo v3 • Meta Feed</p>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Platform Comparison */}
      <div className="glass-card rounded-3xl p-8 border border-neutral-200/60 cyan-glow-card relative overflow-hidden fade-up fade-up-delay-5">
        <div className="flex items-start gap-6">
          <div className="w-12 h-12 rounded-2xl bg-gradient-to-br from-cyan-400 to-cyan-600 flex items-center justify-center flex-shrink-0 shadow-lg shadow-cyan-500/30">
            <BarChart2 className="w-6 h-6 text-white" strokeWidth={1.5} />
          </div>
          <div className="flex-1">
            <h4 className="text-xl font-semibold text-neutral-900 mb-4">Platform Comparison</h4>
            <div className="space-y-4">
              {[
                { name: 'Meta', roas: '4.8x', width: 96 },
                { name: 'Google', roas: '3.9x', width: 78 },
                { name: 'TikTok', roas: '3.2x', width: 64 },
              ].map((platform) => (
                <div key={platform.name}>
                  <div className="flex items-center justify-between mb-2">
                    <span className="text-sm font-medium text-neutral-700">{platform.name}</span>
                    <span className="text-sm font-semibold text-neutral-900">ROAS {platform.roas}</span>
                  </div>
                  <div className="w-full h-3 bg-neutral-100 rounded-full overflow-hidden">
                    <div
                      className="h-full bg-gradient-to-r from-cyan-400 to-cyan-500 rounded-full"
                      style={{ width: `${platform.width}%` }}
                    ></div>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>

      {/* Recommendation */}
      <div className="glass-card rounded-3xl p-8 border border-cyan-300/40 cyan-glow-card relative overflow-hidden fade-up fade-up-delay-6">
        <div className="absolute inset-0 bg-gradient-to-br from-cyan-50/40 via-transparent to-transparent"></div>
        <div className="flex items-start gap-6 relative z-10">
          <div className="w-12 h-12 rounded-2xl bg-gradient-to-br from-cyan-400 to-cyan-600 flex items-center justify-center flex-shrink-0 shadow-lg shadow-cyan-500/30">
            <Lightbulb className="w-6 h-6 text-white" strokeWidth={1.5} />
          </div>
          <div className="flex-1">
            <h4 className="text-xl font-semibold text-neutral-900 mb-3">Recommendation</h4>
            <p className="text-base text-neutral-700 leading-relaxed mb-4">
              Shift <MetricBadge>10–15% budget</MetricBadge> from low-ROAS ad sets to <span className="font-medium text-cyan-600">Meta lookalike 2%</span>.
            </p>
            <div className="flex items-center gap-3">
              <button className="px-5 py-2.5 rounded-full bg-cyan-500 text-white text-sm font-medium shadow-lg shadow-cyan-500/30 hover:bg-cyan-600 transition-all">
                Apply change
              </button>
              <button className="px-5 py-2.5 rounded-full bg-white/60 border border-neutral-200/60 text-neutral-700 text-sm font-medium hover:bg-white hover:border-cyan-400/40 transition-all">
                Simulate impact
              </button>
            </div>
          </div>
        </div>
        <div className="absolute -right-16 -bottom-16 w-32 h-32 bg-cyan-400 rounded-full blur-[70px] opacity-20 pulse-glow"></div>
      </div>
    </div>
  );
}

