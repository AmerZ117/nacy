# I Love My Gefen So Much ❤️

A beautiful and romantic Django website showcasing love and memories through photos and videos.

## 🌟 Features

- **Beautiful Home Page**: Romantic love messages with animated hearts
- **Photo Gallery**: Masonry layout with lightbox functionality
- **Video Gallery**: Embedded video players for precious moments
- **Responsive Design**: Works perfectly on all devices
- **Modern UI**: Beautiful gradients, animations, and typography
- **Interactive Elements**: Hover effects, smooth transitions, and filters

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repository-url>
   cd gefen-love-website
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run migrations**
   ```bash
   python manage.py migrate
   ```

4. **Start the development server**
   ```bash
   python manage.py runserver
   ```

5. **Open your browser**
   Navigate to `http://127.0.0.1:8000/`

## 📁 Project Structure

```
gefen-love-website/
├── gefen_love_website/     # Main Django project
├── gallery/               # Gallery app
│   ├── templates/         # HTML templates
│   ├── models.py         # Database models
│   ├── views.py          # View functions
│   └── urls.py           # URL patterns
├── static/               # Static files
│   ├── images/           # Photo files
│   └── videos/           # Video files
├── media/                # User uploaded files
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## 🎨 Customization

### Adding New Photos
1. Place your photos in the `static/images/` directory
2. The website will automatically detect and display them

### Adding New Videos
1. Place your videos in the `static/videos/` directory
2. Supported format: MP4

### Changing Colors
Edit the CSS variables in the templates to customize the color scheme:
- Primary color: `#e91e63` (pink)
- Secondary color: `#ff6b9d` (light pink)
- Background gradient: Purple to blue

## 🌐 Deployment

### Deploy to GitHub Pages (Static Files)

1. **Build static files**
   ```bash
   python manage.py collectstatic
   ```

2. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Add beautiful love website"
   git push origin main
   ```

3. **Enable GitHub Pages**
   - Go to your repository settings
   - Scroll to "GitHub Pages" section
   - Select source branch (usually `main`)
   - Save the settings

### Deploy to Heroku

1. **Create Heroku app**
   ```bash
   heroku create your-app-name
   ```

2. **Add buildpacks**
   ```bash
   heroku buildpacks:add heroku/python
   ```

3. **Deploy**
   ```bash
   git push heroku main
   ```

4. **Run migrations**
   ```bash
   heroku run python manage.py migrate
   ```

## 💝 Love Features

- **Floating Hearts**: Animated hearts floating in the background
- **Heartbeat Animation**: Pulsing heart icons
- **Love Messages**: Romantic text throughout the website
- **Memory Counter**: Shows the number of photos and videos
- **Responsive Gallery**: Beautiful grid layout for memories

## 🛠️ Technologies Used

- **Backend**: Django 4.2.7
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Custom CSS with gradients and animations
- **Icons**: Font Awesome
- **Fonts**: Google Fonts (Dancing Script, Poppins)
- **Animations**: AOS (Animate On Scroll)

## 📱 Mobile Responsive

The website is fully responsive and works beautifully on:
- Desktop computers
- Tablets
- Mobile phones
- All modern browsers

## 🔧 Development

### Running Tests
```bash
python manage.py test
```

### Creating Superuser
```bash
python manage.py createsuperuser
```

### Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

## 📄 License

This project is created with love and is open source. Feel free to use and modify for your own love story!

## 💌 Support

If you have any questions or need help customizing the website for your own love story, feel free to reach out!

---

**Made with ❤️ by Amer for my beloved Gefen**

*Every moment with you is a treasure, every smile is a blessing*
