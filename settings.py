DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
	('soe', 'soe@soe.im'),
)

MANAGERS = ADMINS

import sys, os

# set project path
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))

# append apps and libs
sys.path.append(os.path.join(PROJECT_PATH, '~apps'))
sys.path.append(os.path.join(PROJECT_PATH, '~libs'))

import mongoengine
# connect to mongoengine
mongoengine.connect('riverid')
# mongoengine.connect(db, username=None, password=None, **kwargs)

TIME_ZONE = 'America/Chicago'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = False

USE_L10N = False

MEDIA_ROOT = os.path.join(PROJECT_PATH, 'static')

MEDIA_URL = '/static/'

# ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '*m7yaq5xzi@4z*mgxar*s%l=$)+i7rml4pdme_$_i#wvng#a7v'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.media',
    'context_processors.auth',
    'context_processors.site_info',
)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, 'templates'),
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

# uses mongoengine auth and sessions
SESSION_ENGINE = 'mongoengine.django.sessions'

AUTHENTICATION_BACKENDS = (
    'mongoengine.django.auth.MongoEngineBackend',
)

ROOT_URLCONF = 'urls'

INSTALLED_APPS = (
    'django.contrib.sessions',
    # 'django.contrib.messages',

	'registration',	
    'face',
    'key',
    'fish',

	'piston',
    'api',	
    # Uncomment the next line to enable the admin:
    # 'django.contrib.admin',
)

# settings for apps

ACCOUNT_ACTIVATION_DAYS = 7 # One-week activation window; you may, of course, use a different value.
REGISTRATION_OPEN = True

OAUTH_CALLBACK_VIEW = 'key.views.oauth_callback'