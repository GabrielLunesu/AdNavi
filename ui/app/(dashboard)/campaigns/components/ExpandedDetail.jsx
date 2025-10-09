"use client";
import { useEffect, useRef } from "react";
import { Chart, registerables } from "chart.js";

Chart.register(...registerables);

function AdSetCard({ adSet }) {
  const canvasRef = useRef(null);
  const chartInstance = useRef(null);

  useEffect(() => {
    if (canvasRef.current && adSet.sparklineData) {
      const ctx = canvasRef.current.getContext('2d');
      
      if (chartInstance.current) {
        chartInstance.current.destroy();
      }
      
      chartInstance.current = new Chart(ctx, {
        type: 'line',
        data: {
          labels: Array(adSet.sparklineData.length).fill(''),
          datasets: [{
            data: adSet.sparklineData,
            borderColor: '#06B6D4',
            borderWidth: 1.5,
            tension: 0.4,
            pointRadius: 0
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: { legend: { display: false }, tooltip: { enabled: false } },
          scales: { x: { display: false }, y: { display: false } }
        }
      });
    }

    return () => {
      if (chartInstance.current) {
        chartInstance.current.destroy();
      }
    };
  }, [adSet.sparklineData]);

  return (
    <div className="glass-card rounded-2xl p-5 border border-neutral-200/60 hover:border-cyan-400/40 transition-all cursor-pointer relative overflow-hidden group">
      <div className="absolute bottom-0 left-0 right-0 h-0.5 bg-gradient-to-r from-transparent via-cyan-400 to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
      <div className="flex items-start justify-between mb-3">
        <p className="text-sm font-semibold text-neutral-900">{adSet.name}</p>
        <span className="inline-flex px-2 py-0.5 rounded-full text-xs font-medium pill-active">{adSet.status}</span>
      </div>
      <div className="space-y-2 mb-3">
        <div className="flex items-center justify-between">
          <span className="text-xs text-neutral-600">Spend</span>
          <span className="text-sm font-semibold text-neutral-900">${adSet.spend}</span>
        </div>
        <div className="flex items-center justify-between">
          <span className="text-xs text-neutral-600">ROAS</span>
          <span className="text-sm font-semibold text-cyan-600">{adSet.roas}x</span>
        </div>
      </div>
      <div className="h-8">
        <canvas ref={canvasRef}></canvas>
      </div>
    </div>
  );
}

export default function ExpandedDetail({ campaign }) {
  const chartRef = useRef(null);
  const chartInstance = useRef(null);

  useEffect(() => {
    if (chartRef.current && campaign.detailChartData) {
      const ctx = chartRef.current.getContext('2d');
      
      if (chartInstance.current) {
        chartInstance.current.destroy();
      }
      
      chartInstance.current = new Chart(ctx, {
        type: 'line',
        data: {
          labels: campaign.detailChartData.labels,
          datasets: [{
            label: 'ROAS',
            data: campaign.detailChartData.data,
            borderColor: '#06B6D4',
            backgroundColor: 'rgba(6, 182, 212, 0.1)',
            borderWidth: 2,
            fill: true,
            tension: 0.4,
            pointRadius: 3,
            pointHoverRadius: 5,
            pointBackgroundColor: '#06B6D4'
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: {
            legend: { display: false },
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
                  return 'ROAS: ' + context.parsed.y.toFixed(2) + 'x';
                }
              }
            }
          },
          scales: {
            x: {
              display: true,
              grid: { display: false },
              ticks: { color: '#A3A3A3', font: { size: 10 } }
            },
            y: {
              display: true,
              grid: { color: 'rgba(0, 0, 0, 0.05)' },
              ticks: { color: '#A3A3A3', font: { size: 10 } }
            }
          }
        }
      });
    }

    return () => {
      if (chartInstance.current) {
        chartInstance.current.destroy();
      }
    };
  }, [campaign.detailChartData]);

  return (
    <div className="expanded-section mt-6 pt-6 border-t border-neutral-200/40">
      <div className="grid grid-cols-12 gap-6">
        {/* Left: Summary */}
        <div className="col-span-5">
          <h4 className="text-sm font-semibold text-neutral-900 mb-4 uppercase tracking-wide">Campaign Summary</h4>
          <div className="space-y-3">
            <div className="flex items-center justify-between">
              <span className="text-sm text-neutral-600">Total Spend</span>
              <span className="text-sm font-semibold text-neutral-900">${campaign.spend.toLocaleString()}</span>
            </div>
            <div className="flex items-center justify-between">
              <span className="text-sm text-neutral-600">Total Revenue</span>
              <span className="text-sm font-semibold text-neutral-900">${campaign.revenue.toLocaleString()}</span>
            </div>
            <div className="flex items-center justify-between">
              <span className="text-sm text-neutral-600">ROAS</span>
              <span className="text-sm font-semibold text-cyan-600">{campaign.roas}x</span>
            </div>
            <div className="flex items-center justify-between">
              <span className="text-sm text-neutral-600">Conversions</span>
              <span className="text-sm font-semibold text-neutral-900">{campaign.conversions}</span>
            </div>
            <div className="flex items-center justify-between">
              <span className="text-sm text-neutral-600">CTR</span>
              <span className="text-sm font-semibold text-neutral-900">{campaign.ctr}%</span>
            </div>
          </div>
        </div>
        
        {/* Right: Chart */}
        <div className="col-span-7">
          <h4 className="text-sm font-semibold text-neutral-900 mb-4 uppercase tracking-wide">Last 14 Days</h4>
          <div className="h-40">
            <canvas ref={chartRef}></canvas>
          </div>
        </div>
      </div>
      
      {/* Ad Sets */}
      {campaign.adSets && campaign.adSets.length > 0 && (
        <div className="mt-8">
          <h4 className="text-sm font-semibold text-neutral-900 mb-4 uppercase tracking-wide">
            Ad Sets ({campaign.adSets.length})
          </h4>
          <div className="grid grid-cols-3 gap-4">
            {campaign.adSets.map((adSet, idx) => (
              <AdSetCard key={idx} adSet={adSet} />
            ))}
          </div>
        </div>
      )}
    </div>
  );
}

