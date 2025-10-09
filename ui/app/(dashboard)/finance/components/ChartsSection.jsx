"use client";
import { useEffect, useRef, useState } from "react";
import { Chart, registerables } from "chart.js";
import { fetchWorkspaceKpis } from "../../../../lib/api";
import { currentUser } from "../../../../lib/auth";

Chart.register(...registerables);

export default function ChartsSection() {
  const revenueChartRef = useRef(null);
  const profitChartRef = useRef(null);
  const revenueChartInstance = useRef(null);
  const profitChartInstance = useRef(null);
  const [workspaceId, setWorkspaceId] = useState(null);
  const [revenueData, setRevenueData] = useState(null);
  const [conversionsData, setConversionsData] = useState(null);
  const [loading, setLoading] = useState(true);

  // Fetch workspace ID and revenue data
  useEffect(() => {
    let mounted = true;
    
    currentUser().then(user => {
      if (!mounted || !user) return;
      setWorkspaceId(user.workspace_id);
      
      // Fetch last 7 days of revenue data
      return fetchWorkspaceKpis({
        workspaceId: user.workspace_id,
        metrics: ['revenue', 'conversions'],
        lastNDays: 7,
        dayOffset: 0,
        compareToPrevious: false,
        sparkline: true
      });
    }).then(data => {
      if (!mounted || !data) return;
      
      const revenueMetric = data.find(m => m.key === 'revenue');
      const conversionsMetric = data.find(m => m.key === 'conversions');
      
      setRevenueData(revenueMetric);
      setConversionsData(conversionsMetric);
      setLoading(false);
    }).catch(err => {
      console.error('Failed to fetch revenue data:', err);
      setLoading(false);
    });
    
    return () => { mounted = false; };
  }, []);

  useEffect(() => {
    // Revenue Chart (Last 7 Days)
    if (revenueChartRef.current && revenueData && !loading) {
      const ctx = revenueChartRef.current.getContext('2d');
      
      if (revenueChartInstance.current) {
        revenueChartInstance.current.destroy();
      }
      
      // Get last 7 days labels
      const getDayLabels = () => {
        const days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
        const labels = [];
        const today = new Date();
        
        for (let i = 6; i >= 0; i--) {
          const date = new Date(today);
          date.setDate(date.getDate() - i);
          labels.push(days[date.getDay()]);
        }
        
        return labels;
      };
      
      const labels = getDayLabels();
      const revenueValues = revenueData.sparkline ? revenueData.sparkline.map(sp => sp.value || 0) : [];
      const conversionsValues = conversionsData && conversionsData.sparkline ? conversionsData.sparkline.map(sp => sp.value || 0) : [];
      
      // Calculate totals for legend
      const totalRevenue = revenueValues.reduce((sum, val) => sum + val, 0);
      const totalConversions = conversionsValues.reduce((sum, val) => sum + val, 0);
      
      revenueChartInstance.current = new Chart(ctx, {
        type: 'bar',
        data: {
          labels: labels,
          datasets: [
            {
              label: `Revenue: $${totalRevenue.toLocaleString(undefined, { maximumFractionDigits: 0 })}`,
              data: revenueValues,
              backgroundColor: 'rgba(6, 182, 212, 0.8)',
              borderColor: '#06B6D4',
              borderWidth: 0,
              borderRadius: 8,
              barPercentage: 0.7
            }
          ]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: {
            legend: {
              display: true,
              position: 'bottom',
              labels: {
                usePointStyle: true,
                padding: 20,
                font: { size: 12, weight: '500' },
                color: '#0B0B0B'
              }
            },
            tooltip: {
              backgroundColor: 'rgba(255, 255, 255, 0.95)',
              titleColor: '#0B0B0B',
              bodyColor: '#0B0B0B',
              borderColor: 'rgba(6, 182, 212, 0.2)',
              borderWidth: 1,
              padding: 12,
              displayColors: true,
              callbacks: {
                label: function(context) {
                  return 'Revenue: $' + context.parsed.y.toLocaleString(undefined, { maximumFractionDigits: 0 });
                }
              }
            }
          },
          scales: {
            x: {
              grid: { display: false },
              ticks: { color: '#737373', font: { size: 11 } }
            },
            y: {
              grid: { color: 'rgba(0, 0, 0, 0.05)' },
              ticks: {
                color: '#737373',
                font: { size: 11 },
                callback: function(value) {
                  return '$' + value.toLocaleString(undefined, { maximumFractionDigits: 0 });
                }
              }
            }
          }
        }
      });
    }

    // Profit Composition Chart
    if (profitChartRef.current) {
      const ctx = profitChartRef.current.getContext('2d');
      
      if (profitChartInstance.current) {
        profitChartInstance.current.destroy();
      }
      
      profitChartInstance.current = new Chart(ctx, {
        type: 'doughnut',
        data: {
          labels: ['Google Ads', 'Meta Ads', 'SaaS Tools', 'Agency Fees', 'Miscellaneous'],
          datasets: [{
            data: [3847, 3926, 842, 1200, 285],
            backgroundColor: [
              'rgba(6, 182, 212, 0.8)',
              'rgba(6, 182, 212, 0.6)',
              'rgba(6, 182, 212, 0.4)',
              'rgba(6, 182, 212, 0.25)',
              'rgba(6, 182, 212, 0.15)'
            ],
            borderColor: '#fff',
            borderWidth: 3,
            hoverOffset: 15
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          cutout: '65%',
          plugins: {
            legend: {
              display: true,
              position: 'right',
              labels: {
                usePointStyle: true,
                padding: 15,
                font: { size: 11, weight: '500' }
              }
            },
            tooltip: {
              backgroundColor: 'rgba(255, 255, 255, 0.95)',
              titleColor: '#0B0B0B',
              bodyColor: '#0B0B0B',
              borderColor: 'rgba(6, 182, 212, 0.2)',
              borderWidth: 1,
              padding: 12,
              displayColors: true,
              callbacks: {
                label: function(context) {
                  const value = context.parsed;
                  const total = context.dataset.data.reduce((a, b) => a + b, 0);
                  const percentage = ((value / total) * 100).toFixed(1);
                  return context.label + ': €' + value.toLocaleString() + ' (' + percentage + '%)';
                }
              }
            }
          }
        },
        plugins: [{
          beforeDraw: function(chart) {
            const width = chart.width;
            const height = chart.height;
            const ctx = chart.ctx;
            ctx.restore();
            const fontSize = (height / 160).toFixed(2);
            ctx.font = fontSize + "em sans-serif";
            ctx.textBaseline = "middle";
            ctx.fillStyle = "#06B6D4";
            const text = "Net Margin";
            const textX = Math.round((width - ctx.measureText(text).width) / 2);
            const textY = height / 2 - 15;
            ctx.fillText(text, textX, textY);
            
            ctx.font = "bold " + (fontSize * 2) + "em sans-serif";
            ctx.fillStyle = "#0B0B0B";
            const text2 = "58%";
            const textX2 = Math.round((width - ctx.measureText(text2).width) / 2);
            const textY2 = height / 2 + 15;
            ctx.fillText(text2, textX2, textY2);
            ctx.save();
          }
        }]
      });
    }

    return () => {
      if (revenueChartInstance.current) {
        revenueChartInstance.current.destroy();
      }
      if (profitChartInstance.current) {
        profitChartInstance.current.destroy();
      }
    };
  }, [revenueData, conversionsData, loading]);

  return (
    <div className="grid grid-cols-2 gap-6 mb-8">
      {/* Revenue Chart (Last 7 Days) */}
      <div className="glass-card rounded-3xl border border-neutral-200/60 shadow-lg p-8 relative overflow-hidden fade-up-in" style={{ animationDelay: '500ms' }}>
        <div className="absolute -bottom-10 -left-10 w-40 h-40 bg-cyan-400 rounded-full blur-[100px] opacity-15 pulse-glow-aura"></div>
        <h3 className="text-lg font-semibold text-neutral-900 mb-6">Revenue</h3>
        <div className="h-64">
          {loading ? (
            <div className="flex items-center justify-center h-full">
              <div className="w-8 h-8 border-4 border-cyan-500 border-t-transparent rounded-full animate-spin"></div>
            </div>
          ) : (
            <canvas ref={revenueChartRef}></canvas>
          )}
        </div>
      </div>

      {/* Profit Composition Chart */}
      <div className="glass-card rounded-3xl border border-neutral-200/60 shadow-lg p-8 relative overflow-hidden fade-up-in" style={{ animationDelay: '600ms' }}>
        <div className="absolute -bottom-10 -right-10 w-40 h-40 bg-cyan-400 rounded-full blur-[100px] opacity-15 pulse-glow-aura" style={{ animationDelay: '3s' }}></div>
        <h3 className="text-lg font-semibold text-neutral-900 mb-6">Profit Composition</h3>
        <div className="h-64 flex items-center justify-center">
          <canvas ref={profitChartRef}></canvas>
        </div>
      </div>
    </div>
  );
}

