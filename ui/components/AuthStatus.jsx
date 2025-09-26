"use client";

import { useEffect, useState } from "react";
import { currentUser, logout } from "../lib/auth";
import { useRouter } from "next/navigation";

export default function AuthStatus() {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const router = useRouter();

  useEffect(() => {
    let mounted = true;
    currentUser()
      .then((u) => mounted && setUser(u))
      .finally(() => mounted && setLoading(false));
    return () => {
      mounted = false;
    };
  }, []);

  const onLogout = async () => {
    await logout();
    setUser(null);
    router.push("/");
  };

  return (
    <div className="fixed top-3 left-3 z-50 text-sm bg-slate-900/70 border border-slate-700 rounded-full px-3 py-1.5 backdrop-blur">
      {loading ? (
        <span className="text-slate-400">Checking auth…</span>
      ) : user ? (
        <div className="flex items-center gap-3">
          <span className="text-slate-300">Signed in as {user.email}</span>
          <button onClick={onLogout} className="text-cyan-300 hover:text-cyan-200 underline">
            Logout
          </button>
        </div>
      ) : (
        <a href="/" className="text-cyan-300 hover:text-cyan-200 underline">
          Sign in
        </a>
      )}
    </div>
  );
}



