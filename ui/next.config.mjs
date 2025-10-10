/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'standalone',
  // API URL configuration for production
  env: {
    NEXT_PUBLIC_API_URL: process.env.NEXT_PUBLIC_API_URL || 'https://t8zgrthold5r2-backend--8000.prod1a.defang.dev',
  },
};

export default nextConfig;
