/**
 * P&L Statement Table
 * 
 * WHAT: P&L statement table (read-only, displays all cost sources)
 * WHY: Line-item detail of all costs (ad spend + manual)
 * REFERENCES: lib/pnlAdapter.js:adaptPnLStatement
 */

"use client";

export default function PLTable({ rows, excludedRows = new Set(), onRowToggle }) {
  if (!rows || rows.length === 0) {
    return (
      <div className="glass-card rounded-3xl border border-black/5 shadow-xl mb-8 overflow-hidden p-8">
        <h2 className="text-2xl font-semibold text-black tracking-tight mb-6">Profit & Loss Statement</h2>
        <p className="text-neutral-400">No P&L data available for this period.</p>
      </div>
    );
  }

  // Compute totals from active rows only
  const activeRows = rows.filter(r => !excludedRows.has(r.id));
  const totalActual = activeRows.reduce((sum, r) => sum + (r.actualRaw || 0), 0);
  
  // Format totals
  const formatCurrency = (value) => {
    return new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' }).format(value);
  };

  return (
    <div className="glass-card rounded-3xl border border-black/5 shadow-xl mb-8 overflow-hidden fade-up-in" style={{ animationDelay: '400ms' }}>
      <div className="p-8">
        <h2 className="text-2xl font-semibold text-black tracking-tight mb-6">Profit & Loss Statement</h2>
        
        {/* Table */}
        <div className="overflow-x-auto">
          <table className="w-full">
            {/* Header */}
            <thead className="sticky top-0 bg-white/90 backdrop-blur-lg z-10">
              <tr className="border-b border-black/5">
                <th className="text-center py-4 px-4 text-xs font-semibold text-neutral-500 uppercase tracking-wide w-12">Active</th>
                <th className="text-left py-4 px-4 text-xs font-semibold text-neutral-500 uppercase tracking-wide">Category</th>
                <th className="text-right py-4 px-4 text-xs font-semibold text-neutral-500 uppercase tracking-wide">Actual ($)</th>
                <th className="text-left py-4 px-4 text-xs font-semibold text-neutral-500 uppercase tracking-wide">Notes</th>
              </tr>
            </thead>
            
            {/* Body */}
            <tbody>
              {rows.map((row, idx) => {
                const isLastRow = idx === rows.length - 1;
                
                const isExcluded = excludedRows.has(row.id);
                
                return (
                  <tr key={row.id} className={`${isLastRow ? 'border-b-2 border-black/10' : 'border-b border-black/5'} row-hover transition-all ${isExcluded ? 'opacity-50' : ''}`}>
                    <td className="text-center py-4 px-4">
                      <input
                        type="checkbox"
                        checked={!isExcluded}
                        onChange={() => onRowToggle?.(row.id)}
                        className="w-4 h-4 rounded border-neutral-300 text-cyan-600 focus:ring-cyan-500 cursor-pointer"
                      />
                    </td>
                    <td className="py-4 px-4">
                      <p className={`text-sm font-medium ${isExcluded ? 'line-through text-neutral-400' : 'text-black'}`}>{row.category}</p>
                      {row.isManual && (
                        <p className="text-xs text-neutral-400 mt-0.5">Manual Entry</p>
                      )}
                    </td>
                    <td className="text-right py-4 px-4">
                      <span className={`text-sm font-semibold ${isExcluded ? 'line-through text-neutral-400' : 'text-black'}`}>
                        {row.actual}
                      </span>
                    </td>
                    <td className="py-4 px-4 text-sm text-neutral-500">{row.notes}</td>
                  </tr>
                );
              })}

              {/* Total Row */}
              <tr className="bg-cyan-50/30 border-t-2 border-cyan-400/40">
                <td className="py-5 px-4"></td>
                <td className="py-5 px-4">
                  <p className="text-base font-bold text-black">Total Active Expenses</p>
                </td>
                <td className="text-right py-5 px-4 text-base font-bold text-black">
                  {formatCurrency(totalActual)}
                </td>
                <td className="py-5 px-4"></td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}

