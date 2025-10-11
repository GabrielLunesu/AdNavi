/**
 * Modern Loading Animation Component
 * 
 * WHAT: Futuristic loading animation with smooth transitions
 * WHY: Better UX while data is loading
 * REFERENCES: Used in Finance page and other data-heavy pages
 */

export default function LoadingAnimation({ message = "Loading financial data..." }) {
  return (
    <div className="min-h-[600px] flex items-center justify-center p-8">
      <div className="relative">
        {/* Outer rotating ring */}
        <div className="absolute inset-0 rounded-full border-2 border-cyan-500/20 animate-spin-slow"></div>
        
        {/* Middle pulsing ring */}
        <div className="absolute inset-4 rounded-full border-2 border-cyan-400/40 animate-pulse"></div>
        
        {/* Inner glowing core */}
        <div className="absolute inset-8 rounded-full bg-gradient-to-br from-cyan-400 to-cyan-600 animate-pulse-glow"></div>
        
        {/* Center icon */}
        <div className="relative w-32 h-32 flex items-center justify-center">
          <svg className="w-16 h-16 text-white animate-float" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5} d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
          </svg>
        </div>
        
        {/* Loading message */}
        <div className="absolute -bottom-16 left-1/2 transform -translate-x-1/2 whitespace-nowrap">
          <p className="text-sm font-medium text-neutral-600">{message}</p>
          <div className="flex items-center justify-center gap-1 mt-2">
            <span className="w-2 h-2 bg-cyan-500 rounded-full animate-bounce" style={{ animationDelay: '0ms' }}></span>
            <span className="w-2 h-2 bg-cyan-500 rounded-full animate-bounce" style={{ animationDelay: '150ms' }}></span>
            <span className="w-2 h-2 bg-cyan-500 rounded-full animate-bounce" style={{ animationDelay: '300ms' }}></span>
          </div>
        </div>
      </div>
    </div>
  );
}

// Add these animations to your global CSS:
// @keyframes spin-slow {
//   to { transform: rotate(360deg); }
// }
// animation: spin-slow 3s linear infinite;
//
// @keyframes pulse-glow {
//   0%, 100% { opacity: 0.6; transform: scale(0.8); }
//   50% { opacity: 1; transform: scale(1); }
// }
// animation: pulse-glow 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
//
// @keyframes float {
//   0%, 100% { transform: translateY(0); }
//   50% { transform: translateY(-10px); }
// }
// animation: float 3s ease-in-out infinite;
