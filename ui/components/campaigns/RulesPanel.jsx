'use client'

import { useState } from 'react';
import Card from "../../components/Card";
import { seedRules } from "../../data/campaigns/rules";

export default function RulesPanel() {
  const [rules, setRules] = useState(seedRules);
  const [show, setShow] = useState(false);
  const [input, setInput] = useState('');

  const add = () => { if (!input.trim()) return; setRules(prev => [{ id: crypto.randomUUID(), label: input.trim() }, ...prev]); setInput(''); setShow(false); };
  const remove = (id) => setRules(prev => prev.filter(r => r.id !== id));

  return (
    <Card className="rounded-2xl mt-6">
      <div className="flex items-center justify-between mb-3">
        <h3 className="text-xl font-medium">Rules</h3>
        <button onClick={() => setShow(true)} className="px-3 py-1.5 text-sm rounded-full border border-slate-600/40 bg-slate-900/35 hover:border-cyan-400/60">Add Rule</button>
      </div>
      {show ? (
        <div className="rounded-xl p-3 border border-white/10 bg-slate-900/35 mb-3 flex items-center gap-2">
          <input value={input} onChange={(e)=>setInput(e.target.value)} placeholder="e.g. ROAS < 1.5 → Notify" className="flex-1 bg-transparent px-3 py-2 rounded-lg border border-white/10 text-sm" />
          <button onClick={add} className="px-2.5 py-1.5 text-xs rounded-full bg-emerald-500/15 text-emerald-300 border border-emerald-400/20">Save</button>
          <button onClick={()=>setShow(false)} className="px-2.5 py-1.5 text-xs rounded-full bg-rose-500/15 text-rose-300 border border-rose-400/20">Cancel</button>
        </div>
      ) : null}
      <div className="space-y-2">
        {rules.map(r => (
          <div key={r.id} className="rounded-xl p-3 border border-white/10 bg-slate-900/35 flex items-center justify-between">
            <div className="text-sm">{r.label}</div>
            <div className="flex items-center gap-2">
              <span className="text-xs px-2 py-1 rounded-full bg-white/5 border border-white/10 text-cyan-300">In-app</span>
              <button onClick={()=>remove(r.id)} className="px-2.5 py-1.5 text-xs rounded-full bg-rose-500/15 text-rose-300 border border-rose-400/20">Remove</button>
            </div>
          </div>
        ))}
      </div>
      <div className="text-xs text-slate-400 mt-2">Notifications: In-app only for MVP.</div>
    </Card>
  );
}
