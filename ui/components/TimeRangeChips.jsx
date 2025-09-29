// Functional time range selector
// WHY: Allows users to quickly switch between different time periods for analytics
export default function TimeRangeChips({ activeRange = '7d', onRangeChange }) {
  const chips = [
    { id: 'today', label: 'Today', days: 1 },
    { id: 'yesterday', label: 'Yesterday', days: 1, offset: 1 },
    { id: '7d', label: 'Last 7 days', days: 7 },
    { id: '30d', label: 'Last 30 days', days: 30 },
  ];
  
  const handleClick = (chip) => {
    if (onRangeChange) {
      onRangeChange(chip.id, chip.days, chip.offset);
    }
  };
  
  return (
    <div className="rounded-full p-1 border border-slate-800/60 bg-slate-900/40 inline-flex items-center gap-1">
      {chips.map((c) => (
        <button 
          key={c.id} 
          onClick={() => handleClick(c)}
          className={`px-3 py-1.5 rounded-full text-xs sm:text-sm transition-all ${
            activeRange === c.id 
              ? 'text-white bg-slate-800/60' 
              : 'text-slate-300 hover:text-white hover:bg-slate-800/40'
          }`}
        >
          {c.label}
        </button>
      ))}
    </div>
  );
}
