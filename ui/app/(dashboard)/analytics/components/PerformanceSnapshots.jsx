import { Trophy, MousePointerClick, Image } from "lucide-react";

const snapshots = [
  {
    id: 'campaigns',
    title: 'Top Performing Campaigns',
    icon: Trophy,
    items: [
      { name: 'Summer Sale 2024', value: '92%', percentage: 92 },
      { name: 'Product Launch Q2', value: '87%', percentage: 87 },
      { name: 'Brand Awareness', value: '81%', percentage: 81 },
    ],
  },
  {
    id: 'adsets',
    title: 'Ad Sets with Highest CTR',
    icon: MousePointerClick,
    items: [
      { name: 'Lookalike Audience A', value: '4.8%', percentage: 95 },
      { name: 'Retargeting - 30d', value: '4.2%', percentage: 88 },
      { name: 'Interest: Tech Early Adopters', value: '3.9%', percentage: 82 },
    ],
  },
  {
    id: 'creatives',
    title: 'Most Efficient Creatives',
    icon: Image,
    items: [
      { name: 'Video: Product Demo v3', value: '5.2x', percentage: 94 },
      { name: 'Carousel: Features', value: '4.7x', percentage: 86 },
      { name: 'Static: Testimonial', value: '4.1x', percentage: 79 },
    ],
  },
];

export default function PerformanceSnapshots() {
  return (
    <div className="mx-8">
      <h3 className="text-2xl font-semibold text-neutral-900 mb-6">Performance Snapshots</h3>
      <div className="flex gap-6 overflow-x-auto pb-4 no-scrollbar">
        {snapshots.map((snapshot) => {
          const Icon = snapshot.icon;
          return (
            <div key={snapshot.id} className="glass-card rounded-3xl p-6 border border-neutral-200/60 shadow-lg card-hover min-w-[340px]">
              <div className="flex items-center gap-3 mb-5">
                <div className="w-10 h-10 rounded-xl bg-cyan-50 flex items-center justify-center">
                  <Icon className="w-5 h-5 text-cyan-600" strokeWidth={1.5} />
                </div>
                <h4 className="text-base font-semibold text-neutral-900">{snapshot.title}</h4>
              </div>
              <div className="space-y-4">
                {snapshot.items.map((item, idx) => (
                  <div key={idx} className="flex items-center justify-between">
                    <span className="text-sm text-neutral-700">{item.name}</span>
                    <div className="flex items-center gap-2">
                      <div className="w-20 h-1.5 bg-neutral-100 rounded-full overflow-hidden">
                        <div className="h-full bg-cyan-500 rounded-full" style={{ width: `${item.percentage}%` }}></div>
                      </div>
                      <span className="text-xs font-medium text-neutral-900">{item.value}</span>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}

