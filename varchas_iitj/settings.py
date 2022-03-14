import os
from decouple import config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts.apps.AccountsConfig',
    'adminportal.apps.AdminportalConfig',
    'events.apps.EventsConfig',
    'main.apps.MainConfig',
    'registration.apps.RegistrationConfig',
    'sponsors.apps.SponsorsConfig',
    'ckeditor',
    'ckeditor_uploader',
    'widget_tweaks',
    'rest_framework',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'varchas_iitj.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'main.context_processors.add_variable_to_context',
            ],
        },
    },
]

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

WSGI_APPLICATION = 'varchas_iitj.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
]


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Calcutta'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/'

# CKEditor
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_RESTRICT_BY_USER = True
CKEDITOR_IMAGE_BACKEND = 'pillow'
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Basic',
        'width': '100%',
        'tabSpaces': 4,
        'mathJaxLib': 'https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-AMS_HTML',
        'toolbar_Basic': [
            {'name': 'clipboard', 'items': ['Cut', 'Copy', 'Paste',
                                            'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
            # {'name': 'editing', 'items': ['Find', 'Replace', '-', 'SelectAll']},
            {'name': 'basicstyles',
             'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
            {'name': 'formulae', 'items': ['Mathjax']},
            {'name': 'insert',
             'items': ['Image', 'Table', 'HorizontalRule', 'Smiley', ]},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', '-',
                       'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', ]},
            {'name': 'styles', 'items': [
                'Styles', 'Format', 'Font', 'FontSize']},
        ],
        'extraPlugins': ','.join([
            'uploadimage',
            'div',
            'autolink',
            'iframe',
            'embed',
            'embedsemantic',
            'autoembed',
            'autogrow',
            'uploadimage',
            'widget',
            'lineutils',
            'clipboard',
            'dialog',
            'dialogui',
            'mathjax',
            'codesnippet',
        ]),
    },
}


SESSION_ENGINE = 'django.contrib.sessions.backends.db'

AUTHENTICATION_BACKENDS = (
    ('django.contrib.auth.backends.ModelBackend'),
)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

APPEND_SLASH = True

EMAIL_HOST = config('EMAIL_HOST')
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL')

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}
