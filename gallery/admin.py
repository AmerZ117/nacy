from django.contrib import admin
from .models import Photo, Video, Audio

# Register your models here.
@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title', 'description')
    readonly_fields = ('created_at',)

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title', 'description')
    readonly_fields = ('created_at',)

@admin.register(Audio)
class AudioAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_background_music', 'created_at')
    list_filter = ('is_background_music', 'created_at')
    search_fields = ('title', 'description')
    readonly_fields = ('created_at',)
    list_editable = ('is_background_music',)
