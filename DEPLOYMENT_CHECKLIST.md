# 🚂 Railway Deployment Checklist

## ✅ Pre-Deployment Checklist

### Code Preparation
- [ ] All code changes committed to Git
- [ ] Static files collected (`python manage.py collectstatic`)
- [ ] Database migrations created and applied
- [ ] No syntax errors in code
- [ ] All required files present:
  - [ ] `Procfile`
  - [ ] `requirements.txt`
  - [ ] `runtime.txt`
  - [ ] `railway.json`
  - [ ] `.gitignore`

### Environment Setup
- [ ] GitHub repository created and code pushed
- [ ] Railway account created
- [ ] PostgreSQL database ready (will be created on Railway)

### Configuration
- [ ] `DEBUG=False` for production
- [ ] Strong `SECRET_KEY` generated
- [ ] `ALLOWED_HOSTS` configured
- [ ] Database settings updated for PostgreSQL
- [ ] Static files configuration with whitenoise
- [ ] Security settings enabled

## 🚀 Deployment Steps

### Step 1: Push to GitHub
```bash
# Run the deployment script
./deploy.bat  # Windows
# OR
./deploy.sh   # Linux/Mac
```

### Step 2: Deploy on Railway
1. [ ] Go to [railway.app](https://railway.app)
2. [ ] Sign in with GitHub
3. [ ] Click "New Project"
4. [ ] Select "Deploy from GitHub repo"
5. [ ] Choose your repository
6. [ ] Wait for initial deployment

### Step 3: Configure Database
1. [ ] In Railway project, click "New"
2. [ ] Select "Database" → "PostgreSQL"
3. [ ] Wait for database to be created
4. [ ] Verify `DATABASE_URL` is set automatically

### Step 4: Set Environment Variables
In Railway project → Variables tab:
- [ ] `DEBUG=False`
- [ ] `SECRET_KEY=your-secret-key-here`
- [ ] `ALLOWED_HOSTS=your-app-name.railway.app`

### Step 5: Verify Deployment
- [ ] Website loads correctly
- [ ] Static files (CSS, images) display properly
- [ ] Admin panel accessible
- [ ] Background music works
- [ ] All pages functional

## 🔧 Post-Deployment

### Create Superuser
```bash
# In Railway terminal or locally with DATABASE_URL
python manage.py createsuperuser
```

### Add Background Music
1. [ ] Go to admin panel: `https://your-app.railway.app/admin/`
2. [ ] Log in with superuser credentials
3. [ ] Go to "Audios" section
4. [ ] Add audio file and check "Is background music"

### Test All Features
- [ ] Home page loads
- [ ] Gallery page displays photos/videos
- [ ] Background music plays
- [ ] Music controls work
- [ ] Responsive design on mobile
- [ ] Admin panel functions

## 🐛 Troubleshooting

### Common Issues
- [ ] Static files not loading → Check whitenoise configuration
- [ ] Database connection errors → Verify DATABASE_URL
- [ ] 500 errors → Check Railway logs
- [ ] Music not playing → Verify audio file upload

### Useful Commands
```bash
# Check Railway logs
railway logs

# Run Django shell on Railway
railway run python manage.py shell

# Run migrations manually
railway run python manage.py migrate

# Collect static files
railway run python manage.py collectstatic
```

## 📞 Support

If you encounter issues:
1. Check Railway documentation: [docs.railway.app](https://docs.railway.app)
2. Review Railway logs in the dashboard
3. Check Django deployment checklist
4. Verify all environment variables are set correctly

---

🎉 **Your Django website is now live on Railway!**
