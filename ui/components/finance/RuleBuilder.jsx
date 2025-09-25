export default function RuleBuilder({ onSave, onCancel }) {
  const handleSave = () => {
    const metric = document.getElementById('rb-metric').value;
    const cond = document.getElementById('rb-cond').value;
    const value = document.getElementById('rb-value').value.trim();
    const range = document.getElementById('rb-range').value;
    if (!value) return;
    const metricLabel = { roas:'ROAS', conversions:'Conversions', spend:'Spend', revenue:'Revenue' }[metric] || metric;
    const condLabel = { '<':'<', '>':'>', drop_pct:'drop %', rise_pct:'rise %' }[cond] || cond;
    const label = `${metricLabel} ${condLabel} ${value}${range ? ` (${range})` : ''} → Notify`;
    onSave?.({ label });
  };
  return (
    <div className="rounded-xl p-3 border border-white/10 bg-slate-900/35 mb-3">
      <div className="grid grid-cols-12 gap-2 items-center">
        <select id="rb-metric" className="col-span-2 bg-transparent px-3 py-2 rounded-lg border border-white/10 text-sm">
          <option value="roas">ROAS</option>
          <option value="conversions">Conversions</option>
          <option value="spend">Spend</option>
          <option value="revenue">Revenue</option>
        </select>
        <select id="rb-cond" className="col-span-2 bg-transparent px-3 py-2 rounded-lg border border-white/10 text-sm">
          <option value="<">below</option>
          <option value=">">above</option>
          <option value="drop_pct">drop %</option>
          <option value="rise_pct">rise %</option>
        </select>
        <input id="rb-value" type="text" placeholder="Value (e.g. 1.5, 20%)" className="col-span-2 bg-transparent px-3 py-2 rounded-lg border border-white/10 text-sm" />
        <select id="rb-range" className="col-span-3 bg-transparent px-3 py-2 rounded-lg border border-white/10 text-sm">
          <option value="24h">24h</option>
          <option value="48h">48h</option>
          <option value="7d" selected>7d</option>
          <option value="30d">30d</option>
        </select>
        <div className="col-span-2 px-3 py-2 rounded-lg border border-white/10 text-slate-300 text-sm">Channel: In-app</div>
        <div className="col-span-1 flex items-center justify-end gap-2">
          <button onClick={handleSave} className="px-2.5 py-1.5 text-xs rounded-full bg-emerald-500/15 text-emerald-300 border border-emerald-400/20">Save</button>
          <button onClick={onCancel} className="px-2.5 py-1.5 text-xs rounded-full bg-rose-500/15 text-rose-300 border border-rose-400/20">Cancel</button>
        </div>
      </div>
    </div>
  );
}
