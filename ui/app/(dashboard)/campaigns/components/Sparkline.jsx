"use client";
import { useEffect, useRef } from "react";
import { Chart, registerables } from "chart.js";

Chart.register(...registerables);

export default function Sparkline({ data }) {
  const canvasRef = useRef(null);
  const chartInstance = useRef(null);

  useEffect(() => {
    if (canvasRef.current) {
      const ctx = canvasRef.current.getContext('2d');
      
      if (chartInstance.current) {
        chartInstance.current.destroy();
      }
      
      chartInstance.current = new Chart(ctx, {
        type: 'line',
        data: {
          labels: Array(data.length).fill(''),
          datasets: [{
            data: data,
            borderColor: '#06B6D4',
            backgroundColor: 'rgba(6, 182, 212, 0.1)',
            borderWidth: 2,
            fill: true,
            tension: 0.4,
            pointRadius: 0,
            pointHoverRadius: 4,
            pointHoverBackgroundColor: '#06B6D4'
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: {
            legend: { display: false },
            tooltip: {
              enabled: true,
              backgroundColor: 'rgba(255, 255, 255, 0.95)',
              titleColor: '#0B0B0B',
              bodyColor: '#06B6D4',
              borderColor: 'rgba(6, 182, 212, 0.2)',
              borderWidth: 1,
              padding: 8,
              displayColors: false,
              callbacks: {
                label: function(context) {
                  return context.parsed.y.toFixed(2) + 'x';
                },
                title: function() {
                  return '';
                }
              }
            }
          },
          scales: {
            x: { display: false },
            y: { display: false }
          }
        }
      });
    }

    return () => {
      if (chartInstance.current) {
        chartInstance.current.destroy();
      }
    };
  }, [data]);

  return (
    <div className="sparkline-container">
      <canvas ref={canvasRef}></canvas>
    </div>
  );
}

