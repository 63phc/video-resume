import os

from django.urls import reverse_lazy


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = '3il&cnpn#sb$h6mj5psrhp&fy2%d*08nf)8bopor#ludxfx6f-'

DEBUG = True
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'src.apps.users',
    'src.apps.account_worker',
    'src.apps.account_hr',
    'src.apps.resume',
    'src.apps.vacancy',
    'src.apps.question',
    'webpack_loader',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]

AUTH_USER_MODEL = 'users.User'

ROOT_URLCONF = 'src.core.urls'

LOGOUT_REDIRECT_URL = reverse_lazy('index')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['src/templates/', ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'src.core.wsgi.application'


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


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

project_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

MEDIA_ROOT = os.path.join(BASE_DIR, "media/")
MEDIA_URL = '/media/'

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(project_dir, 'src/static/'),)
STATIC_ROOT = os.path.join(os.path.dirname(os.path.dirname(BASE_DIR)), "static/")

WEBPACK_LOADER = {
    'DEFAULT': {
        'CACHE': not DEBUG,
        'BUNDLE_DIR_NAME': 'build/', # must end with slash
        'STATS_FILE': os.path.join(BASE_DIR, './static/webpack.stats.json'),
        'POLL_INTERVAL': 0.1,
        # 'TIMEOUT': None,
        'IGNORE': ['.+\.hot-update.js', '.+\.map']
    }
}

# if not DEBUG:
#     WEBPACK_LOADER.update({
#         'BUNDLE_DIR_NAME': 'build/',
#         'STATS_FILE': os.path.join(BASE_DIR, './static/webpack.stats.json')
#     })

# it's need for flatepages
SITE_ID = 1

try:
    from src.settings.environments.local import *
except ImportError as e:
    pass
