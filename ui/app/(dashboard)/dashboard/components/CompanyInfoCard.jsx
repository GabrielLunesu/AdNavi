export default function CompanyInfoCard() {
  return (
    <div className="glass-card rounded-3xl p-8 border border-neutral-200/60 shadow-lg">
      <div className="flex items-start justify-between mb-6">
        <h3 className="text-xl font-semibold text-neutral-900">Company Info</h3>
        <button className="text-sm font-medium text-cyan-600 hover:text-cyan-700 transition-colors">
          Edit Info
        </button>
      </div>
      <div className="space-y-4">
        <div>
          <p className="text-xs font-medium text-neutral-500 mb-1 uppercase tracking-wide">
            Company Name
          </p>
          <p className="text-base font-medium text-neutral-900">TechFlow Solutions</p>
        </div>
        <div>
          <p className="text-xs font-medium text-neutral-500 mb-1 uppercase tracking-wide">
            Website
          </p>
          <a
            href="#"
            className="text-base font-medium text-cyan-600 hover:text-cyan-700 transition-colors"
          >
            techflowsolutions.com
          </a>
        </div>
        <div>
          <p className="text-xs font-medium text-neutral-500 mb-1 uppercase tracking-wide">
            Tagline
          </p>
          <p className="text-base text-neutral-700">Innovating the future of digital marketing</p>
        </div>
      </div>
    </div>
  );
}

