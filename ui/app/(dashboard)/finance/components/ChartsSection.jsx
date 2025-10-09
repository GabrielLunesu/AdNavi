"use client";
import { useEffect, useRef } from "react";
import { Chart, registerables } from "chart.js";

Chart.register(...registerables);

export default function ChartsSection() {
  const budgetChartRef = useRef(null);
  const profitChartRef = useRef(null);
  const budgetChartInstance = useRef(null);
  const profitChartInstance = useRef(null);

  useEffect(() => {
    // Budget vs Actual Chart
    if (budgetChartRef.current) {
      const ctx = budgetChartRef.current.getContext('2d');
      
      if (budgetChartInstance.current) {
        budgetChartInstance.current.destroy();
      }
      
      budgetChartInstance.current = new Chart(ctx, {
        type: 'line',
        data: {
          labels: ['Week 1', 'Week 2', 'Week 3', 'Week 4'],
          datasets: [
            {
              label: 'Planned',
              data: [2500, 2500, 2500, 2600],
              borderColor: '#06B6D4',
              backgroundColor: 'rgba(6, 182, 212, 0.1)',
              borderWidth: 2,
              tension: 0.4,
              fill: false,
              pointRadius: 5,
              pointHoverRadius: 7,
              pointBackgroundColor: '#06B6D4',
              pointBorderColor: '#fff',
              pointBorderWidth: 2
            },
            {
              label: 'Actual',
              data: [2380, 2420, 2510, 2790],
              borderColor: '#0B0B0B',
              backgroundColor: 'rgba(11, 11, 11, 0.05)',
              borderWidth: 2,
              tension: 0.4,
              fill: false,
              pointRadius: 5,
              pointHoverRadius: 7,
              pointBackgroundColor: '#0B0B0B',
              pointBorderColor: '#fff',
              pointBorderWidth: 2
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
                font: { size: 12, weight: '500' }
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
                  return context.dataset.label + ': €' + context.parsed.y.toLocaleString();
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
                  return '€' + value.toLocaleString();
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
      if (budgetChartInstance.current) {
        budgetChartInstance.current.destroy();
      }
      if (profitChartInstance.current) {
        profitChartInstance.current.destroy();
      }
    };
  }, []);

  return (
    <div className="grid grid-cols-2 gap-6 mb-8">
      {/* Budget vs Actual Chart */}
      <div className="glass-card rounded-3xl border border-black/5 shadow-xl p-8 relative overflow-hidden fade-up-in" style={{ animationDelay: '500ms' }}>
        <div className="absolute -bottom-10 -left-10 w-40 h-40 bg-cyan-400 rounded-full blur-[100px] opacity-15 pulse-glow-aura"></div>
        <h3 className="text-lg font-semibold text-black mb-6">Budget vs Actual</h3>
        <div className="h-64">
          <canvas ref={budgetChartRef}></canvas>
        </div>
      </div>

      {/* Profit Composition Chart */}
      <div className="glass-card rounded-3xl border border-black/5 shadow-xl p-8 relative overflow-hidden fade-up-in" style={{ animationDelay: '600ms' }}>
        <div className="absolute -bottom-10 -right-10 w-40 h-40 bg-cyan-400 rounded-full blur-[100px] opacity-15 pulse-glow-aura" style={{ animationDelay: '3s' }}></div>
        <h3 className="text-lg font-semibold text-black mb-6">Profit Composition</h3>
        <div className="h-64 flex items-center justify-center">
          <canvas ref={profitChartRef}></canvas>
        </div>
      </div>
    </div>
  );
}

