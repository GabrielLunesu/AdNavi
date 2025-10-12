export default function PlatformBadge({ platform }) {
  const config = {
    meta: { color: 'bg-blue-500', letter: 'M', label: 'Meta' },
    google: { color: 'bg-red-500', letter: 'G', label: 'Google' },
    tiktok: { color: 'bg-black', letter: 'T', label: 'TikTok' },
  };

  // Normalize platform name to lowercase key
  const normalizedPlatform = platform?.toLowerCase().replace(/\s+ads?$/i, '').trim();
  const badge = config[normalizedPlatform] || { color: 'bg-slate-400', letter: platform?.[0]?.toUpperCase() || '?', label: platform };

  return (
    <span 
      className={`inline-flex items-center justify-center w-8 h-8 rounded-full ${badge.color} text-white text-xs font-semibold shadow-sm`}
      title={badge.label}
    >
      {badge.letter}
    </span>
  );
}
