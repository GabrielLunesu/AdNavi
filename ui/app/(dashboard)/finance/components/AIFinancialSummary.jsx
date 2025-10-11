/**
 * AI Financial Summary
 * 
 * WHAT: AI-generated financial insight via QA system
 * WHY: Natural language summary and recommendations
 * REFERENCES: lib/api.js:fetchQA
 */

"use client";
import { useState, useEffect } from "react";
import { Sparkles, TrendingUp } from "lucide-react";
import { fetchQA } from "@/lib/api";

export default function AIFinancialSummary({ workspaceId, selectedPeriod }) {
  const [insight, setInsight] = useState(null);
  const [loading, setLoading] = useState(false);
  
  // Auto-generate insight on mount or period change
  useEffect(() => {
    if (workspaceId && selectedPeriod) {
      generateInsight();
    }
  }, [workspaceId, selectedPeriod]); // Removed hasGenerated from dependencies to trigger on period change
  
  const generateInsight = async () => {
    setLoading(true);
    try {
      // Calculate date range
      const startDate = new Date(selectedPeriod.year, selectedPeriod.month - 1, 1);
      
      // Check if it's the current month
      const now = new Date();
      const isCurrentMonth = selectedPeriod.year === now.getFullYear() && 
                           selectedPeriod.month === (now.getMonth() + 1);
      
      let endDate;
      if (isCurrentMonth) {
        // If current month, use today's date
        endDate = now;
      } else {
        // Otherwise, use the last day of the selected month
        endDate = new Date(selectedPeriod.year, selectedPeriod.month, 0);
      }
      
      // Format dates as readable strings
      const formatDate = (date) => {
        const monthNames = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"];
        return `${monthNames[date.getMonth()]} ${date.getDate()}`;
      };
      
      const question = `Workspace performance breakdown from ${formatDate(startDate)} to ${formatDate(endDate)}?`;
      
      // Log for debugging
      console.log('Finance AI Question:', question);
      
      const response = await fetchQA({
        workspaceId,
        question
      });
      
      console.log('Finance AI Response:', response);
      
      setInsight(response.answer);
    } catch (err) {
      console.error('Failed to generate insight:', err);
      setInsight('Unable to generate insight. Please try again.');
    } finally {
      setLoading(false);
    }
  };
  
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
        
        {loading && !insight && (
          <div className="flex items-center gap-3">
            <div className="w-2 h-2 bg-cyan-500 rounded-full animate-bounce" style={{ animationDelay: '0ms' }}></div>
            <div className="w-2 h-2 bg-cyan-500 rounded-full animate-bounce" style={{ animationDelay: '150ms' }}></div>
            <div className="w-2 h-2 bg-cyan-500 rounded-full animate-bounce" style={{ animationDelay: '300ms' }}></div>
            <span className="text-sm text-neutral-500 ml-2">Analyzing financial data...</span>
          </div>
        )}
        
        {!insight && !loading && (
          <button
            onClick={generateInsight}
            disabled={loading}
            className="group px-4 py-2 rounded-xl bg-gradient-to-r from-cyan-500 to-cyan-600 text-white text-sm font-semibold shadow-lg shadow-cyan-500/30 hover:shadow-xl hover:shadow-cyan-500/40 hover:from-cyan-600 hover:to-cyan-700 transition-all active:scale-95 flex items-center gap-2 disabled:opacity-50 disabled:cursor-not-allowed"
          >
            <TrendingUp className="w-4 h-4" strokeWidth={2.5} />
            Regenerate Insight
          </button>
        )}
        
        {insight && (
          <div className="mb-6">
            <p className="text-base text-neutral-700 leading-relaxed whitespace-pre-wrap">
              {insight}
            </p>
          </div>
        )}
      </div>
    </div>
  );
}
