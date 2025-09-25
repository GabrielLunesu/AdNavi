'use client'

import Logo from "./Logo";
import SidebarSection from "./SidebarSection";
import NavItem from "./NavItem";
import WorkspaceSummary from "./WorkspaceSummary";
import { usePathname } from "next/navigation";
import { Home, BarChart3, MessageSquare, Banknote, Target, Settings } from "lucide-react";

export default function Sidebar() {
  const pathname = usePathname();
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
        <NavItem href="/dashboard" label="Dashboard" icon={<Home size={16} />} active={pathname === "/dashboard"} />
        <NavItem href="/analytics" label="Analytics" icon={<BarChart3 size={16} />} active={pathname === "/analytics"} />
        <NavItem href="/copilot" label="Copilot" icon={<MessageSquare size={16} />} active={pathname?.startsWith('/copilot')} />
        <NavItem href="/finance" label="Finance (P&L)" icon={<Banknote size={16} />} active={pathname === "/finance"} />
        <NavItem href="/campaigns" label="Campaigns" icon={<Target size={16} />} active={pathname?.startsWith('/campaigns')} />
        <NavItem href="#" label="Settings" icon={<Settings size={16} />} active={false} />
      </SidebarSection>
    </aside>
  );
}
