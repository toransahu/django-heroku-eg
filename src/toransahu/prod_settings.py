from .base_settings import *


# Production level settings
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
SECURE_CONTENT_TYPE_NOSNIFF = True


SECURE_HSTS_SECONDS = 1
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6r=p$2nh^@=)f_hpe@&dbm1h(yj^55^0wla^sm3*v2%#85p=jp'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['toransahu.herokuapp.com', 'toransahu.pythonanywhere.com', '127.0.0.1', '0.0.0.0']


STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder'
)



STATIC_ROOT = os.path.join(BASE_DIR, 'allstatic')
