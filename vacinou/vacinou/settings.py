"""
Django settings for vacinou project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=5pim$z%sx^n&ylrq5qq$sso!nj==t6h^7oe5dn756!2#_z@3z'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#DEFAULT_FROM_EMAIL = 'VACINOU <vacinouenterprise@gmail.com>'
#EMAIL_USE_TLS = True
#EMAIL_HOST = 'smtp.gmail.com'
#EMAIL_HOST_USER = 'vacinouenterprise@gmail.com'
#EMAIL_HOST_PASSWORD = 'vacinou2jm'
#EMAIL_PORT = 587

#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'Vacinou Contato<vacinouenterprise@gmail.com>'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'vacinouenterprise@gmail.com'
EMAIL_HOST_PASSWORD = 'vacinouj2m'
EMAIL_PORT = 587



# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'vacinas',
    'doencas',
    'django_verbatim',
    'widget_tweaks',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'vacinou.urls'

WSGI_APPLICATION = 'vacinou.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'vacinou_bd',
            }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
MEDIA_URL = '/media/'

TEMPLATE_DIRS = [
    os.path.join(BASE_DIR, 'templates'),
    BASE_DIR,
]

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    BASE_DIR,
)


