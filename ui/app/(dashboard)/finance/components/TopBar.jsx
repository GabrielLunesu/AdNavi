/**
 * Finance Page Top Bar
 * 
 * WHAT: Period selector and comparison toggle
 * WHY: Controls which data is displayed in Finance page
 * REFERENCES: app/(dashboard)/finance/page.jsx
 */

"use client";
import { useState, useEffect, useRef } from "react";
import { Download, ChevronDown } from "lucide-react";

export default function TopBar({ selectedPeriod, onPeriodChange, compareEnabled, onCompareToggle }) {
  const [isDropdownOpen, setIsDropdownOpen] = useState(false);
  const dropdownRef = useRef(null);
  
  // Handle click outside to close dropdown
  useEffect(() => {
    function handleClickOutside(event) {
      if (dropdownRef.current && !dropdownRef.current.contains(event.target)) {
        setIsDropdownOpen(false);
      }
    }
    
    if (isDropdownOpen) {
      document.addEventListener('mousedown', handleClickOutside);
      return () => document.removeEventListener('mousedown', handleClickOutside);
    }
  }, [isDropdownOpen]);
  
  // Generate all period options
  const periods = [];
  const now = new Date();
  const monthNames = ["January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"];
  
  // Generate last 12 months
  for (let i = 0; i < 12; i++) {
    const date = new Date(now.getFullYear(), now.getMonth() - i, 1);
    periods.push({
      year: date.getFullYear(),
      month: date.getMonth() + 1,
      label: i === 0 ? 'This Month' : i === 1 ? 'Last Month' : `${monthNames[date.getMonth()]} ${date.getFullYear()}`,
      isMain: i <= 1 // First two are main options
    });
  }

  const handlePeriodClick = (period) => {
    onPeriodChange?.({ year: period.year, month: period.month });
    setIsDropdownOpen(false);
  };
  
  const isSelected = (period) => {
    return selectedPeriod.year === period.year && selectedPeriod.month === period.month;
  };
  
  const getCurrentLabel = () => {
    const current = periods.find(p => isSelected(p));
    return current?.label || 'Select Period';
  };

  return (
    <div className="sticky top-6 z-30 mb-8">
      <div className="glass-bar rounded-3xl border border-black/5 shadow-2xl p-8 relative overflow-hidden">
        {/* Cyan divider glow */}
        <div className="absolute bottom-0 left-0 right-0 h-0.5 bg-gradient-to-r from-transparent via-cyan-400 to-transparent opacity-40"></div>
        
        <div className="flex items-center justify-between mb-6">
          <div>
            <h1 className="text-4xl font-semibold tracking-tight text-black">Finance & P&L Overview</h1>
            <div className="h-0.5 w-24 bg-gradient-to-r from-cyan-400 to-transparent mt-3"></div>
          </div>
          
          <div className="flex items-center gap-3">
            {/* Period Selector */}
            <div className="flex items-center gap-2">
              {/* Main buttons - This Month, Last Month */}
              <div className="flex items-center gap-2 px-1 py-1 rounded-full bg-white/60 border border-black/5">
                {periods.filter(p => p.isMain).map((period, idx) => (
                  <button
                    key={idx}
                    onClick={() => handlePeriodClick(period)}
                    className={`px-5 py-2 rounded-full text-sm font-medium transition-all ${
                      isSelected(period)
                        ? 'bg-white text-cyan-600 border border-cyan-400/40 shadow-sm'
                        : 'text-neutral-600 hover:bg-white'
                    }`}
                  >
                    {period.label}
                  </button>
                ))}
              </div>
              
              {/* Dropdown for other months */}
              <div className="relative" ref={dropdownRef}>
                <button
                  onClick={() => setIsDropdownOpen(!isDropdownOpen)}
                  className={`px-4 py-2 rounded-full text-sm font-medium transition-all flex items-center gap-2 ${
                    periods.some(p => !p.isMain && isSelected(p))
                      ? 'bg-white text-cyan-600 border border-cyan-400/40 shadow-sm'
                      : 'bg-white/60 text-neutral-600 hover:bg-white border border-black/5'
                  }`}
                >
                  {periods.some(p => !p.isMain && isSelected(p)) ? getCurrentLabel() : 'Other months'}
                  <ChevronDown className={`w-4 h-4 transition-transform ${isDropdownOpen ? 'rotate-180' : ''}`} />
                </button>
                
                {isDropdownOpen && (
                  <div className="absolute top-full mt-2 right-0 w-64 glass-card rounded-2xl border border-black/5 shadow-xl p-2 max-h-80 overflow-y-auto">
                    {periods.filter(p => !p.isMain).map((period, idx) => (
                      <button
                        key={idx}
                        onClick={() => handlePeriodClick(period)}
                        className={`w-full text-left px-4 py-2 rounded-xl text-sm font-medium transition-all ${
                          isSelected(period)
                            ? 'bg-cyan-50 text-cyan-600'
                            : 'text-neutral-600 hover:bg-neutral-50'
                        }`}
                      >
                        {period.label}
                      </button>
                    ))}
                  </div>
                )}
              </div>
            </div>
            
            {/* Export Button */}
            <button className="px-5 py-2.5 rounded-full bg-black text-white text-sm font-medium border border-cyan-400/40 shadow-lg shadow-cyan-500/20 hover:shadow-cyan-500/40 transition-all flex items-center gap-2 relative overflow-hidden group">
              <span className="relative z-10">Export</span>
              <Download className="w-4 h-4 relative z-10" strokeWidth={1.5} />
              <div className="absolute inset-0 bg-gradient-to-r from-transparent via-cyan-400/20 to-transparent shimmer-effect opacity-0 group-hover:opacity-100"></div>
            </button>
          </div>
        </div>
        
        {/* Comparison Toggle */}
        <div className="flex items-center gap-3">
          <label className="flex items-center gap-3 cursor-pointer group">
            <div className="relative w-12 h-6 bg-white/60 rounded-full border border-black/5 transition-all">
              <input
                type="checkbox"
                className="sr-only peer"
                checked={compareEnabled}
                onChange={(e) => onCompareToggle?.(e.target.checked)}
              />
              <div className={`absolute top-0.5 left-0.5 w-5 h-5 bg-cyan-500 rounded-full transition-all shadow-sm ${compareEnabled ? 'translate-x-6' : ''}`}></div>
            </div>
            <span className="text-sm font-medium text-neutral-600 group-hover:text-black transition-all">Compare vs previous period</span>
          </label>
        </div>
      </div>
    </div>
  );
}
