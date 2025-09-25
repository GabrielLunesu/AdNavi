// Dashboard-scoped layout. Provides the shell (sidebar + content area).
import Sidebar from "../../components/Sidebar";

export default function DashboardLayout({ children }) {
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
