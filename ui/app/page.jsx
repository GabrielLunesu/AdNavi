// Minimal homepage with a CTA to open the dashboard
import Link from "next/link";

export default function HomePage() {
  return (
    <main className="min-h-screen grid place-items-center p-8">
      <div className="text-center space-y-6">
        {/* App title for quick identification */}
        <h1 className="text-4xl md:text-5xl font-semibold tracking-tight">AdNavi</h1>
        {/* Primary action: navigate to the dashboard route */}
        <Link
          href="/dashboard"
          className="inline-block rounded-full bg-cyan-500 text-slate-950 px-6 py-3 font-medium hover:bg-cyan-400 transition-colors"
        >
          Go to dashboard
        </Link>
      </div>
    </main>
  );
}
