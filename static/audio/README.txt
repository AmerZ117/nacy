BACKGROUND MUSIC SETUP
======================

To add background music to your website:

1. Place your MP3 file in this directory (static/audio/)
2. Rename it to "background-music.mp3" 
   OR
   Update the audio source in gallery/templates/gallery/base.html to match your filename

Supported formats: MP3, WAV, OGG

The music will automatically play when users visit the website and loop continuously.
Users can control the music using the floating music player in the bottom-right corner.

Note: Modern browsers may block autoplay until the user interacts with the page.
The music will start playing after the first user interaction (click, scroll, etc.).
