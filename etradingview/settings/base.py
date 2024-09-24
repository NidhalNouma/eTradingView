"""
Django settings for etradingview project.

Generated by 'django-admin startproject' using Django 4.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
import environ


# Initialise environment variables
env = environ.Env()
environ.Env.read_env()

# print(env)
# print(os.environ)

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent
PROJECT_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []



# Application definition

INSTALLED_APPS = [
    'profile_user.apps.ProfileUserConfig',
    'strategies',
    'docs',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.sites',
    # Add the following django-allauth apps
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google', # for Google OAuth
    'ckeditor',

    "django_htmx",
    'storages',
    'compressor', 
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'profile_user.middleware.check_user_and_stripe_middleware',
    'allauth.account.middleware.AccountMiddleware',

    "django_htmx.middleware.HtmxMiddleware",
]

ROOT_URLCONF = 'etradingview.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates", 
                BASE_DIR / "etradingview/templates",
                BASE_DIR / "etradingview/templates/etradingview",
                BASE_DIR / "profile_user/templates/profile_user",
                BASE_DIR / "docs/templates/docs",
                BASE_DIR / "strategies/templates/strategies"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'profile_user.context_processors.profile_context',
            ],
        },
    },
]

WSGI_APPLICATION = 'etradingview.wsgi.application'




# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [ BASE_DIR / "static",]

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Composer settings for tailwind css

COMPRESS_ROOT = BASE_DIR / 'static'

COMPRESS_ENABLED = True

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',  # Finds files in STATICFILES_DIRS
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',  # Finds files in your apps' static directories
    'compressor.finders.CompressorFinder',  # Required for Django Compressor
]

# SMTP settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.zoho.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')

DEFAULT_FROM_EMAIL = env('EMAIL_HOST_USER')

# Django allauth

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend'
]

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        },
    }
}


SITE_ID = 2

SOCIALACCOUNT_LOGIN_ON_GET= True

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "optional"  # or "mandatory" based on your requirement
LOGIN_REDIRECT_URL = '/p/'  # Ensure it redirects to the home page after login
ACCOUNT_LOGOUT_REDIRECT_URL = '/'  # Redirect after logout

# SOCIALACCOUNT_ADAPTER = 'etradingview.adapters.CustomSocialAccountAdapter'

# Prices

PRICE_LIST = {
    'MONTHLY': env('STRIPE_PRICE_MN_ID'),
    'QUARTERLY': env('STRIPE_PRICE_3MN_ID'),
    'YEARLY': env('STRIPE_PRICE_Y_ID'),
    'LIFETIME': env('STRIPE_PRICE_LT_ID'),
}

PRICES = {
    'MONTHLY': env('STRIPE_PRICE_MN_PRICE'),
    'QUARTERLY': env('STRIPE_PRICE_3MN_PRICE'),
    'YEARLY': env('STRIPE_PRICE_Y_PRICE'),
    'LIFETIME': env('STRIPE_PRICE_LT_PRICE'),
}

# CKEDITOR Text Editor

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 300,
        'width': '100%',
        'extraPlugins': ','.join([
            'uploadimage', # Enable the upload image feature
            'div',
            'autolink',
            'autoembed',
            'embedsemantic',
            'autogrow',
            # other plugins
        ]),
    }
}

# Backend tasks

CELERY_BROKER_URL = 'redis://' + env('REDIS_ENDPOINT') + ':6379/0'  # Configure as per your broker
CELERY_RESULT_BACKEND = 'redis://' + env('REDIS_ENDPOINT') + ':6379/0'
