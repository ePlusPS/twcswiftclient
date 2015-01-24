"""
Django settings for twcswiftclient project.

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
SECRET_KEY = '+=8i5y##fl7b5$50o(#qk$s((q*7e*h6z&-u_bxa_4v_h4$d-o'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'gallery',
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


ROOT_URLCONF = 'twcswiftclient.urls'

WSGI_APPLICATION = 'twcswiftclient.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), 'templates'),
)

DEFAULT_FILE_STORAGE = 'swift.storage.SwiftStorage'
STATICFILES_STORAGE = 'swift.storage.StaticSwiftStorage'

SWIFT_AUTH_URL = 'http://172.168.2.110:5000/v2.0'
SWIFT_USERNAME = 'admin'
SWIFT_KEY = '213e1687ba754530'
SWIFT_AUTH_VERSION = 2.0
SWIFT_TENANT_NAME = 'admin'
SWIFT_CONTAINER_NAME = 'twc_client_demo_container'
SWIFT_STATIC_CONTAINER_NAME = 'twc_client_demo_static_container'
SWIFT_AUTO_CREATE_CONTAINER = True
SWIFT_AUTO_BASE_URL = True
SWIFT_BASE_URL = 'http://172.168.2.110:8080/'
SWIFT_USE_TEMP_URLS = True
SWIFT_TEMP_URL_KEY = 'twcswift_demo'
SWIFT_TEMP_URL_DURATION = 30*60
SWIFT_EXTRA_OPTIONS = {}







