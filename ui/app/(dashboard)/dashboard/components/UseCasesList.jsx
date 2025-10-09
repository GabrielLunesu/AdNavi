import { Rocket, LineChart, Store } from "lucide-react";

const useCases = [
  {
    id: 1,
    icon: Rocket,
    title: "From zero to profitable campaign in 48h",
    description: "Launch and optimize your first campaign with AI guidance",
  },
  {
    id: 2,
    icon: LineChart,
    title: "Understand ROAS without spreadsheets",
    description: "Visual analytics that make sense of your marketing data",
  },
  {
    id: 3,
    icon: Store,
    title: "How to market a local business with $500/mo",
    description: "Smart strategies for small budgets with big impact",
  },
];

export default function UseCasesList() {
  return (
    <div className="mb-16">
      <h3 className="text-2xl font-semibold text-neutral-900 mb-6">Discover Use Cases</h3>
      <div className="grid grid-cols-3 gap-6">
        {useCases.map((useCase) => {
          const Icon = useCase.icon;
          return (
            <div
              key={useCase.id}
              className="glass-card rounded-3xl p-6 border border-neutral-200/60 shadow-lg card-hover group cursor-pointer relative overflow-hidden"
            >
              <div className="absolute bottom-0 left-0 right-0 h-1 bg-gradient-to-r from-cyan-400 to-cyan-600 opacity-0 group-hover:opacity-100 transition-opacity"></div>
              <div className="w-12 h-12 rounded-2xl bg-cyan-50 flex items-center justify-center mb-4">
                <Icon className="w-6 h-6 text-cyan-600" strokeWidth={1.5} />
              </div>
              <h4 className="text-base font-semibold text-neutral-900 mb-2">{useCase.title}</h4>
              <p className="text-sm text-neutral-600">{useCase.description}</p>
            </div>
          );
        })}
      </div>
    </div>
  );
}

