import { Sparkles, Search, TrendingUp, Calendar } from "lucide-react";

const suggestedQuestions = [
  { icon: Search, text: 'Where did we overspend this month?' },
  { icon: TrendingUp, text: "What's driving profit growth?" },
  { icon: Calendar, text: 'Show me predicted costs next month' },
];

export default function AIFinancialSummary() {
  return (
    <div className="glass-card rounded-3xl border border-black/5 shadow-xl p-8 relative overflow-hidden fade-up-in" style={{ animationDelay: '800ms' }}>
      <div className="absolute -bottom-20 -right-20 w-64 h-64 bg-cyan-400 rounded-full blur-[120px] opacity-20 pulse-glow-aura"></div>
      
      <div className="relative z-10">
        <div className="flex items-center gap-3 mb-6">
          <div className="w-10 h-10 rounded-xl bg-gradient-to-br from-cyan-400 to-cyan-600 flex items-center justify-center">
            <Sparkles className="w-5 h-5 text-white" strokeWidth={1.5} />
          </div>
          <h3 className="text-lg font-semibold text-black">AdNavi Insight: Financial Overview</h3>
        </div>
        
        <div className="mb-6">
          <p className="text-base text-neutral-700 leading-relaxed">
            Profit margins improved by <span className="font-semibold text-cyan-600">8.2%</span> this month due to reduced Meta CPC and higher conversion rates on Google campaigns. Your total revenue of <span className="font-semibold text-cyan-600">€24.3K</span> exceeded projections, while maintaining controlled spending at <span className="font-semibold text-cyan-600">€8.9K</span>. ROAS performance of <span className="font-semibold text-cyan-600">2.73x</span> is well above your target threshold.
          </p>
        </div>
        
        {/* <div className="flex flex-wrap gap-3">
          {suggestedQuestions.map((q, idx) => {
            const Icon = q.icon;
            return (
              <button key={idx} className="suggestion-pill px-5 py-3 rounded-full bg-white/60 border border-black/5 text-sm font-medium text-neutral-700 hover:text-black flex items-center gap-2">
                <Icon className="w-4 h-4" strokeWidth={1.5} />
                {q.text}
              </button>
            );
          })}
        </div> */}
      </div>
    </div>
  );
}

