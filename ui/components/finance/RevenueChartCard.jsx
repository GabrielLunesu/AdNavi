'use client'

import { useState } from 'react';
import Card from "../../components/Card";
import { ResponsiveContainer, LineChart, Line, XAxis, YAxis, Tooltip, Legend, CartesianGrid } from 'recharts';
import { labels, revenue, spend, net } from "../../data/finance/series";

const baseData = labels.map((d, i) => ({ date: d, revenue: revenue[i], spend: spend[i], net: net[i] }));

export default function RevenueChartCard() {
  const [showNet, setShowNet] = useState(false);
  return (
    <Card className="rounded-2xl mb-6">
      <div className="flex items-center justify-between">
        <div className="flex items-center gap-2">
          <h3 className="text-xl font-medium">Revenue vs Spend</h3>
        </div>
        <button onClick={() => setShowNet(!showNet)} className="rounded-full px-3 py-1.5 text-sm border border-slate-600/40 bg-slate-900/35">
          {showNet ? 'Hide Net' : 'Show Net'}
        </button>
      </div>
      <div className="mt-4 rounded-xl bg-[#0B1220] border border-white/10 p-3">
        <h4 className="text-sm text-slate-400 mb-1">Daily</h4>
        <div className="w-full h-72">
          <ResponsiveContainer width="100%" height="100%">
            <LineChart data={baseData} margin={{ top: 8, right: 16, left: 0, bottom: 0 }}>
              <CartesianGrid stroke="rgba(148,163,184,0.12)" />
              <XAxis dataKey="date" tick={{ fill: '#94a3b8', fontSize: 12 }} tickLine={false} axisLine={false} />
              <YAxis tick={{ fill: '#94a3b8', fontSize: 12 }} tickLine={false} axisLine={false} />
              <Tooltip contentStyle={{ background: '#0b1220', border: '1px solid #1f2937', color: '#e5e7eb' }} />
              <Legend />
              <Line type="monotone" dataKey="revenue" name="Revenue" stroke="#a78bfa" strokeWidth={2} dot={false} />
              <Line type="monotone" dataKey="spend" name="Spend" stroke="#f43f5e" strokeWidth={2} dot={false} />
              {showNet ? <Line type="monotone" dataKey="net" name="Net" stroke="#22c55e" strokeWidth={2} dot={false} /> : null}
            </LineChart>
          </ResponsiveContainer>
        </div>
      </div>
    </Card>
  );
}
