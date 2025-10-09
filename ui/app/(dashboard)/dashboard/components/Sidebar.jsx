'use client'

import { usePathname } from "next/navigation";
import { Home, BarChart3, Bot, Receipt, Megaphone, Settings } from "lucide-react";
import { useEffect, useState } from "react";
import { currentUser, logout } from "../../../../lib/auth";

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

  const navItems = [
    { href: "/dashboard", label: "Dashboard", icon: Home, active: pathname === "/dashboard" },
    { href: "/analytics", label: "Analytics", icon: BarChart3, active: pathname === "/analytics" },
    { href: "/copilot", label: "Copilot", icon: Bot, active: pathname?.startsWith('/copilot') },
    { href: "/finance", label: "Finance (P&L)", icon: Receipt, active: pathname === "/finance" },
    { href: "/campaigns", label: "Campaigns", icon: Megaphone, active: pathname?.startsWith('/campaigns') },
    { href: "#", label: "Settings", icon: Settings, active: false },
  ];

  return (
    <aside className="fixed left-4 top-4 bottom-4 w-64 glass-sidebar rounded-3xl border border-neutral-200/60 shadow-xl flex flex-col p-6 z-50">
      {/* Brand */}
      <div className="mb-10">
        <h1 className="text-2xl font-semibold tracking-tight text-transparent bg-clip-text bg-gradient-to-r from-black to-cyan-600" style={{ letterSpacing: '-0.05em' }}>
          AdNavi
        </h1>
      </div>
      
      {/* Navigation */}
      <nav className="flex-1 space-y-2">
        {navItems.map((item) => {
          const Icon = item.icon;
          return (
            <a
              key={item.href}
              href={item.href}
              className={`flex items-center gap-3 px-4 py-3 rounded-2xl transition-all ${
                item.active
                  ? 'bg-white border border-cyan-400/40 text-cyan-600 shadow-sm shadow-cyan-500/20'
                  : 'text-neutral-600 hover:bg-white/60 hover:text-neutral-900'
              }`}
            >
              <Icon className="w-5 h-5" strokeWidth={1.5} />
              <span className="text-sm font-medium">{item.label}</span>
            </a>
          );
        })}
      </nav>
      
      {/* Bottom Section - Workspace */}
      <div className="mt-6 pt-6 border-t border-neutral-200/60">
        <div className="flex items-center gap-3 px-4 py-3 rounded-2xl bg-white/40 border border-neutral-200/60">
          <div className="w-8 h-8 rounded-full bg-gradient-to-br from-cyan-400 to-cyan-600 flex items-center justify-center text-white text-xs font-semibold">
            {user?.email?.charAt(0)?.toUpperCase() || "A"}
          </div>
          <div className="flex-1 min-w-0">
            <p className="text-sm font-medium text-neutral-900 truncate">Workspace</p>
            <p className="text-xs text-neutral-500 truncate">Pro Plan</p>
          </div>
        </div>
        {user && (
          <form action={async () => { await logout(); location.href = "/"; }} className="mt-3">
            <button
              type="submit"
              className="w-full rounded-2xl bg-neutral-100 hover:bg-neutral-200 text-neutral-700 px-4 py-2 text-sm font-medium transition-colors"
            >
              Logout
            </button>
          </form>
        )}
      </div>
    </aside>
  );
}

