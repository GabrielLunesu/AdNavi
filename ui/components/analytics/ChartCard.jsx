'use client'

import { useState } from 'react';
import { Equal, LineChart as Lc, GitCompare, HelpCircle } from 'lucide-react';
import { ResponsiveContainer, LineChart, Line, XAxis, YAxis, Tooltip, Legend, CartesianGrid } from 'recharts';
import TabPill from "../../components/TabPill";
import PillButton from "../../components/PillButton";
import Card from "../../components/Card";
import { chartLabels, revenue, spend, roas } from "../../data/analytics/chart";

const baseData = chartLabels.map((d, i) => ({ date: d, revenue: revenue[i], spend: spend[i], roas: roas[i] }));

export default function ChartCard() {
  const [activeMetric, setActiveMetric] = useState('revenue');

  return (
    <Card className="rounded-2xl mb-6">
      <div className="flex items-center justify-between">
        <div className="flex items-center gap-2">
          <TabPill active={activeMetric==='revenue'} onClick={() => setActiveMetric('revenue')}>Revenue</TabPill>
          <TabPill active={activeMetric==='roas'} onClick={() => setActiveMetric('roas')}>ROAS</TabPill>
          <TabPill active={activeMetric==='spend'} onClick={() => setActiveMetric('spend')}>Spend</TabPill>
        </div>
        <div className="flex items-center gap-2">
          {/* <PillButton><Equal size={16} /> <span className="ml-1">Normalize by spend</span></PillButton> */}
          <PillButton><Lc size={16} /> <span className="ml-1">Line</span></PillButton>
          <PillButton><GitCompare size={16} /> <span className="ml-1">vs last period</span></PillButton>
          <button className="text-slate-400 hover:text-white" title="This chart tracks KPIs over time."><HelpCircle size={20} /></button>
        </div>
      </div>
      <div className="mt-4 rounded-xl bg-[#0B1220] border border-white/10 p-3">
        <h4 className="text-sm text-slate-400 mb-1">Revenue, Spend, ROAS</h4>
        <div className="w-full h-72">
          <ResponsiveContainer width="100%" height="100%">
            <LineChart data={baseData} margin={{ top: 8, right: 16, left: 0, bottom: 0 }}>
              <CartesianGrid stroke="rgba(148,163,184,0.12)" />
              <XAxis dataKey="date" tick={{ fill: '#94a3b8', fontSize: 12 }} tickLine={false} axisLine={false} />
              <YAxis yAxisId="left" tick={{ fill: '#94a3b8', fontSize: 12 }} tickLine={false} axisLine={false} />
              <YAxis yAxisId="right" orientation="right" tick={{ fill: '#94a3b8', fontSize: 12 }} tickLine={false} axisLine={false} />
              <Tooltip contentStyle={{ background: '#0b1220', border: '1px solid #1f2937', color: '#e5e7eb' }} />
              <Legend />
              <Line type="monotone" dataKey="revenue" name="Revenue" stroke="#a78bfa" strokeWidth={2} dot={{ r: 3 }} yAxisId="left" />
              <Line type="monotone" dataKey="spend" name="Spend" stroke="#f43f5e" strokeWidth={2} dot={{ r: 3 }} yAxisId="left" />
              <Line type="monotone" dataKey="roas" name="ROAS" stroke="#60a5fa" strokeWidth={2} dot={{ r: 3 }} yAxisId="right" />
            </LineChart>
          </ResponsiveContainer>
        </div>
      </div>
    </Card>
  );
}
