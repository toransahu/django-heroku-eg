from .base_settings import *


# not necessary, but better
'''
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder'
)
'''

# only for dev server, otherwise it will conflict with collectstatic in production
'''
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'), 
    '/var/www/static/',
]
'''
# Production level settings - HTTPS may cause error in browser, use incognito tab
CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False
SECURE_SSL_REDIRECT = False
SECURE_BROWSER_XSS_FILTER = False
# X_FRAME_OPTIONS = 'DENY'
SECURE_CONTENT_TYPE_NOSNIFF = False


SECURE_HSTS_SECONDS = 0
SECURE_HSTS_INCLUDE_SUBDOMAINS = False
SECURE_HSTS_PRELOAD = False


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6r=p$2nh^@=)f_hpe@&dbm1h(yj^55^0wla^sm3*v2%#85p=jp'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# allowed host not required in dev
ALLOWED_HOSTS = ['toransahu.herokuapp.com', 'toransahu.pythonanywhere.com', '127.0.0.1', '0.0.0.0']


# not required to set STATIC_ROOT in dev
# STATIC_ROOT = os.path.join(BASE_DIR, 'allstatic') # don't name it 'static', during collection django gets confused
