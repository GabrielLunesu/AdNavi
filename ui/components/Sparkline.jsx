'use client'

// Tiny sparkline line chart using Recharts (static data)
import { ResponsiveContainer, LineChart, Line } from 'recharts';

export default function Sparkline({ data = [], color = '#22d3ee' }) {
  // Transform array of numbers into { x, y } series for Recharts
  const series = Array.isArray(data)
    ? data.map((v, i) => ({ x: i + 1, y: v }))
    : [];

  return (
    <div className="w-24 h-12">
      <ResponsiveContainer width="100%" height="100%">
        <LineChart data={series} margin={{ top: 6, bottom: 0, left: 0, right: 0 }}>
          <Line type="monotone" dataKey="y" stroke={color} strokeWidth={2} dot={false} />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}
