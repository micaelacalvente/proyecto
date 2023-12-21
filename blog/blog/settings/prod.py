from .base import *
# SECURITY WARNING: don't run with debug turned on in production!

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'micacomision6$default',
        'USER': 'micacomision6',
        'PASSWORD': 'informatorio2023',
        'HOST': 'micacomision6.mysql.pythonanywhere-services.com',
        'PORT': '',
    }
}