#!/bin/bash
# Production Database Setup Script
# This script runs migrations and seeds the database for production deployment

set -e  # Exit on error

echo "🚀 AdNavi Production Database Setup"
echo "===================================="
echo ""

# Check if DATABASE_URL is set
if [ -z "$DATABASE_URL" ]; then
    echo "❌ ERROR: DATABASE_URL environment variable is not set"
    echo "Please set it to your Railway PostgreSQL connection string:"
    echo "export DATABASE_URL='postgresql://user:password@host:port/dbname'"
    exit 1
fi

echo "✅ DATABASE_URL is set"
echo ""

# Run migrations
echo "📦 Running database migrations..."
cd "$(dirname "$0")"
alembic upgrade head

if [ $? -eq 0 ]; then
    echo "✅ Migrations completed successfully"
else
    echo "❌ Migration failed"
    exit 1
fi

echo ""

# Ask user if they want to seed the database
read -p "Do you want to seed the database with mock data? (y/n) " -n 1 -r
echo ""

if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "🌱 Seeding database..."
    python -m app.seed_mock
    
    if [ $? -eq 0 ]; then
        echo "✅ Database seeded successfully"
        echo ""
        echo "📝 Login credentials:"
        echo "   Owner: owner@defanglabs.com / password123"
        echo "   Viewer: viewer@defanglabs.com / password123"
    else
        echo "❌ Seeding failed"
        exit 1
    fi
else
    echo "⏭️  Skipping database seeding"
fi

echo ""
echo "🎉 Production database setup complete!"
echo "===================================="

