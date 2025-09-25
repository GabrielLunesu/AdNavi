// Global app layout. Provides HTML shell and imports global CSS.
// No dashboard chrome here; that lives in the dashboard layout.
import "./globals.css";

export const metadata = {
  title: "AdNavi",
  description: "AdNavi - AI Marketing Assistant",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className="min-h-screen bg-slate-950 text-slate-200 antialiased relative overflow-x-hidden">
        {/* Background gradient */}
        <div aria-hidden className="pointer-events-none absolute inset-0 bg-[radial-gradient(1200px_600px_at_50%_-20%,rgba(56,189,248,0.15),transparent),radial-gradient(900px_500px_at_20%_10%,rgba(167,139,250,0.12),transparent),radial-gradient(900px_500px_at_80%_20%,rgba(20,184,166,0.10),transparent)]" />
        {/* Floating subtle glow orbs */}
        <div aria-hidden className="pointer-events-none absolute w-40 h-40 rounded-full blur-3xl opacity-30 bg-cyan-400 top-20 left-1/4" />
        <div aria-hidden className="pointer-events-none absolute w-28 h-28 rounded-full blur-3xl opacity-25 bg-violet-400 top-64 right-1/3" />
        <div aria-hidden className="pointer-events-none absolute w-48 h-48 rounded-full blur-3xl opacity-20 bg-teal-400 bottom-32 left-1/2" />

        <div className="relative z-10">{children}</div>
      </body>
    </html>
  );
}
