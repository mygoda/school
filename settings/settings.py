# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
import os
import json
from config import config

DATETIME_FORMAT = "Y-m-d H:i"
SESSION_COOKIE_AGE = 94608000 # cookie三年过期

AUTHENTICATION_BACKENDS = (
    'applications.users.backends.EmailBackend',
    'applications.users.backends.PhoneCheckBackend',
)

MAX_GRADE = config.get('max_grade', 1)

LOGIN_URL = "/users/login/"

AUTH_USER_MODEL = "users.User"

PROJECT_HOME = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

DEBUG = config.getboolean("django", "debug")
TEMPLATE_DEBUG = config.getboolean("django", "template_dubug")

ALLOWED_HOSTS = json.loads(config.get("django", "allowed_hosts"))
APP_HOST_NAME = config.get("django", "app_host_name")
SYSTEM_NAME = config.get("db", "db_table")

ADMINS = (
    ('Shadow', 'chenchiyuan03@gmail.com'),
)

EMAIL_TO = config.get("settings", "email_to")
EMAIL_FROM = config.get("settings", "email_from")

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': config.get("db", "engine"),
        'NAME': config.get("db", "db_table"),
        'USER': config.get("db", "username"),
        'PASSWORD': config.get("db", "password"),
        'HOST': '',
        'PORT': '',
    }
}

TIME_ZONE = 'Asia/Shanghai'

LANGUAGE_CODE = 'zh-cn'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = os.path.join(PROJECT_HOME, "media")

MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(PROJECT_HOME, 'static')

STATIC_URL = '/static/'

STATICFILES_DIRS = (
)


STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)

SECRET_KEY = 'dly31d$+kks@z_!jpie*zw3t=06_as+z(*q8&amp;j0e7p30-euon-'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'raven.contrib.django.raven_compat.middleware.SentryResponseErrorIdMiddleware',
)

ROOT_URLCONF = 'settings.urls'

WSGI_APPLICATION = 'settings.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_HOME, "templates"),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.request",
    "django.core.context_processors.i18n",
    'django.contrib.messages.context_processors.messages',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # third_parts
  #  'debug_toolbar',
    'grappelli.dashboard',
    'grappelli',
    # apps
    'applications.users',
    'applications.ueditor',
    'applications.weixin',
    'applications.teacher',
    'applications.parents',
    'applications.grade',
    'applications.activity',
    'applications.api',


    'django.contrib.admin',
    'django.contrib.admindocs',

    'django_extensions',

    'raven.contrib.django.raven_compat',
    'south',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(pathname)s %(lineno)s %(funcName)s %(message)s'
        },
    },
    'filters': {
        'info': {
            '()': 'libs.logs.InfoLevelFilter',
        },
        'warning': {
            '()': 'libs.logs.WarningLevelFilter'
        }
    },
    'handlers': {
        'sentry': {
            'level': 'ERROR',
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
        },
        'rotate_warning': {
            'level': 'WARNING',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(PROJECT_HOME, "data", "logs", "warning.log"),
            'when': 'D',
            'formatter': 'verbose',
            'filters': ['warning', ]
        },
        'rotate_info': {
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(PROJECT_HOME, "data", "logs", "info.log"),
            'when': 'D',
            'formatter': 'verbose',
            'filters': ['info', ]
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        '': {
            'level': 'DEBUG',
            'handlers': ['console', 'rotate_info', 'rotate_warning', 'sentry'],
            'propagate': False,
        },
        'django': {
            'level': 'ERROR',
            'handlers': ['console', 'rotate_info', 'rotate_warning'],
        },
        'django.request': {
            'level': 'DEBUG',
            'handlers': ['console', 'rotate_info', 'rotate_warning', 'sentry'],
            'propagate': False,
        },
        'applications': {
            'level': 'DEBUG',
            'handlers': ['console', 'rotate_info', 'rotate_warning', 'sentry'],
            'propagate': False,
        },
    },
}

INTERNAL_IPS = ['127.0.0.1']
GRAPPELLI_INDEX_DASHBOARD = 'settings.dashboard.CustomIndexDashboard'
GRAPPELLI_ADMIN_TITLE = u"青橙会议管理系统"
IMG_AVAILABLE_HOSTS = ['zoneke-img.b0.upaiyun.com', ]

UPYUN_BUCKET = config.get("upyun", "UPYUN_BUCKET")
UPYUN_USER = config.get("upyun", "UPYUN_USER")
UPYUN_PASS = config.get("upyun", "UPYUN_PASS")
IMG_HOST = config.get("upyun", "IMG_HOST")

UPYUN_BUCKET = config.get("upyun", "UPYUN_BUCKET")
UPYUN_USER = config.get("upyun", "UPYUN_USER")
UPYUN_PASS = config.get("upyun", "UPYUN_PASS")
IMG_HOST = config.get("upyun", "IMG_HOST")
IMG_FORM_SECRET_KEY = config.get("upyun", "IMG_FORM_SECRET_KEY")

UPYUN_FILE_BUCKET = config.get("upyun", "UPYUN_FILE_BUCKET")
UPYUN_FILE_USER = config.get("upyun", "UPYUN_FILE_USER")
UPYUN_FILE_PASS = config.get("upyun", "UPYUN_FILE_PASS")
FILE_HOST = config.get("upyun", "FILE_HOST")
FILE_FORM_SECRET_KEY = config.get("upyun", "FILE_FORM_SECRET_KEY")

UPYUN_BUCKET_DICT = {
    UPYUN_BUCKET: IMG_FORM_SECRET_KEY,
    UPYUN_FILE_BUCKET: FILE_FORM_SECRET_KEY
}


# WEIXIN
WX_MANGER_STATES = {
    "NO_CACHE": "applications.weixin.states.NoCacheState",
    "MENU": "applications.weixin.states.MenuEventState",
    "SUBSCRIBE": "applications.weixin.states.SubscribeEventState",
}

#raven
RAVEN_CONFIG = {
    'dsn': config.get("sentry", "dsn"),
    'auto_log_stacks': False,
}

#MQ
BROKER_URL = 'amqp://guest:guest@localhost:5672//'
CELERY_IMPORTS = ['applications.certificate.tasks']

# PINGXX
PINGXX_TEST_KEY = u"sk_test_X9CmvHuv10GKXr90WTvvnjLC"
PINGXX_KEY = u"sk_test_X9CmvHuv10GKXr90WTvvnjLC"

# SMS
SMS_ACCESS_KEY = config.get("sms", "accesskey")
SMS_SECRET_KEY = config.get("sms", "secretkey")

#SMS_GUODU
SMS_GUODU_USERNAME = config.get("sms_guodu", "guodu_username")
SMS_GUODU_PASSWORD = config.get("sms_guodu", "guodu_password")
SMS_GUODU_SERVER = config.get("sms_guodu", "guodu_server")
SMS_GUODU_PORT = config.get("sms_guodu", "guodu_port")
SMS_GUODU_PATH = config.get("sms_guodu", "guodu_path")

WEIXIN_CLOUD_PAYMENT_API_URL = config.get("pay", "WEIXIN_CLOUD_PAYMENT_API_URL")