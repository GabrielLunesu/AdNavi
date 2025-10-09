/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'standalone',
  // API URL configuration for production
  env: {
    NEXT_PUBLIC_API_URL: process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000',
  },
};

export default nextConfig;
