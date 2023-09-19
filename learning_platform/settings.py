from pathlib import Path
from courses import views
import os



AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',  # Default authentication backend
]

MIDDLEWARE = [
    # ...
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # ...
]


BASE_DIR = Path(__file__).resolve().parent.parent


# Specifiication of the root URL patterns
ROOT_URLCONF = 'learning_platform.urls'

AUTH_USER_MODEL = 'profiles.UserProfile' 

# ...

# Installed apps configuration
INSTALLED_APPS = [
    # ...
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'courses',
    'profiles',  # Your app
]

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# ...

# Database configuration (for SQLite)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# ...

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
# ...
