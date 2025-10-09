// Dashboard-scoped layout. Provides the shell (sidebar + content area).
"use client";
import Sidebar from "./dashboard/components/Sidebar";
import { useEffect, useState } from "react";
import { currentUser } from "../../lib/auth";

export default function DashboardLayout({ children }) {
  const [authed, setAuthed] = useState(null);

  useEffect(() => {
    let mounted = true;
    currentUser().then((u) => {
      if (!mounted) return;
      setAuthed(Boolean(u));
    });
    return () => {
      mounted = false;
    };
  }, []);

  if (authed === null) {
    return <div className="p-6">Checking authentication…</div>;
  }

  if (!authed) {
    return (
      <div className="min-h-screen grid place-items-center p-6">
        <div className="max-w-md w-full glass-card rounded-3xl border border-neutral-200/60 p-6 text-center">
          <h2 className="text-xl font-medium mb-2 text-neutral-900">You must be signed in.</h2>
          <a href="/" className="text-cyan-600 hover:text-cyan-700 underline">Go to sign in</a>
        </div>
      </div>
    );
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
