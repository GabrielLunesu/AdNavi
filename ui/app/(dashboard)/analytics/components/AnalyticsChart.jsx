"use client";
import { useEffect, useRef, useState } from "react";
import { Chart, registerables } from "chart.js";
import { fetchWorkspaceKpis, fetchWorkspaceCampaigns } from "@/lib/api";
import { ChevronDown } from "lucide-react";

Chart.register(...registerables);

const METRIC_OPTIONS = [
  { value: 'revenue', label: 'Revenue' },
  { value: 'spend', label: 'Spend' },
  { value: 'roas', label: 'ROAS' },
  { value: 'clicks', label: 'Clicks' },
  { value: 'conversions', label: 'Conversions' },
  { value: 'impressions', label: 'Impressions' },
  { value: 'ctr', label: 'CTR' },
  { value: 'cpc', label: 'CPC' }
];

const GROUPING_OPTIONS = [
  { value: 'provider', label: 'By Provider' },
  { value: 'campaign', label: 'By Campaign' }
];

export default function AnalyticsChart({
  workspaceId,
  selectedProvider,
  rangeDays,
  customStartDate,
  customEndDate,
  selectedMetric,
  setSelectedMetric,
  selectedGrouping,
  setSelectedGrouping,
  selectedCampaign,
  setSelectedCampaign
}) {
  const chartRef = useRef(null);
  const chartInstance = useRef(null);
  const [chartData, setChartData] = useState(null);
  const [campaigns, setCampaigns] = useState([]);
  const [loading, setLoading] = useState(true);
  const [showMetricDropdown, setShowMetricDropdown] = useState(false);
  const [showGroupingDropdown, setShowGroupingDropdown] = useState(false);
  const [showCampaignDropdown, setShowCampaignDropdown] = useState(false);

  // Fetch campaigns when grouping is 'campaign' or provider changes
  useEffect(() => {
    if (!workspaceId || selectedGrouping !== 'campaign') return;

    let mounted = true;
    
    fetchWorkspaceCampaigns({ 
      workspaceId, 
      provider: selectedProvider === 'all' ? null : selectedProvider,
      status: 'active' 
    })
      .then((data) => {
        if (!mounted) return;
        setCampaigns(data.campaigns || []);
        // Auto-select first campaign if none selected
        if (!selectedCampaign && data.campaigns && data.campaigns.length > 0) {
          setSelectedCampaign(data.campaigns[0].id);
        }
      })
      .catch((err) => {
        console.error('Failed to fetch campaigns:', err);
      });
    
    return () => { mounted = false; };
  }, [workspaceId, selectedGrouping, selectedProvider, selectedCampaign, setSelectedCampaign]);

  // Fetch chart data
  useEffect(() => {
    if (!workspaceId) return;

    let mounted = true;
    setLoading(true);

    // Find the selected campaign's name
    const selectedCampaignName = selectedCampaign && campaigns.length > 0
      ? campaigns.find(c => c.id === selectedCampaign)?.name
      : null;

    const params = {
      workspaceId,
      metrics: [selectedMetric],
      lastNDays: rangeDays,
      provider: selectedProvider === 'all' ? null : selectedProvider,
      compareToPrevious: false,
      sparkline: true,
      customStartDate: customStartDate || null,
      customEndDate: customEndDate || null,
      entityName: selectedGrouping === 'campaign' && selectedCampaignName ? selectedCampaignName : null
    };

    // Add breakdown based on grouping (not needed when filtering to specific campaign)
    if (selectedGrouping === 'provider') {
      params.breakdown = 'provider';
    }

    fetchWorkspaceKpis(params)
      .then((data) => {
        if (!mounted) return;
        setChartData(data[0]); // First metric
        setLoading(false);
      })
      .catch((err) => {
        console.error('Failed to fetch chart data:', err);
        if (mounted) setLoading(false);
      });

    return () => { mounted = false; };
  }, [workspaceId, selectedProvider, rangeDays, selectedMetric, selectedGrouping, selectedCampaign, campaigns, customStartDate, customEndDate]);

  // Render chart
  useEffect(() => {
    if (!chartRef.current || !chartData || loading) return;

    const ctx = chartRef.current.getContext('2d');

    if (chartInstance.current) {
      chartInstance.current.destroy();
    }

    // Prepare labels and data
    let labels = [];
    let datasets = [];

    if (selectedGrouping === 'provider' && chartData.sparkline) {
      // Show timeline with sparkline data
      labels = chartData.sparkline.map(sp => {
        const date = new Date(sp.date);
        return date.toLocaleDateString('en-US', { month: 'short', day: 'numeric' });
      });
      
      datasets = [{
        label: METRIC_OPTIONS.find(m => m.value === selectedMetric)?.label || selectedMetric,
        data: chartData.sparkline.map(sp => sp.value || 0),
        borderColor: '#06B6D4',
        backgroundColor: 'rgba(6, 182, 212, 0.1)',
        borderWidth: 2.5,
        tension: 0.4,
        fill: true,
        pointRadius: 4,
        pointHoverRadius: 6,
        pointBackgroundColor: '#06B6D4',
        pointBorderColor: '#fff',
        pointBorderWidth: 2
      }];
    } else if (selectedGrouping === 'campaign' && chartData.sparkline) {
      // Show timeline for campaign
      labels = chartData.sparkline.map(sp => {
        const date = new Date(sp.date);
        return date.toLocaleDateString('en-US', { month: 'short', day: 'numeric' });
      });
      
      datasets = [{
        label: METRIC_OPTIONS.find(m => m.value === selectedMetric)?.label || selectedMetric,
        data: chartData.sparkline.map(sp => sp.value || 0),
        borderColor: '#06B6D4',
        backgroundColor: 'rgba(6, 182, 212, 0.1)',
        borderWidth: 2.5,
        tension: 0.4,
        fill: true,
        pointRadius: 4,
        pointHoverRadius: 6,
        pointBackgroundColor: '#06B6D4',
        pointBorderColor: '#fff',
        pointBorderWidth: 2
      }];
    }

    // Format value based on metric type
    const formatValue = (value) => {
      if (value === null || value === undefined) return 'N/A';
      
      if (['revenue', 'spend', 'cpc', 'cpa', 'cpm'].includes(selectedMetric)) {
        return '$' + value.toLocaleString(undefined, { maximumFractionDigits: 2 });
      } else if (['roas'].includes(selectedMetric)) {
        return value.toFixed(2) + 'x';
      } else if (['ctr', 'cvr'].includes(selectedMetric)) {
        return (value * 100).toFixed(2) + '%';
      } else {
        return value.toLocaleString(undefined, { maximumFractionDigits: 0 });
      }
    };

    chartInstance.current = new Chart(ctx, {
      type: 'line',
      data: { labels, datasets },
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
                return context.dataset.label + ': ' + formatValue(context.parsed.y);
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
                return formatValue(value);
              }
            }
          }
        }
      }
    });

    return () => {
      if (chartInstance.current) {
        chartInstance.current.destroy();
      }
    };
  }, [chartData, loading, selectedMetric, selectedGrouping]);

  return (
    <div className="px-8 mb-8">
      <div className="glass-card rounded-3xl p-8 border border-neutral-200/60 shadow-lg">
        {/* Header with Dropdowns */}
        <div className="flex items-center justify-between mb-6">
          <h3 className="text-lg font-semibold text-neutral-900">Trend Analysis</h3>
          
          <div className="flex items-center gap-3">
            {/* Metric Dropdown */}
            <div className="relative">
              <button
                onClick={() => setShowMetricDropdown(!showMetricDropdown)}
                className="flex items-center gap-2 px-4 py-2 rounded-full bg-neutral-100 hover:bg-neutral-200 text-neutral-700 text-sm font-medium transition-colors"
              >
                {METRIC_OPTIONS.find(m => m.value === selectedMetric)?.label || 'Select Metric'}
                <ChevronDown className="w-4 h-4" />
              </button>
              
              {showMetricDropdown && (
                <div className="absolute right-0 mt-2 w-48 bg-white rounded-2xl border border-neutral-200 shadow-xl py-2 z-20">
                  {METRIC_OPTIONS.map((option) => (
                    <button
                      key={option.value}
                      onClick={() => {
                        setSelectedMetric(option.value);
                        setShowMetricDropdown(false);
                      }}
                      className={`w-full text-left px-4 py-2 text-sm hover:bg-neutral-50 transition-colors ${
                        selectedMetric === option.value ? 'text-cyan-600 font-medium' : 'text-neutral-700'
                      }`}
                    >
                      {option.label}
                    </button>
                  ))}
                </div>
              )}
            </div>

            {/* Grouping Dropdown */}
            <div className="relative">
              <button
                onClick={() => setShowGroupingDropdown(!showGroupingDropdown)}
                className="flex items-center gap-2 px-4 py-2 rounded-full bg-neutral-100 hover:bg-neutral-200 text-neutral-700 text-sm font-medium transition-colors"
              >
                {GROUPING_OPTIONS.find(g => g.value === selectedGrouping)?.label || 'Group By'}
                <ChevronDown className="w-4 h-4" />
              </button>
              
              {showGroupingDropdown && (
                <div className="absolute right-0 mt-2 w-48 bg-white rounded-2xl border border-neutral-200 shadow-xl py-2 z-20">
                  {GROUPING_OPTIONS.map((option) => (
                    <button
                      key={option.value}
                      onClick={() => {
                        setSelectedGrouping(option.value);
                        setShowGroupingDropdown(false);
                      }}
                      className={`w-full text-left px-4 py-2 text-sm hover:bg-neutral-50 transition-colors ${
                        selectedGrouping === option.value ? 'text-cyan-600 font-medium' : 'text-neutral-700'
                      }`}
                    >
                      {option.label}
                    </button>
                  ))}
                </div>
              )}
            </div>

            {/* Campaign Dropdown (only shown when grouping by campaign) */}
            {selectedGrouping === 'campaign' && (
              <div className="relative">
                <button
                  onClick={() => setShowCampaignDropdown(!showCampaignDropdown)}
                  className="flex items-center gap-2 px-4 py-2 rounded-full bg-cyan-500 hover:bg-cyan-600 text-white text-sm font-medium transition-colors"
                >
                  {campaigns.find(c => c.id === selectedCampaign)?.name || 'Select Campaign'}
                  <ChevronDown className="w-4 h-4" />
                </button>
                
                {showCampaignDropdown && (
                  <div className="absolute right-0 mt-2 w-64 bg-white rounded-2xl border border-neutral-200 shadow-xl py-2 z-20 max-h-64 overflow-y-auto">
                    {campaigns.map((campaign) => (
                      <button
                        key={campaign.id}
                        onClick={() => {
                          setSelectedCampaign(campaign.id);
                          setShowCampaignDropdown(false);
                        }}
                        className={`w-full text-left px-4 py-2 text-sm hover:bg-neutral-50 transition-colors ${
                          selectedCampaign === campaign.id ? 'text-cyan-600 font-medium' : 'text-neutral-700'
                        }`}
                      >
                        {campaign.name}
                      </button>
                    ))}
                  </div>
                )}
              </div>
            )}
          </div>
        </div>

        {/* Chart Canvas */}
        <div className="h-80">
          {loading ? (
            <div className="flex items-center justify-center h-full">
              <div className="w-8 h-8 border-4 border-cyan-500 border-t-transparent rounded-full animate-spin"></div>
            </div>
          ) : (
            <canvas ref={chartRef}></canvas>
          )}
        </div>
      </div>
    </div>
  );
}


