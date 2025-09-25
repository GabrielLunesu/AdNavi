export default function PlatformBadge({ platform }) {
  const map = {
    'Meta Ads': { bg:'bg-sky-500/15', color:'text-sky-300', text:'M' },
    'Google Ads': { bg:'bg-amber-500/15', color:'text-amber-300', text:'G' },
    'TikTok Ads': { bg:'bg-fuchsia-500/15', color:'text-fuchsia-300', text:'T' },
    'LinkedIn Ads': { bg:'bg-blue-500/15', color:'text-blue-300', text:'L' },
  };
  const s = map[platform] || { bg:'bg-white/10', color:'text-slate-300', text:platform?.[0] || '?' };
  return (
    <span className={`inline-flex items-center justify-center w-6 h-6 rounded-md ${s.bg} ${s.color} text-xs`}>{s.text}</span>
  );
}
