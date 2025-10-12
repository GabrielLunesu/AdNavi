/**
 * Charts Section
 * 
 * WHAT: Displays profit composition pie chart
 * WHY: Visual breakdown of spend sources
 * REFERENCES: lib/pnlAdapter.js:adaptPnLStatement
 */

"use client";
import { useEffect, useRef } from "react";
import { Chart, registerables } from "chart.js";

Chart.register(...registerables);

export default function ChartsSection({ composition, timeseries, totalRevenue, totalSpend, excludedRows = new Set(), rows = [], onRowToggle }) {
  const profitChartRef = useRef(null);
  const profitChartInstance = useRef(null);
  const revenueChartRef = useRef(null);
  const revenueChartInstance = useRef(null);

  useEffect(() => {
    // Profit Composition Chart
    if (profitChartRef.current && composition && composition.length > 0) {
      const ctx = profitChartRef.current.getContext('2d');
      
      if (profitChartInstance.current) {
        profitChartInstance.current.destroy();
      }
      
      // Keep all items but set excluded ones to 0 for chart display
      const labels = composition.map(c => c.label);
      const data = composition.map(item => {
        const matchingRow = rows.find(r => r.category === item.label);
        const isExcluded = matchingRow && excludedRows.has(matchingRow.id);
        return isExcluded ? 0 : item.value;
      });
      
      // Calculate total only from active items
      const total = composition.reduce((sum, item) => {
        const matchingRow = rows.find(r => r.category === item.label);
        const isExcluded = matchingRow && excludedRows.has(matchingRow.id);
        return isExcluded ? sum : sum + item.value;
      }, 0);
      
      // Calculate net margin percentage
      const netMarginPct = totalRevenue && totalSpend && totalRevenue > 0 
        ? Math.round(((totalRevenue - totalSpend) / totalRevenue) * 100)
        : 0;
      
      profitChartInstance.current = new Chart(ctx, {
        type: 'doughnut',
        data: {
          labels: labels,
          datasets: [{
            data: data,
            backgroundColor: [
              'rgba(6, 182, 212, 0.8)',   // Cyan
              'rgba(34, 211, 238, 0.8)',  // Light Cyan
              'rgba(59, 130, 246, 0.8)',  // Blue
              'rgba(99, 102, 241, 0.8)',  // Indigo
              'rgba(139, 92, 246, 0.8)',  // Purple
              'rgba(168, 85, 247, 0.8)',  // Purple Light
              'rgba(236, 72, 153, 0.8)'   // Pink
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
              display: false // Hide the Chart.js legend
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
                  const percentage = ((value / total) * 100).toFixed(1);
                  return context.label + ': $' + value.toLocaleString(undefined, { maximumFractionDigits: 0 }) + ' (' + percentage + '%)';
                }
              }
            }
          }
        },
        plugins: [{
          beforeDraw: function(chart) {
            const { ctx, chartArea } = chart;
            if (!chartArea) return;
            
            const centerX = (chartArea.left + chartArea.right) / 2;
            const centerY = (chartArea.top + chartArea.bottom) / 2;
            
            ctx.save();
            const fontSize = ((chartArea.bottom - chartArea.top) / 160).toFixed(2);
            
            // Draw "Margin" text
            ctx.font = fontSize + "em sans-serif";
            ctx.textAlign = "center";
            ctx.textBaseline = "middle";
            ctx.fillStyle = "#06B6D4";
            ctx.fillText("Margin", centerX, centerY - 20);
            
            // Draw percentage
            ctx.font = "bold " + (fontSize * 2) + "em sans-serif";
            ctx.fillStyle = "#0B0B0B";
            ctx.fillText(netMarginPct + "%", centerX, centerY + 25);
            
            ctx.restore();
          }
        }]
      });
    }

    // Revenue Chart
    if (revenueChartRef.current && timeseries && timeseries.length > 0) {
      const ctx = revenueChartRef.current.getContext('2d');
      
      if (revenueChartInstance.current) {
        revenueChartInstance.current.destroy();
      }
      
      // Process timeseries data for revenue chart
      const labels = timeseries.map(d => {
        const date = new Date(d.date);
        return date.toLocaleDateString('en-US', { month: 'short', day: 'numeric' });
      });
      const revenueData = timeseries.map(d => d.revenue || 0);
      
      revenueChartInstance.current = new Chart(ctx, {
        type: 'bar',
        data: {
          labels: labels,
          datasets: [{
            label: 'Revenue',
            data: revenueData,
            backgroundColor: 'rgba(6, 182, 212, 0.7)',
            borderColor: 'rgba(6, 182, 212, 1)',
            borderWidth: 1,
            borderRadius: 8,
            hoverBackgroundColor: 'rgba(6, 182, 212, 0.9)'
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          interaction: {
            mode: 'index',
            intersect: false
          },
          plugins: {
            legend: {
              display: false
            },
            tooltip: {
              backgroundColor: 'rgba(255, 255, 255, 0.95)',
              titleColor: '#0B0B0B',
              bodyColor: '#0B0B0B',
              borderColor: 'rgba(6, 182, 212, 0.2)',
              borderWidth: 1,
              padding: 12,
              displayColors: false,
              callbacks: {
                label: function(context) {
                  return 'Revenue: $' + context.parsed.y.toLocaleString(undefined, { maximumFractionDigits: 0 });
                }
              }
            }
          },
          scales: {
            x: {
              grid: {
                display: false
              },
              ticks: {
                font: { size: 11 },
                color: '#6B7280'
              }
            },
            y: {
              beginAtZero: true,
              grid: {
                color: 'rgba(0, 0, 0, 0.05)',
                drawBorder: false
              },
              ticks: {
                font: { size: 11 },
                color: '#6B7280',
                callback: function(value) {
                  return '$' + (value / 1000).toFixed(0) + 'K';
                }
              }
            }
          }
        }
      });
    }

    return () => {
      if (profitChartInstance.current) {
        profitChartInstance.current.destroy();
      }
      if (revenueChartInstance.current) {
        revenueChartInstance.current.destroy();
      }
    };
  }, [composition, timeseries, totalRevenue, totalSpend, excludedRows, rows, onRowToggle]);

  return (
    <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-8">
      {/* Revenue Chart */}
      {timeseries && timeseries.length > 0 && (
        <div className="bg-white rounded-3xl border border-black/5 shadow-xl p-8 relative overflow-hidden fade-up-in" style={{ animationDelay: '500ms' }}>
          <div className="absolute -bottom-10 -right-10 w-40 h-40 bg-cyan-400 rounded-full blur-[100px] opacity-15 pulse-glow-aura" style={{ animationDelay: '2.5s' }}></div>
          <h3 className="text-lg font-semibold text-black mb-6">Revenue</h3>
          <div className="h-64 relative">
            <canvas ref={revenueChartRef}></canvas>
          </div>
          <div className="mt-4 flex items-center justify-center">
            <p className="text-sm text-neutral-500">
              Revenue: <span className="font-semibold text-black">${(timeseries.reduce((sum, d) => sum + (d.revenue || 0), 0) / 1000).toFixed(0)}K</span>
            </p>
          </div>
        </div>
      )}
      
      {/* Spend Composition Chart */}
      {composition && composition.length > 0 && (
        <div className="bg-white rounded-3xl border border-black/5 shadow-xl p-8 relative overflow-hidden fade-up-in" style={{ animationDelay: '600ms' }}>
          <div className="absolute -bottom-10 -right-10 w-40 h-40 bg-cyan-400 rounded-full blur-[100px] opacity-15 pulse-glow-aura" style={{ animationDelay: '3s' }}></div>
          <h3 className="text-lg font-semibold text-black mb-6 text-center">Spend Composition</h3>
          <div className="h-64 flex items-center justify-center">
            <div className="w-full h-full max-w-sm mx-auto">
              <canvas ref={profitChartRef}></canvas>
            </div>
          </div>
          
          {/* Custom Legend */}
          <div className="mt-6 flex flex-wrap justify-center gap-3">
            {composition.map((item, index) => {
              const matchingRow = rows.find(r => r.category === item.label);
              const isExcluded = matchingRow && excludedRows.has(matchingRow.id);
              const colors = [
                'rgba(6, 182, 212, 0.8)',   // Cyan
                'rgba(34, 211, 238, 0.8)',  // Light Cyan
                'rgba(59, 130, 246, 0.8)',  // Blue
                'rgba(99, 102, 241, 0.8)',  // Indigo
                'rgba(139, 92, 246, 0.8)',  // Purple
                'rgba(168, 85, 247, 0.8)',  // Purple Light
                'rgba(236, 72, 153, 0.8)'   // Pink
              ];
              const color = colors[index % colors.length];
              
              return (
                <div key={item.label} className={`flex items-center gap-2 ${isExcluded ? 'opacity-40' : ''}`}>
                  <div 
                    className="w-3 h-3 rounded-full" 
                    style={{ backgroundColor: isExcluded ? 'rgba(156, 163, 175, 0.5)' : color }}
                  />
                  <span className={`text-sm ${isExcluded ? 'line-through text-gray-400' : 'text-gray-700'}`}>
                    {item.label}
                  </span>
                </div>
              );
            })}
          </div>
        </div>
      )}
    </div>
  );
}
