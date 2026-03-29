from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = "django-insecure-m*0)#_3c%52w9w-=fs(t(ue2jziu^)wnesejpaoekdq1q-8v3i"


DEBUG = True

ALLOWED_HOSTS = []


INSTALLED_APPS = [
    "crispy_forms",
    "crispy_bootstrap5",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "ckeditor",
    "ckeditor_uploader",
    "rest_framework",
    "drf_spectacular",
    "blog",
    "users",
    "api"
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "project.wsgi.application"




DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}




AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]




LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True




CKEDITOR_RESTRICT_BY_USER = True
STATIC_URL = "/static/"
STATICFILES_DIRS = [str(BASE_DIR.joinpath("static"))]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"



DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


CRISPY_TEMPLATE_PACK = "bootstrap5"

LOGIN_REDIRECT_URL = "blog-home"
LOGIN_URL = "login"

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True

EMAIL_HOST_USER = "abdullacoder17@gmail.com"
EMAIL_HOST_PASSWORD = "mvbt vklb dinx tzts"


CKEDITOR_UPLOAD_PATH = "uploads/"

CKEDITOR_CONFIGS = {
    "default": {
        "toolbar": "Full",
    },
}


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ]
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'Blixly API',
    'DESCRIPTION': 'REST API for Blixly',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
}