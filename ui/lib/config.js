// Centralized configuration for frontend
// Handles both local development and production deployment
// WHY: One source of truth for environment-specific settings

/**
 * Get the backend API base URL
 * Priority:
 * 1. NEXT_PUBLIC_API_BASE environment variable (set during build for production)
 * 2. Fallback to localhost for local development
 */
export function getApiBase() {
  // Check if we have the env var set during build
  const envBase = process.env.NEXT_PUBLIC_API_BASE;
  
  // If we have it and it's not empty, use it
  if (envBase && envBase.trim() !== '') {
    return envBase;
  }
  
  // Fallback for local development
  // This runs when NEXT_PUBLIC_API_BASE is not set (local dev)
  if (typeof window !== 'undefined') {
    // Client-side: use localhost
    return 'http://localhost:8000';
  } else {
    // Server-side: use localhost (for SSR)
    return 'http://localhost:8000';
  }
}

/**
 * Check if we're running in production
 */
export function isProduction() {
  return process.env.NODE_ENV === 'production';
}

/**
 * Check if we're running in development
 */
export function isDevelopment() {
  return process.env.NODE_ENV === 'development';
}

/**
 * Get configuration object
 */
export const config = {
  apiBase: getApiBase(),
  isProduction: isProduction(),
  isDevelopment: isDevelopment(),
};

// Export as default for convenience
export default config;

