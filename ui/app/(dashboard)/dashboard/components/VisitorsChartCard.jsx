export default function VisitorsChartCard() {
  const daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'];
  const barHeights = ['45%', '60%', '52%', '75%', '85%', '100%', '68%'];

  return (
    <div className="glass-card rounded-3xl p-8 border border-neutral-200/60 shadow-lg">
      <h3 className="text-xl font-semibold text-neutral-900 mb-6">Website Visitors</h3>
      <div className="h-48 flex items-end justify-between gap-2">
        {barHeights.map((height, idx) => (
          <div
            key={idx}
            className={`flex-1 bg-gradient-to-t from-cyan-400 to-cyan-200 rounded-t-lg ${
              idx === 5 ? 'opacity-100' : 'opacity-60'
            }`}
            style={{ height }}
          ></div>
        ))}
      </div>
      <div className="mt-4 flex items-center justify-between text-xs text-neutral-500">
        {daysOfWeek.map((day) => (
          <span key={day}>{day}</span>
        ))}
      </div>
      <div className="mt-6 flex items-center gap-4">
        <div className="flex items-center gap-2">
          <div className="w-3 h-3 rounded-full bg-cyan-400"></div>
          <span className="text-xs text-neutral-600">Visitors: 12,458</span>
        </div>
        <div className="flex items-center gap-2">
          <div className="w-3 h-3 rounded-full bg-cyan-600"></div>
          <span className="text-xs text-neutral-600">Conversions: 1,294</span>
        </div>
      </div>
    </div>
  );
}

