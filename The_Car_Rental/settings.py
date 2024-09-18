"""
Django settings for The_Car_Rental project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

STRIPE_PUBLISHABLE_KEY=config('STRIPE_PUBLISHABLE_KEY')
STRIPE_SECRET_KEY=config('STRIPE_SECRET_KEY')
LOCAL_DOMAIN=config('LOCAL_DOMAIN')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-b86s0n^!i&n1%$(*3owf%$+5r&grdari4#zc@=3hsw)k+yp3+e'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = []


# ALLOWED_HOSTS = []


CART_SESSION_ID = 'cart'


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'contact',
    'Main_Hero_Section',
    'Default_Background',
    'Main_Cars_Carousel',
    'Counter_Section',
    'Why_Choose_Us_Section',
    'Testimonial',
    'Background_Video',
    'General_Questions',
    'CARS',
    'Blog',
    'Our_Team',
    'About_Counter_Description',
    'Book_Your_Drive_Section',
    'Questions_About_Payment',
    'Quick_Book',
    'cart',
    'users',

    'orders',

    'Header',
    'Footer',
    'Newsletter',



]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'whitenoise.middleware.WhiteNoiseMiddleware',
    'The_Car_Rental.middleware.Custom404Middleware',
    # 'whitenoise.middleware.WhiteNoiseMiddleware',

]


ROOT_URLCONF = 'The_Car_Rental.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR, 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'cart.context_processor.cart_total_amount',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'The_Car_Rental.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': BASE_DIR / 'db.sqlite3',

        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'car_rental',     # Replace with your MySQL database name
        'DATABASE': 'car_rental',
        'USER': 'root',    # Replace with your MySQL username
        'PASSWORD': '',# Replace with your MySQL password
        'HOST': 'localhost',              # Or an IP Address that your MySQL is hosted on
        'PORT': '3306',

        # 'ENGINE': 'django.db.backends.mysql',
        # 'NAME': 'thecarre_car_rental',     # Replace with your MySQL database name
        # 'DATABASE': 'thecarre_car_rental',
        # 'USER': 'thecarre_car_rental_test',    # Replace with your MySQL username
        # 'PASSWORD': 'u3kLBYGT@6Yv',# Replace with your MySQL password
        # 'HOST': 'localhost',              # Or an IP Address that your MySQL is hosted on
        # 'PORT': '3306',



        # 'ENGINE': 'django.db.backends.mysql',
        # 'NAME': 'thecarre_car_rental',     # Replace with your MySQL database name
        # 'DATABASE': 'thecarre_car_rental',
        # 'USER': 'thecarre_car_rental_test',    # Replace with your MySQL username
        # 'PASSWORD': 'u3kLBYGT@6Yv',# Replace with your MySQL password
        # 'HOST': 'localhost',              # Or an IP Address that your MySQL is hosted on
        # 'PORT': '3306',

        
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'


TIME_ZONE = "Asia/Karachi"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

STATIC_ROOT = BASE_DIR / 'productionfiles'

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

MEDIA_ROOT = BASE_DIR / 'media'

MEDIA_URL = '/media/'





# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'








EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'malikqasim20051@gmail.com'
EMAIL_HOST_PASSWORD = 'Haiderammar123'  # Use the app password here
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER