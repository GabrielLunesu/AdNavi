"use client";
import { useState } from "react";
import { Edit2, Trash2 } from "lucide-react";

export default function ManualCostDropdown({ costs, onEdit, onDelete, onClose }) {
  const [deletingId, setDeletingId] = useState(null);

  const handleDelete = async (costId) => {
    if (deletingId) return;
    if (!confirm("Are you sure you want to delete this cost?")) return;
    
    setDeletingId(costId);
    try {
      await onDelete(costId);
    } finally {
      setDeletingId(null);
    }
  };

  if (!costs || costs.length === 0) {
    return (
      <div className="absolute top-full left-0 mt-2 w-96 bg-white rounded-2xl border border-black/10 shadow-2xl p-4 z-50">
        <p className="text-sm text-neutral-500">No manual costs in this category</p>
      </div>
    );
  }

  return (
    <div className="absolute top-full left-0 mt-2 w-96 bg-white rounded-2xl border border-black/10 shadow-2xl overflow-hidden z-50">
      <div className="p-4 border-b border-black/5 bg-gradient-to-br from-cyan-50 to-white">
        <h4 className="text-sm font-semibold text-black">Manual Costs</h4>
        <p className="text-xs text-neutral-500 mt-0.5">{costs.length} {costs.length === 1 ? 'entry' : 'entries'}</p>
      </div>
      
      <div className="max-h-80 overflow-y-auto">
        {costs.map((cost) => (
          <div
            key={cost.id}
            className="p-4 border-b border-black/5 hover:bg-neutral-50 transition-colors group"
          >
            <div className="flex items-start justify-between mb-2">
              <div className="flex-1">
                <p className="text-sm font-medium text-black">{cost.label}</p>
                <p className="text-xs text-neutral-500 mt-0.5">{cost.category}</p>
              </div>
              <p className="text-sm font-semibold text-black ml-4">
                ${cost.amount_dollar.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 })}
              </p>
            </div>
            
            {cost.notes && (
              <p className="text-xs text-neutral-400 mb-2">{cost.notes}</p>
            )}
            
            <div className="flex items-center gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
              <button
                onClick={() => onEdit(cost)}
                className="flex items-center gap-1 px-3 py-1.5 rounded-lg bg-cyan-50 hover:bg-cyan-100 text-cyan-600 text-xs font-medium transition-colors"
              >
                <Edit2 className="w-3 h-3" />
                Edit
              </button>
              <button
                onClick={() => handleDelete(cost.id)}
                disabled={deletingId === cost.id}
                className="flex items-center gap-1 px-3 py-1.5 rounded-lg bg-red-50 hover:bg-red-100 text-red-600 text-xs font-medium transition-colors disabled:opacity-50"
              >
                <Trash2 className="w-3 h-3" />
                {deletingId === cost.id ? 'Deleting...' : 'Delete'}
              </button>
            </div>
          </div>
        ))}
      </div>
      
      <div className="p-3 bg-neutral-50 border-t border-black/5">
        <button
          onClick={onClose}
          className="w-full px-4 py-2 rounded-lg bg-white border border-neutral-200 text-neutral-700 text-sm font-medium hover:bg-neutral-100 transition-colors"
        >
          Close
        </button>
      </div>
    </div>
  );
}

