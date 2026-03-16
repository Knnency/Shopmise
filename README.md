# SnapShelf

A modern Django image showcase app where users can upload, categorize, search, and display visual posts in a clean gallery interface.

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Django](https://img.shields.io/badge/Django-5.2-darkgreen?logo=django)
![Render](https://img.shields.io/badge/Deploy-Render-46E3B7)
![Cloudinary](https://img.shields.io/badge/Media-Cloudinary-3448C5)

## Features

- Upload image posts with title, category, description, and image
- Expanded category system (`Nature`, `Travel`, `Food`, `Art`, `Lifestyle`, `Technology`, `Architecture`, `Fashion`, `Sports`, `Animals`, `People`, `Events`, `Business`, `Other`)
- Search posts by title, description, or category
- Filter gallery results by category
- Improved card readability and typography for long descriptions
- Django Admin integration for post management
- Production-ready deployment on Render
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
|- core/                  # Project settings and root URLs
|- gallery/               # Main app (models, forms, views, urls, admin)
|- templates/gallery/     # Homepage template
|- build.sh               # Render build script
|- requirements.txt       # Python dependencies
|- runtime.txt            # Python version pin for Render
`- manage.py
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
TIME_ZONE=UTC

# Optional for local Cloudinary testing
DATABASE_URL=
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
./build.sh && python manage.py shell -c "from django.contrib.auth import get_user_model; import os; U=get_user_model(); u, _ = U.objects.get_or_create(username=os.environ['DJANGO_SUPERUSER_USERNAME'], defaults={'email': os.environ.get('DJANGO_SUPERUSER_EMAIL','admin@example.com')}); u.set_password(os.environ['DJANGO_SUPERUSER_PASSWORD']); u.is_staff=True; u.is_superuser=True; u.is_active=True; u.save(); print('superuser ready')"
```

### Start Command
```bash
gunicorn core.wsgi:application --bind 0.0.0.0:$PORT
```

### Required Environment Variables

```env
DATABASE_URL=...
SECRET_KEY=...
DEBUG=0
ALLOWED_HOSTS=your-service-name.onrender.com
TIME_ZONE=Asia/Manila

CLOUDINARY_CLOUD_NAME=...
CLOUDINARY_API_KEY=...
CLOUDINARY_API_SECRET=...

DJANGO_SUPERUSER_USERNAME=...
DJANGO_SUPERUSER_EMAIL=...
DJANGO_SUPERUSER_PASSWORD=...
```

## Admin Access

Admin URL:

```text
/admin/
```

If Render Shell is unavailable (free plan), use the build command above with `DJANGO_SUPERUSER_*` environment variables to create/update admin credentials on each deploy.

## Notes

- On Render free plan, persistent upload storage should be handled with Cloudinary.
- `.env`, `db.sqlite3`, `mediafiles/`, and `staticfiles/` are ignored via `.gitignore`.

## License

This project is for academic and portfolio use. Add your preferred license if needed.
