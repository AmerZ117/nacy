# 🚀 Deployment Guide

This guide will help you deploy your beautiful "I Love My Gefen So Much" website to various platforms.

## 📋 Prerequisites

Before deploying, make sure you have:
- Git installed on your computer
- A GitHub account
- Python 3.8+ installed
- All dependencies installed (`pip install -r requirements.txt`)

## 🌐 Deploy to GitHub

### Step 1: Initialize Git Repository

```bash
# Initialize git repository
git init

# Add all files to git
git add .

# Make your first commit
git commit -m "Initial commit: Beautiful love website for Gefen"
```

### Step 2: Create GitHub Repository

1. Go to [GitHub.com](https://github.com)
2. Click the "+" icon in the top right corner
3. Select "New repository"
4. Name your repository (e.g., "gefen-love-website")
5. Make it public or private (your choice)
6. Don't initialize with README (we already have one)
7. Click "Create repository"

### Step 3: Push to GitHub

```bash
# Add your GitHub repository as remote origin
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# Push to GitHub
git push -u origin main
```

### Step 4: Deploy to GitHub Pages (Static Version)

Since Django is a server-side framework, we'll create a static version for GitHub Pages:

1. **Create a static version of your site**
   - The current setup works for local development
   - For GitHub Pages, you might want to create a static HTML version

2. **Alternative: Use Django with a hosting service**
   - Continue to the next sections for full Django deployment

## ☁️ Deploy to Heroku

### Step 1: Install Heroku CLI

Download and install from: https://devcenter.heroku.com/articles/heroku-cli

### Step 2: Create Heroku App

```bash
# Login to Heroku
heroku login

# Create a new Heroku app
heroku create your-app-name

# Add Python buildpack
heroku buildpacks:add heroku/python
```

### Step 3: Configure for Production

Create a `Procfile` in your project root:

```
web: gunicorn gefen_love_website.wsgi --log-file -
```

Update `requirements.txt`:

```
Django==4.2.7
Pillow==10.0.1
gunicorn==21.2.0
whitenoise==6.5.0
```

### Step 4: Update Settings for Production

Add to `gefen_love_website/settings.py`:

```python
import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['your-app-name.herokuapp.com', 'localhost', '127.0.0.1']

# Static files configuration
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Add whitenoise middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Add this line
    # ... other middleware
]
```

### Step 5: Deploy to Heroku

```bash
# Add all changes
git add .

# Commit changes
git commit -m "Configure for Heroku deployment"

# Deploy to Heroku
git push heroku main

# Run migrations
heroku run python manage.py migrate

# Open your app
heroku open
```

## 🐳 Deploy with Docker

### Step 1: Create Dockerfile

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

### Step 2: Create docker-compose.yml

```yaml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - .:/app
    environment:
      - DEBUG=True
```

### Step 3: Run with Docker

```bash
# Build and run
docker-compose up --build

# Or run in background
docker-compose up -d
```

## 🌍 Deploy to PythonAnywhere

### Step 1: Create PythonAnywhere Account

1. Go to [PythonAnywhere.com](https://www.pythonanywhere.com)
2. Create a free account
3. Access your dashboard

### Step 2: Upload Your Code

1. Go to the "Files" tab
2. Upload your project files
3. Or use git to clone your repository

### Step 3: Configure Web App

1. Go to the "Web" tab
2. Click "Add a new web app"
3. Choose "Django"
4. Select Python version
5. Set your source code directory

### Step 4: Configure Settings

Update your Django settings for PythonAnywhere:

```python
ALLOWED_HOSTS = ['yourusername.pythonanywhere.com']
DEBUG = False
```

### Step 5: Deploy

1. Run migrations in the PythonAnywhere console
2. Collect static files
3. Reload your web app

## 🔧 Environment Variables

For production, use environment variables for sensitive settings:

```python
import os

SECRET_KEY = os.environ.get('SECRET_KEY', 'your-default-secret-key')
DEBUG = os.environ.get('DEBUG', 'False') == 'True'
```

## 📊 Monitoring and Maintenance

### Health Checks

Add a simple health check endpoint:

```python
# In your views.py
from django.http import JsonResponse

def health_check(request):
    return JsonResponse({'status': 'healthy', 'message': 'I Love My Gefen So Much!'})
```

### Logging

Configure logging in settings:

```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'django.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}
```

## 🎯 Quick Deployment Checklist

- [ ] All files committed to git
- [ ] Dependencies listed in requirements.txt
- [ ] Static files configured
- [ ] Database migrations ready
- [ ] Environment variables set
- [ ] Debug mode disabled for production
- [ ] Allowed hosts configured
- [ ] SSL certificate (if needed)

## 🆘 Troubleshooting

### Common Issues

1. **Static files not loading**
   - Run `python manage.py collectstatic`
   - Check STATIC_ROOT and STATIC_URL settings

2. **Database errors**
   - Run `python manage.py migrate`
   - Check database configuration

3. **Import errors**
   - Verify all dependencies are installed
   - Check Python version compatibility

### Getting Help

- Check Django documentation: https://docs.djangoproject.com/
- Review deployment logs
- Test locally before deploying

---

**Happy Deploying! 💕**

*Your love story deserves to be shared with the world*

---

**Made with ❤️ by Amer for Gefen**
