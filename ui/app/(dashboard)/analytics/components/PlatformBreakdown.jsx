const platforms = [
  { id: 'meta', name: 'Meta', amount: '$42,580', percentage: 58, color: 'bg-blue-500', initial: 'M' },
  { id: 'google', name: 'Google', amount: '$32,140', percentage: 44, color: 'bg-red-500', initial: 'G' },
  { id: 'tiktok', name: 'TikTok', amount: '$14,520', percentage: 20, color: 'bg-neutral-900', initial: 'T' },
];

export default function PlatformBreakdown() {
  return (
    <div className="glass-card rounded-3xl p-8 border border-neutral-200/60 shadow-lg card-hover">
      <h3 className="text-lg font-semibold text-neutral-900 mb-6">Platform Breakdown</h3>
      <div className="space-y-5">
        {platforms.map((platform) => (
          <div key={platform.id}>
            <div className="flex items-center justify-between mb-2">
              <div className="flex items-center gap-3">
                <div className={`w-8 h-8 rounded-xl ${platform.color} flex items-center justify-center`}>
                  <span className="text-white text-xs font-semibold">{platform.initial}</span>
                </div>
                <span className="text-sm font-medium text-neutral-900">{platform.name}</span>
              </div>
              <span className="text-sm font-semibold text-neutral-900">{platform.amount}</span>
            </div>
            <div className="w-full h-2 bg-neutral-100 rounded-full overflow-hidden">
              <div
                className="h-full bg-gradient-to-r from-cyan-400 to-cyan-500 rounded-full shadow-sm shadow-cyan-500/50"
                style={{ width: `${platform.percentage}%` }}
              ></div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

