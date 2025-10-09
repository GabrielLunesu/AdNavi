"use client";

const expenses = [
  {
    category: 'Ad Spend – Google',
    subtitle: 'Search & Display',
    planned: 4200,
    actual: 3847,
    variance: -8.4,
    notes: 'Lower CPC, better quality',
  },
  {
    category: 'Ad Spend – Meta',
    subtitle: 'Facebook & Instagram',
    planned: 3500,
    actual: 3926,
    variance: 12.2,
    notes: 'Testing new creatives',
  },
  {
    category: 'Tools / SaaS',
    subtitle: 'Analytics & Automation',
    planned: 800,
    actual: 842,
    variance: 5.3,
    notes: 'Added new tool',
  },
  {
    category: 'Agency Fees',
    subtitle: 'Management & Strategy',
    planned: 1200,
    actual: 1200,
    variance: 0,
    notes: 'As planned',
  },
  {
    category: 'Miscellaneous',
    subtitle: 'Other costs',
    planned: 400,
    actual: 285,
    variance: -28.8,
    notes: 'Reduced overhead',
  },
];

export default function PLTable() {
  const totalPlanned = expenses.reduce((sum, e) => sum + e.planned, 0);
  const totalActual = expenses.reduce((sum, e) => sum + e.actual, 0);
  const totalVariance = ((totalActual - totalPlanned) / totalPlanned * 100).toFixed(1);

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
                <th className="text-left py-4 px-4 text-xs font-semibold text-neutral-500 uppercase tracking-wide">Category</th>
                <th className="text-right py-4 px-4 text-xs font-semibold text-neutral-500 uppercase tracking-wide">Planned (€)</th>
                <th className="text-right py-4 px-4 text-xs font-semibold text-neutral-500 uppercase tracking-wide">Actual (€)</th>
                <th className="text-right py-4 px-4 text-xs font-semibold text-neutral-500 uppercase tracking-wide">Variance</th>
                <th className="text-left py-4 px-4 text-xs font-semibold text-neutral-500 uppercase tracking-wide">Notes</th>
              </tr>
            </thead>
            
            {/* Body */}
            <tbody>
              {expenses.map((expense, idx) => {
                const isPositive = expense.variance <= 0; // For expenses, negative variance is good
                const badgeColor = expense.variance === 0 
                  ? 'bg-cyan-50 text-cyan-600 border-cyan-200'
                  : isPositive 
                    ? 'bg-green-50 text-green-600 border-green-200' 
                    : 'bg-red-50 text-red-600 border-red-200';
                
                const isLastRow = idx === expenses.length - 1;
                
                return (
                  <tr key={idx} className={`${isLastRow ? 'border-b-2 border-black/10' : 'border-b border-black/5'} row-hover transition-all`}>
                    <td className="py-4 px-4">
                      <p className="text-sm font-medium text-black">{expense.category}</p>
                      <p className="text-xs text-neutral-400 mt-0.5">{expense.subtitle}</p>
                    </td>
                    <td className="text-right py-4 px-4 text-sm font-medium text-neutral-600">
                      €{expense.planned.toLocaleString()}
                    </td>
                    <td className="text-right py-4 px-4 text-sm font-semibold text-black">
                      €{expense.actual.toLocaleString()}
                    </td>
                    <td className="text-right py-4 px-4">
                      <span className={`inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-xs font-semibold border ${badgeColor}`}>
                        {expense.variance > 0 ? '+' : ''}{expense.variance.toFixed(1)}%
                      </span>
                    </td>
                    <td className="py-4 px-4 text-sm text-neutral-500">{expense.notes}</td>
                  </tr>
                );
              })}

              {/* Total Row */}
              <tr className="bg-cyan-50/30 border-t-2 border-cyan-400/40">
                <td className="py-5 px-4">
                  <p className="text-base font-bold text-black">Total Expenses</p>
                </td>
                <td className="text-right py-5 px-4 text-base font-bold text-neutral-600">
                  €{totalPlanned.toLocaleString()}
                </td>
                <td className="text-right py-5 px-4 text-base font-bold text-black">
                  €{totalActual.toLocaleString()}
                </td>
                <td className="text-right py-5 px-4">
                  <span className="inline-flex items-center gap-1 px-3 py-1.5 rounded-full bg-cyan-100 text-cyan-600 text-sm font-bold border border-cyan-300">
                    {totalVariance > 0 ? '+' : ''}{totalVariance}%
                  </span>
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

