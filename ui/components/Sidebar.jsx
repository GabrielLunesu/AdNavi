import Logo from "./Logo";
import SidebarSection from "./SidebarSection";
import NavItem from "./NavItem";
import WorkspaceSummary from "./WorkspaceSummary";

export default function Sidebar() {
  return (
    <aside className="h-full w-full max-w-[260px] p-6 border-r border-slate-800/60 bg-slate-950/60">
      {/* Brand */}
      <div className="mb-8">
        <Logo />
      </div>

      {/* Workspace summary */}
      <div className="mb-6">
        <WorkspaceSummary />
      </div>

      {/* Navigation */}
      <SidebarSection>
        <NavItem href="/dashboard" label="Dashboard" icon={<span aria-hidden>🏠</span>} active />
        <NavItem href="#" label="Analytics" icon={<span aria-hidden>📊</span>} />
        <NavItem href="#" label="Campaigns" icon={<span aria-hidden>🎯</span>} />
        <NavItem href="#" label="Settings" icon={<span aria-hidden>⚙️</span>} />
      </SidebarSection>
    </aside>
  );
}
