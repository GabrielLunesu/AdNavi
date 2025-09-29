'use client'

import Logo from "./Logo";
import SidebarSection from "./SidebarSection";
import NavItem from "./NavItem";
import WorkspaceSummary from "./WorkspaceSummary";
import { usePathname } from "next/navigation";
import { Home, BarChart3, MessageSquare, Banknote, Target, Settings } from "lucide-react";
import Link from "next/link";
import { useEffect, useState } from "react";
import { currentUser, logout } from "../lib/auth";

export default function Sidebar() {
  const pathname = usePathname();
  const [user, setUser] = useState(null);
  useEffect(() => {
    let mounted = true;
    currentUser().then((u) => mounted && setUser(u));
    return () => {
      mounted = false;
    };
  }, []);
  return (
    <aside className="h-full w-full max-w-[260px] p-6 border-r border-slate-800/60 bg-slate-950/60">
      {/* Brand */}
      <div className="mb-8">
        <Logo />
      </div>

      {/* Workspace summary */}
      <div className="mb-6">
        <WorkspaceSummary workspaceId={user?.workspace_id} />
      </div>

      {/* Auth pill */}
      {user && (
        <div className="mb-6 rounded-2xl border border-cyan-700/40 bg-cyan-950/20 p-3">
          <div className="flex items-center gap-3">
            <div className="flex items-center justify-center w-9 h-9 rounded-full bg-cyan-600 text-slate-950 font-semibold">
              {user.email?.charAt(0)?.toUpperCase() || "U"}
            </div>
            <div className="min-w-0">
              <div className="text-xs uppercase tracking-wide text-cyan-300/80">Signed in</div>
              <div className="text-sm font-medium text-cyan-200 truncate" title={user.email}>{user.email}</div>
            </div>
          </div>
          <div className="mt-3">
            <form action={async () => { await logout(); location.href = "/"; }}>
              <button
                type="submit"
                className="w-full rounded-full bg-cyan-500 text-slate-950 px-3 py-2 text-sm font-medium hover:bg-cyan-400 transition-colors"
              >
                Logout
              </button>
            </form>
          </div>
        </div>
      )}

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
