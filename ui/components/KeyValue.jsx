// Label/value pair used in CompanyCard
export default function KeyValue({ label, children }) {
  return (
    <div className="flex items-start gap-2 text-sm">
      <span className="text-slate-400 w-28 shrink-0">{label}</span>
      <div className="text-slate-200">{children}</div>
    </div>
  );
}
