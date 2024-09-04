"""
Django settings for freedjango project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-#g-84&bph@pj@qoq@i4rsr&k-b$8v=5br9vs^m+j32i6mg)7d&"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "users.apps.UsersConfig",
    # "kaspi",
    "polygraphy.apps.PolygraphyConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.postgres",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # "park",
    "polls",
    'social_django',
    'userprofile',
    'bootstrap4',
    ]

MIDDLEWARE = [
    "polls.middleware.simple_middleware",
    "polls.middleware.CustomMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
]

ROOT_URLCONF = "freedjango.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["MyTemplates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                'django.template.context_processors.media',
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
             "libraries":{
                    'custom': 'freedjango.templatetags.custom'
                }
        },
    },
]

# WSGI_APPLICATION = "freedjango.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
# POSTGRESQL
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql_psycopg2",
#         "NAME": "django",
#         "USER": "postgres",
#         "PASSWORD": "123",
#         "HOST": "localhost",
#         "PORT": "5050",
#     }
# }
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTHENTICATION_BACKENDS = (
    'social_core.backends.open_id.OpenIdAuth',
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.google.GoogleOAuth',
    'social_core.backends.twitter.TwitterOAuth',
    # 'social_core.backends.yahoo.YahooOpenId',
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.instagram.InstagramOAuth2',
    'django.contrib.auth.backends.ModelBackend',
    
)



# CASHES = {
#     'default': {
#         'BACKEND':  
#                 'django.core.cache.backends.redis.RedisCache',
#         'LOCATION': 'redis://redis-18306.c302.asia-northeast1-1.gce.redns.redis-cloud.com:18306',
#         'OPTIONS': {
#             'PASSWORD' : 'gifTs1TvvfK7mDS9SuFNvpW0j4KBdA77',
#         }
#     }
# }
CACHES = { 
    'default': { 
        'BACKEND':  
                'django.core.cache.backends.redis.RedisCache', 
        'LOCATION': 'redis://redis-12583.c299.asia-northeast1-1.gce.redns.redis-cloud.com:12583', 
        'OPTIONS': { 
            'password': 'euq9hnBtrn8FkRdsSLfNGftSf6PRqpt9', 
        } 
    } 
}


CACHE_MIDDLEWARE_ALIAS = 'default'
CACHE_MIDDLEWARE_SECONDS = 30
CACHE_MIDDLEWARE_KEY_PREFIX = 'aaaa'


MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = 'media/'

# EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
EMAIL_FILE_PATH = BASE_DIR / 'media'