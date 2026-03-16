# SnapShelf

A modern Django image showcase app where users can upload, categorize, and display visual posts in a clean gallery interface.

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Django](https://img.shields.io/badge/Django-5.2-darkgreen?logo=django)
![Render](https://img.shields.io/badge/Deploy-Render-46E3B7)
![Cloudinary](https://img.shields.io/badge/Media-Cloudinary-3448C5)

## Features

- Upload image posts with title, category, and description
- Professional homepage UI with responsive card layout
- Category-based organization (`Nature`, `Travel`, `Food`, `Art`, `Lifestyle`, `Other`)
- Django Admin integration for post management
- Production-ready setup for Render
- Persistent media storage using Cloudinary (works on Render free plan)

## Tech Stack

- Python
- Django
- SQLite (local development)
- PostgreSQL (Render production via `DATABASE_URL`)
- WhiteNoise (static files)
- Cloudinary (`django-cloudinary-storage`) for media uploads
- Bootstrap 5 for frontend styling

## Project Structure

```text
snapshelf/
├── core/                  # Project settings and root URLs
├── gallery/               # Main app (models, forms, views, urls, admin)
├── templates/gallery/     # Homepage template
├── build.sh               # Render build script
├── requirements.txt       # Python dependencies
└── manage.py
```

## Local Setup

1. Clone the repo
```bash
git clone https://github.com/richald03/Snapshelf.git
cd Snapshelf
```

2. Create and activate virtual environment
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Create `.env` in project root
```env
SECRET_KEY=django-insecure-change-this-to-your-secret-key
DEBUG=1
ALLOWED_HOSTS=127.0.0.1 localhost

# Optional for local Cloudinary testing
CLOUDINARY_CLOUD_NAME=
CLOUDINARY_API_KEY=
CLOUDINARY_API_SECRET=
```

5. Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

6. Start development server
```bash
python manage.py runserver
```

Open: `http://127.0.0.1:8000`

## Deployment (Render)

### Build Command
```bash
./build.sh
```

### Start Command
```bash
gunicorn core.wsgi:application
```

### Required Environment Variables

```env
DATABASE_URL=...
SECRET_KEY=...
DEBUG=0
ALLOWED_HOSTS=your-service-name.onrender.com

CLOUDINARY_CLOUD_NAME=...
CLOUDINARY_API_KEY=...
CLOUDINARY_API_SECRET=...
```

## Admin Access

Create a superuser:

```bash
python manage.py createsuperuser
```

Admin URL:

```text
/admin/
```

## Notes

- On Render free plan, persistent upload storage should be handled with Cloudinary.
- `.env`, `db.sqlite3`, `mediafiles/`, and `staticfiles/` are ignored via `.gitignore`.

## License

This project is for academic and portfolio use. Add your preferred license if needed.
