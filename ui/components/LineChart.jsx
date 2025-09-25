'use client'

import { ResponsiveContainer, LineChart as RLineChart, Line, XAxis, YAxis, Tooltip, Legend, CartesianGrid } from 'recharts';

export default function LineChart({ data = [] }) {
  return (
    <div className="w-full h-72">
      <ResponsiveContainer width="100%" height="100%">
        <RLineChart data={data} margin={{ top: 8, right: 16, left: 0, bottom: 0 }}>
          <CartesianGrid stroke="rgba(148,163,184,0.08)" />
          <XAxis dataKey="date" tick={{ fill: '#94a3b8', fontSize: 12 }} tickLine={false} axisLine={false} />
          <YAxis tick={{ fill: '#94a3b8', fontSize: 12 }} tickLine={false} axisLine={false} />
          <Tooltip contentStyle={{ background: '#0b1220', border: '1px solid #1f2937', color: '#e5e7eb' }} />
          <Legend />
          <Line type="monotone" dataKey="visitors" stroke="#22d3ee" strokeWidth={2} dot={false} fillOpacity={0.12} />
          <Line type="monotone" dataKey="conversions" stroke="#a78bfa" strokeWidth={2} dot={false} />
        </RLineChart>
      </ResponsiveContainer>
    </div>
  );
}
