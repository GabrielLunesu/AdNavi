"use client";
import { useState, useEffect } from "react";

export default function ManualCostModal({ open, onClose, onSubmit, defaultMonth, defaultYear, editingCost = null }) {
  const [label, setLabel] = useState("");
  const [category, setCategory] = useState("Tools / SaaS");
  const [amount, setAmount] = useState("");
  const [date, setDate] = useState("");
  const [notes, setNotes] = useState("");

  useEffect(() => {
    if (!open) return;
    
    if (editingCost) {
      // Pre-fill form with existing cost data
      setLabel(editingCost.label || "");
      setCategory(editingCost.category || "Tools / SaaS");
      setAmount(editingCost.amount_dollar?.toString() || "");
      setNotes(editingCost.notes || "");
      
      // Extract date from allocation or notes
      if (editingCost.allocation?.date) {
        setDate(editingCost.allocation.date);
      } else {
        // Prefill with selected month's start date
        const start = new Date(defaultYear, defaultMonth - 1, 1);
        const toIso = (d) => d.toISOString().slice(0, 10);
        setDate(toIso(start));
      }
    } else {
      // Reset form for new cost
      setLabel("");
      setCategory("Tools / SaaS");
      setAmount("");
      setNotes("");
      
      // Prefill date based on selected month
      if (defaultMonth && defaultYear) {
        const start = new Date(defaultYear, defaultMonth - 1, 1);
        const toIso = (d) => d.toISOString().slice(0, 10);
        setDate(toIso(start));
      }
    }
  }, [open, defaultMonth, defaultYear, editingCost]);

  if (!open) return null;

  const handleSubmit = (e) => {
    e.preventDefault();
    // For now, we'll create costs without dates since the backend has issues
    const payload = {
      label: label.trim(),
      category,
      amount_dollar: parseFloat(amount || 0),
      allocation: {
        type: "one_off"
        // Omitting date fields due to backend validation issues
      },
      notes: notes.trim() ? `${notes.trim()} (Date: ${date})` : `Date: ${date}`
    };
    onSubmit?.(payload);
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/40">
      <div className="bg-white w-full max-w-lg rounded-3xl border border-black/5 shadow-2xl overflow-hidden">
        <div className="px-6 py-5 border-b border-black/5 flex items-center justify-between">
          <h3 className="text-lg font-semibold text-black">{editingCost ? 'Edit' : 'Add'} Manual Cost</h3>
          <button onClick={onClose} className="text-neutral-500 hover:text-black text-sm">Close</button>
        </div>
        <form onSubmit={handleSubmit} className="p-6 space-y-4">
          <div>
            <label className="block text-xs font-medium text-neutral-600 mb-1">Label</label>
            <input value={label} onChange={(e) => setLabel(e.target.value)} required className="w-full px-4 py-2 rounded-2xl border border-neutral-200 text-sm focus:outline-none focus:border-cyan-400 focus:ring-2 focus:ring-cyan-400/20" placeholder="HubSpot, Agency Retainer" />
          </div>
          <div>
            <label className="block text-xs font-medium text-neutral-600 mb-1">Category</label>
            <select value={category} onChange={(e) => setCategory(e.target.value)} className="w-full px-4 py-2 rounded-2xl border border-neutral-200 text-sm focus:outline-none focus:border-cyan-400 focus:ring-2 focus:ring-cyan-400/20">
              <option>Tools / SaaS</option>
              <option>Agency Fees</option>
              <option>Events</option>
              <option>Ad Spend - Other</option>
              <option>Miscellaneous</option>
            </select>
          </div>
          <div>
            <label className="block text-xs font-medium text-neutral-600 mb-1">Amount (USD)</label>
            <input type="number" step="0.01" min="0" value={amount} onChange={(e) => setAmount(e.target.value)} required className="w-full px-4 py-2 rounded-2xl border border-neutral-200 text-sm focus:outline-none focus:border-cyan-400 focus:ring-2 focus:ring-cyan-400/20" placeholder="0.00" />
          </div>
          <div>
            <label className="block text-xs font-medium text-neutral-600 mb-1">Date</label>
            <input type="date" value={date} onChange={(e) => setDate(e.target.value)} required className="w-full px-4 py-2 rounded-2xl border border-neutral-200 text-sm focus:outline-none focus:border-cyan-400 focus:ring-2 focus:ring-cyan-400/20" />
          </div>
          <div>
            <label className="block text-xs font-medium text-neutral-600 mb-1">Notes</label>
            <textarea value={notes} onChange={(e) => setNotes(e.target.value)} rows={3} className="w-full px-4 py-2 rounded-2xl border border-neutral-200 text-sm focus:outline-none focus:border-cyan-400 focus:ring-2 focus:ring-cyan-400/20" placeholder="Optional"></textarea>
          </div>

          <div className="flex items-center justify-end gap-3 pt-2">
            <button type="button" onClick={onClose} className="px-4 py-2 rounded-2xl bg-neutral-100 text-neutral-700 text-sm hover:bg-neutral-200">Cancel</button>
            <button type="submit" className="px-5 py-2 rounded-2xl bg-cyan-500 text-white text-sm font-semibold hover:bg-cyan-600">
              {editingCost ? 'Update Cost' : 'Add Cost'}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}


