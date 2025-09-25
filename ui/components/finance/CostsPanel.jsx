'use client'

import { useState } from 'react';
import Card from "../../components/Card";
import CostRow from "./CostRow";
import AddCostRow from "./AddCostRow";
import { seedCosts, totalCostsSelected } from "../../data/finance/costs";

export default function CostsPanel() {
  const [rows, setRows] = useState(seedCosts);
  const [showAdd, setShowAdd] = useState(false);

  const handleSave = (r) => {
    setRows(prev => [...prev, { id: crypto.randomUUID(), ...r }]);
    setShowAdd(false);
  };
  const handleRemove = (id) => setRows(prev => prev.filter(x => x.id !== id));

  return (
    <Card className="rounded-2xl mb-6">
      <div className="flex items-center justify-between mb-3">
        <h3 className="text-xl font-medium">Costs</h3>
        <button onClick={() => setShowAdd(true)} className="px-3 py-1.5 text-sm rounded-full border border-slate-600/40 bg-slate-900/35 hover:border-cyan-400/60">Add Cost</button>
      </div>
      <div className="rounded-xl border border-white/10 overflow-hidden">
        <div className="grid grid-cols-12 px-3 py-2 text-xs text-slate-400 bg-white/5 border-b border-white/10">
          <div className="col-span-3">Name</div>
          <div className="col-span-2">Amount</div>
          <div className="col-span-3">Date / Range</div>
          <div className="col-span-3">Notes</div>
          <div className="col-span-1 text-right">Actions</div>
        </div>
        <div className="divide-y divide-white/10">
          {rows.map(r => (
            <CostRow key={r.id} row={r} onRemove={handleRemove} />
          ))}
          {showAdd ? (
            <AddCostRow onSave={handleSave} onCancel={() => setShowAdd(false)} />
          ) : null}
        </div>
      </div>
      <div className="mt-3 flex items-center justify-between text-sm">
        <div className="text-slate-400">Costs are deducted from Revenue when viewing Net.</div>
        <div className="flex items-center gap-4">
          <div className="text-slate-400">Total Costs (selected):</div>
          <div className="text-lg font-medium tracking-tight">{totalCostsSelected}</div>
        </div>
      </div>
    </Card>
  );
}
