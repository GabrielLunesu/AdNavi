// Grouping section for sidebar content with a small label
export default function SidebarSection({ title, children }) {
  return (
    <section className="mb-6">
      {title ? (
        <h3 className="text-xs font-medium text-slate-400 mb-3 uppercase tracking-wide">
          {title}
        </h3>
      ) : null}
      <div className="space-y-2">{children}</div>
    </section>
  );
}
