// Minimal homepage with a CTA to open the dashboard
"use client";
import Link from "next/link";
import { useState } from "react";
import { login, register } from "../lib/auth";
import { useRouter } from "next/navigation";

export default function HomePage() {
  const [mode, setMode] = useState("login");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const router = useRouter();

  const onSubmit = async (e) => {
    e.preventDefault();
    setError("");
    try {
      if (mode === "login") {
        await login(email, password);
        router.push("/dashboard");
      } else {
        await register(email, password);
        setMode("login");
      }
    } catch (err) {
      setError(err.message || "Something went wrong");
    }
  };
  return (
    <main className="min-h-screen grid place-items-center p-8">
      <div className="text-center space-y-6 w-full max-w-md">
        {/* App title */}
        <h1 className="text-4xl md:text-5xl font-semibold tracking-tight gradient-text">AdNavi</h1>
        {/* Auth card */}
        <div className="glass-card border border-neutral-200/60 rounded-3xl p-6 text-left shadow-lg">
          <div className="flex gap-4 mb-4">
            <button
              onClick={() => setMode("login")}
              className={`px-3 py-1.5 rounded-full text-sm ${mode === "login" ? "bg-cyan-500 text-white" : "bg-neutral-100 text-neutral-700"}`}
            >
              Login
            </button>
            <button
              onClick={() => setMode("register")}
              className={`px-3 py-1.5 rounded-full text-sm ${mode === "register" ? "bg-cyan-500 text-white" : "bg-neutral-100 text-neutral-700"}`}
            >
              Register
            </button>
          </div>
          <form onSubmit={onSubmit} className="space-y-3">
            <input
              type="email"
              required
              placeholder="email@example.com"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className="w-full rounded-2xl bg-white border border-neutral-200 px-4 py-3 text-neutral-900 placeholder:text-neutral-400 focus:outline-none focus:border-cyan-400"
            />
            <input
              type="password"
              required
              minLength={8}
              placeholder="password (min 8 chars)"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="w-full rounded-2xl bg-white border border-neutral-200 px-4 py-3 text-neutral-900 placeholder:text-neutral-400 focus:outline-none focus:border-cyan-400"
            />
            {error && <div className="text-red-600 text-sm">{error}</div>}
            <button type="submit" className="w-full rounded-2xl bg-cyan-500 text-white px-4 py-3 font-medium hover:bg-cyan-600 transition-colors">
              {mode === "login" ? "Sign in" : "Create account"}
            </button>
          </form>
        </div>
        <div>
          <Link href="/dashboard" className="text-cyan-600 hover:text-cyan-700 underline">
            Go to dashboard
          </Link>
        </div>
      </div>
    </main>
  );
}
