@echo off
echo 🚂 Preparing for Railway deployment...

REM Check if git is installed
git --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Git is not installed. Please install Git first.
    pause
    exit /b 1
)

REM Check if we're in a git repository
git rev-parse --git-dir >nul 2>&1
if errorlevel 1 (
    echo ❌ Not in a git repository. Please initialize git first:
    echo    git init
    echo    git add .
    echo    git commit -m "Initial commit"
    pause
    exit /b 1
)

REM Check if we have a remote repository
git remote get-url origin >nul 2>&1
if errorlevel 1 (
    echo ❌ No remote repository found. Please add your GitHub repository:
    echo    git remote add origin https://github.com/yourusername/yourrepo.git
    pause
    exit /b 1
)

echo ✅ Git repository found

REM Collect static files
echo 📦 Collecting static files...
python manage.py collectstatic --noinput

REM Make migrations
echo 🗄️  Making migrations...
python manage.py makemigrations

REM Run migrations
echo 🔄 Running migrations...
python manage.py migrate

REM Add all changes
echo 📝 Adding changes to git...
git add .

REM Commit changes
echo 💾 Committing changes...
git commit -m "Prepare for Railway deployment - %date% %time%"

REM Push to GitHub
echo 🚀 Pushing to GitHub...
git push origin main

echo.
echo 🎉 Code pushed to GitHub successfully!
echo.
echo 📋 Next steps:
echo 1. Go to https://railway.app
echo 2. Sign in with your GitHub account
echo 3. Click "New Project"
echo 4. Select "Deploy from GitHub repo"
echo 5. Choose your repository
echo 6. Add PostgreSQL database
echo 7. Configure environment variables:
echo    - DEBUG=False
echo    - SECRET_KEY=your-secret-key
echo    - ALLOWED_HOSTS=your-app-name.railway.app
echo.
echo 📖 For detailed instructions, see RAILWAY_DEPLOYMENT.md
pause
