# 🚂 Railway Deployment Guide

This guide will help you deploy your Django website to Railway.

## Prerequisites

1. **GitHub Account**: Make sure your code is on GitHub
2. **Railway Account**: Sign up at [railway.app](https://railway.app)
3. **Git**: Make sure you have Git installed locally

## Step 1: Prepare Your Code

### 1.1 Commit All Changes
```bash
git add .
git commit -m "Prepare for Railway deployment"
git push origin main
```

### 1.2 Create a Superuser (Optional)
If you want to access the admin panel:
```bash
python manage.py createsuperuser
```

## Step 2: Deploy to Railway

### 2.1 Connect to Railway
1. Go to [railway.app](https://railway.app)
2. Sign in with your GitHub account
3. Click "New Project"
4. Select "Deploy from GitHub repo"
5. Choose your repository

### 2.2 Configure Environment Variables
In your Railway project dashboard, go to "Variables" tab and add:

```
DEBUG=False
SECRET_KEY=your-super-secret-key-here
ALLOWED_HOSTS=your-app-name.railway.app,localhost,127.0.0.1
```

### 2.3 Add PostgreSQL Database
1. In your Railway project, click "New"
2. Select "Database" → "PostgreSQL"
3. Railway will automatically set the `DATABASE_URL` environment variable

### 2.4 Deploy
1. Railway will automatically detect your Django project
2. It will use the `Procfile` to run your application
3. The deployment will run migrations and collect static files automatically

## Step 3: Configure Custom Domain (Optional)

1. In your Railway project, go to "Settings"
2. Click "Generate Domain" or add your custom domain
3. Update your `ALLOWED_HOSTS` environment variable to include your domain

## Step 4: Add Background Music

### Option 1: Upload via Admin Panel
1. Go to your deployed website: `https://your-app-name.railway.app/admin/`
2. Log in with your superuser credentials
3. Go to "Audios" section
4. Add a new audio file and check "Is background music"

### Option 2: Upload via Railway Files
1. In Railway dashboard, go to "Files" tab
2. Navigate to `static/audio/`
3. Upload your MP3 file as `background-music.mp3`

## Step 5: Verify Deployment

1. Visit your deployed website
2. Check that all pages load correctly
3. Verify that static files (CSS, images) are loading
4. Test the background music functionality
5. Check that the admin panel is accessible

## Troubleshooting

### Common Issues:

1. **Static Files Not Loading**
   - Check that `whitenoise` is in your `MIDDLEWARE`
   - Verify `STATIC_ROOT` is set correctly
   - Run `python manage.py collectstatic` locally

2. **Database Connection Issues**
   - Verify `DATABASE_URL` is set in Railway environment variables
   - Check that PostgreSQL service is running

3. **Media Files Not Uploading**
   - For production, consider using a cloud storage service like AWS S3
   - Or configure Railway's file system for media storage

4. **Background Music Not Playing**
   - Check that the audio file is uploaded correctly
   - Verify the file path in the template
   - Check browser console for errors

### Logs
- Check Railway logs in the "Deployments" tab
- Look for any error messages during deployment

## Environment Variables Reference

| Variable | Description | Example |
|----------|-------------|---------|
| `DEBUG` | Debug mode (False for production) | `False` |
| `SECRET_KEY` | Django secret key | `your-secret-key` |
| `DATABASE_URL` | PostgreSQL connection string | `postgresql://...` |
| `ALLOWED_HOSTS` | Comma-separated list of allowed hosts | `your-app.railway.app` |

## Performance Tips

1. **Enable Caching**: Consider adding Redis for caching
2. **CDN**: Use a CDN for static files in production
3. **Database Optimization**: Add database indexes for better performance
4. **Image Optimization**: Compress images before uploading

## Security Checklist

- [ ] `DEBUG=False` in production
- [ ] Strong `SECRET_KEY` set
- [ ] `ALLOWED_HOSTS` configured
- [ ] HTTPS enabled (automatic on Railway)
- [ ] Admin panel secured with strong password
- [ ] Database credentials secure

## Support

If you encounter issues:
1. Check Railway documentation: [docs.railway.app](https://docs.railway.app)
2. Check Django deployment checklist: [docs.djangoproject.com](https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/)
3. Review Railway logs for error messages

---

🎉 **Congratulations!** Your Django website is now deployed on Railway!
