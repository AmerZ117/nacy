from django.shortcuts import render
from django.conf import settings
import os
from pathlib import Path
from .models import Photo, Video, Audio

# Create your views here.

def home(request):
    """Home page view with a beautiful love message for Gefen"""
    # Get background music
    try:
        db_audio = Audio.objects.filter(is_background_music=True).first()
        background_music = None
        if db_audio and db_audio.audio_file:
            background_music = {
                'name': db_audio.audio_file.name.split('/')[-1],
                'url': db_audio.audio_file.url,
                'title': db_audio.title
            }
    except Exception as e:
        background_music = None
    
    # Fallback to static files if no database audio
    if not background_music:
        audio_dir = Path(settings.BASE_DIR) / 'static' / 'audio'
        if audio_dir.exists():
            for audio_file in audio_dir.glob('*.mp3'):
                background_music = {
                    'name': audio_file.name,
                    'url': f'/static/audio/{audio_file.name}',
                    'title': f'Background Music - {audio_file.stem}'
                }
                break
    
    context = {
        'background_music': background_music,
    }
    return render(request, 'gallery/home.html', context)

def gallery(request):
    """Gallery view showing all photos and videos"""
    # Try to get photos and videos from database first
    try:
        db_photos = Photo.objects.all()
        db_videos = Video.objects.all()
        db_audio = Audio.objects.filter(is_background_music=True).first()
        
        # Convert database objects to the same format as static files
        images = []
        for photo in db_photos:
            images.append({
                'name': photo.image.name.split('/')[-1] if photo.image else '',
                'url': photo.image.url if photo.image else '',
                'title': photo.title
            })
        
        videos = []
        for video in db_videos:
            videos.append({
                'name': video.video_file.name.split('/')[-1] if video.video_file else '',
                'url': video.video_file.url if video.video_file else '',
                'title': video.title
            })
            
        # Get background music from database
        background_music = None
        if db_audio and db_audio.audio_file:
            background_music = {
                'name': db_audio.audio_file.name.split('/')[-1],
                'url': db_audio.audio_file.url,
                'title': db_audio.title
            }
            
    except Exception as e:
        # Fallback to static files if database fails
        print(f"Database error: {e}")
        images = []
        videos = []
        background_music = None
    
    # If no database content, fallback to static files
    if not images:
        # Get all image files from static/images directory
        images_dir = Path(settings.BASE_DIR) / 'static' / 'images'
        if images_dir.exists():
            for img_file in images_dir.glob('*.jpg'):
                images.append({
                    'name': img_file.name,
                    'url': f'/static/images/{img_file.name}',
                    'title': f'Photo of Gefen - {img_file.stem}'
                })
    
    if not videos:
        # Get all video files from static/videos directory
        videos_dir = Path(settings.BASE_DIR) / 'static' / 'videos'
        if videos_dir.exists():
            for vid_file in videos_dir.glob('*.mp4'):
                videos.append({
                    'name': vid_file.name,
                    'url': f'/static/videos/{vid_file.name}',
                    'title': f'Video of Gefen - {vid_file.stem}'
                })
    
    # If no background music from database, check static files
    if not background_music:
        audio_files = []
        audio_dir = Path(settings.BASE_DIR) / 'static' / 'audio'
        if audio_dir.exists():
            for audio_file in audio_dir.glob('*.mp3'):
                audio_files.append({
                    'name': audio_file.name,
                    'url': f'/static/audio/{audio_file.name}',
                    'title': f'Background Music - {audio_file.stem}'
                })
            # Use the first audio file as background music
            if audio_files:
                background_music = audio_files[0]
    
    context = {
        'images': images,
        'videos': videos,
        'background_music': background_music,
    }
    return render(request, 'gallery/gallery.html', context)
