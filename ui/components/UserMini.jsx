// Small user identity snippet for topbar/sidebar
export default function UserMini({ name = "Alex Morgan" }) {
  const initials = name
    .split(" ")
    .map((n) => n[0])
    .join("")
    .slice(0, 2)
    .toUpperCase();

  return (
    <div className="flex items-center gap-3">
      <div className="w-8 h-8 rounded-full bg-slate-800 text-slate-200 grid place-items-center text-xs font-medium">
        {initials}
      </div>
      <span className="text-sm text-slate-300">{name}</span>
    </div>
  );
}
