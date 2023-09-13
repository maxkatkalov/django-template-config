from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent

SECRET_KEY = "django-insecure-$z%k#*sssl9wzf%wded51af+1_$2_(qfix_%9$%#!m2g8_+v49"


INSTALLED_APPS = [
    'db',
    'django_extensions',
]


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


USE_TZ = False

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
