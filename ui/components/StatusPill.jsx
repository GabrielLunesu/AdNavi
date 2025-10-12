// WHAT: Reusable pill component to display entity status (Active/Paused).
// WHY: Centralizes status styling for consistency across UI tables.
// REFERENCES:
// - ui/components/campaigns/CampaignRow.jsx (consumer)
export default function StatusPill({ status }) {
  const isActive = status?.toLowerCase() === 'active';
  return (
    <span className={`text-xs px-2 py-1 rounded-full ${isActive ? 'bg-emerald-500/10 text-emerald-300 border border-emerald-400/20' : 'bg-amber-500/10 text-amber-300 border border-amber-400/20'}`}>
      {status}
    </span>
  );
}
