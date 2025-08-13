#!/bin/bash

# Railway Deployment Script for Django Website
echo "🚂 Preparing for Railway deployment..."

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "❌ Git is not installed. Please install Git first."
    exit 1
fi

# Check if we're in a git repository
if ! git rev-parse --git-dir > /dev/null 2>&1; then
    echo "❌ Not in a git repository. Please initialize git first:"
    echo "   git init"
    echo "   git add ."
    echo "   git commit -m 'Initial commit'"
    exit 1
fi

# Check if we have a remote repository
if ! git remote get-url origin &> /dev/null; then
    echo "❌ No remote repository found. Please add your GitHub repository:"
    echo "   git remote add origin https://github.com/yourusername/yourrepo.git"
    exit 1
fi

echo "✅ Git repository found"

# Collect static files
echo "📦 Collecting static files..."
python manage.py collectstatic --noinput

# Make migrations
echo "🗄️  Making migrations..."
python manage.py makemigrations

# Run migrations
echo "🔄 Running migrations..."
python manage.py migrate

# Add all changes
echo "📝 Adding changes to git..."
git add .

# Commit changes
echo "💾 Committing changes..."
git commit -m "Prepare for Railway deployment - $(date)"

# Push to GitHub
echo "🚀 Pushing to GitHub..."
git push origin main

echo ""
echo "🎉 Code pushed to GitHub successfully!"
echo ""
echo "📋 Next steps:"
echo "1. Go to https://railway.app"
echo "2. Sign in with your GitHub account"
echo "3. Click 'New Project'"
echo "4. Select 'Deploy from GitHub repo'"
echo "5. Choose your repository"
echo "6. Add PostgreSQL database"
echo "7. Configure environment variables:"
echo "   - DEBUG=False"
echo "   - SECRET_KEY=your-secret-key"
echo "   - ALLOWED_HOSTS=your-app-name.railway.app"
echo ""
echo "📖 For detailed instructions, see RAILWAY_DEPLOYMENT.md"
