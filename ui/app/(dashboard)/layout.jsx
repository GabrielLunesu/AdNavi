// Dashboard-scoped layout. Provides the shell (sidebar + content area).
"use client";
import Sidebar from "./dashboard/components/Sidebar";
import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import { currentUser } from "../../lib/auth";

export default function DashboardLayout({ children }) {
  const [authed, setAuthed] = useState(null);
  const router = useRouter();

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
    <div className="flex min-h-screen">
      {/* Sidebar */}
      <Sidebar />

      {/* Main Content */}
      <main className="flex-1 ml-72 p-8 pt-12">
        <div className="max-w-7xl mx-auto">
          {children}
        </div>
      </main>
    </div>
  );
}
