export default function AddCostRow({ onSave, onCancel }) {
  const handleSave = () => {
    const name = document.getElementById('addc-name').value.trim();
    const amount = document.getElementById('addc-amount').value.trim();
    const start = document.getElementById('addc-start').value || null;
    const end = document.getElementById('addc-end').value || null;
    const notes = document.getElementById('addc-notes').value.trim();
    if (!name || !amount || !start) return;
    onSave?.({ name, amount, start, end, notes });
  };
  return (
    <div className="px-3 py-3">
      <div className="grid grid-cols-12 gap-2">
        <input id="addc-name" type="text" placeholder="Cost name" className="col-span-3 bg-transparent px-3 py-2 rounded-lg border border-white/10 text-sm" />
        <input id="addc-amount" type="text" placeholder="$300 or 2.9% or $1/conv" className="col-span-2 bg-transparent px-3 py-2 rounded-lg border border-white/10 text-sm" />
        <div className="col-span-3 grid grid-cols-2 gap-2">
          <input id="addc-start" type="date" className="bg-transparent px-3 py-2 rounded-lg border border-white/10 text-sm" />
          <input id="addc-end" type="date" className="bg-transparent px-3 py-2 rounded-lg border border-white/10 text-sm" />
        </div>
        <input id="addc-notes" type="text" placeholder="Notes (optional)" className="col-span-3 bg-transparent px-3 py-2 rounded-lg border border-white/10 text-sm" />
        <div className="col-span-1 flex items-center justify-end gap-2">
          <button onClick={handleSave} className="px-2.5 py-1.5 text-xs rounded-full bg-emerald-500/15 text-emerald-300 border border-emerald-400/20">Save</button>
          <button onClick={onCancel} className="px-2.5 py-1.5 text-xs rounded-full bg-rose-500/15 text-rose-300 border border-rose-400/20">Cancel</button>
        </div>
      </div>
    </div>
  );
}
