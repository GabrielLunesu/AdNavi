// Dashboard-scoped layout. Provides the shell (sidebar + content area).
"use client";
import Sidebar from "./dashboard/components/Sidebar";
import FooterDashboard from "../../components/FooterDashboard";
import { useEffect, useState } from "react";
import { useRouter, usePathname } from "next/navigation";
import { currentUser } from "../../lib/auth";

export default function DashboardLayout({ children }) {
  const [authed, setAuthed] = useState(null);
  const router = useRouter();
  const pathname = usePathname();
  const immersive = pathname === "/canvas";

  useEffect(() => {
    let mounted = true;
    currentUser().then((u) => {
      if (!mounted) return;
      const isAuthed = Boolean(u);
      setAuthed(isAuthed);
      
      // Redirect to login if not authenticated
      if (!isAuthed) {
        router.push("/login");
      }
    });
    return () => {
      mounted = false;
    };
  }, [router]);

  // Show loading state while checking auth
  if (authed === null) {
    return (
      <div className="min-h-screen grid place-items-center p-6">
        <div className="text-center">
          <div className="w-12 h-12 border-4 border-cyan-500 border-t-transparent rounded-full animate-spin mx-auto mb-4"></div>
          <p className="text-neutral-600">Loading...</p>
        </div>
      </div>
    );
  }

  // Don't render dashboard if not authenticated (will redirect)
  if (!authed) {
    return null;
  }

  return (
    <div className="min-h-screen w-full bg-white relative overflow-hidden">
      {/* Blue Corner Glow Background */}
      <div
        className="absolute inset-0 z-0"
        style={{
          backgroundImage: `
            radial-gradient(circle 600px at 0% 200px, #bfdbfe, transparent),
            radial-gradient(circle 600px at 100% 200px, #bfdbfe, transparent)
          `,
        }}
      />

      {/* Dashboard Shell */}
      <div className={`flex min-h-screen relative z-10 ${immersive ? "" : ""}`}>
        {/* Sidebar */}
        {!immersive && <Sidebar />}

        {/* Main Content */}
        <main className={`flex-1 ${immersive ? "p-0" : "ml-72 p-8 pt-12"}`}>
          <div className={immersive ? "w-full" : "max-w-7xl mx-auto"}>
            {children}
            {!immersive && <FooterDashboard />}
          </div>
        </main>
      </div>
    </div>
  );
}
