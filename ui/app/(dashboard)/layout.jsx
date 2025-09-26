// Dashboard-scoped layout. Provides the shell (sidebar + content area).
"use client";
import Sidebar from "../../components/Sidebar";
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
        <div className="max-w-md w-full bg-slate-900/60 border border-slate-700 rounded-xl p-6 text-center">
          <h2 className="text-xl font-medium mb-2">You must be signed in.</h2>
          <a href="/" className="text-cyan-300 hover:text-cyan-200 underline">Go to sign in</a>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen grid grid-cols-[260px_1fr]">
      {/* Sidebar */}
      <Sidebar />
      {/* Main content area; assistant lives inside the page */}
      <div className="flex flex-col">
        <main className="p-6">
          <div className="max-w-7xl mx-auto">
            {children}
          </div>
        </main>
      </div>
    </div>
  );
}
