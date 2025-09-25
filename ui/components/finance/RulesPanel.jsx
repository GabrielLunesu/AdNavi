'use client'

import { useState } from 'react';
import Card from "../../components/Card";
import RuleBuilder from "./RuleBuilder";
import RuleRow from "./RuleRow";
import { seedRules } from "../../data/finance/rules";

export default function RulesPanel() {
  const [rules, setRules] = useState(seedRules);
  const [show, setShow] = useState(false);

  const addRule = (r) => {
    setRules(prev => [{ id: crypto.randomUUID(), ...r }, ...prev]);
    setShow(false);
  };
  const removeRule = (id) => setRules(prev => prev.filter(x => x.id !== id));

  return (
    <Card className="rounded-2xl mb-10">
      <div className="flex items-center justify-between mb-3">
        <h3 className="text-xl font-medium">Rules</h3>
        <button onClick={() => setShow(true)} className="px-3 py-1.5 text-sm rounded-full border border-slate-600/40 bg-slate-900/35 hover:border-cyan-400/60">Add Rule</button>
      </div>
      {show ? <RuleBuilder onSave={addRule} onCancel={() => setShow(false)} /> : null}
      <div className="space-y-2">
        {rules.map(r => (
          <RuleRow key={r.id} rule={r} onRemove={removeRule} />
        ))}
      </div>
      <div className="text-xs text-slate-400 mt-2">Notifications: In-app only for MVP.</div>
    </Card>
  );
}
