"""
Django settings for atlas project.

Generated by 'django-admin startproject' using Django 1.11.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import datetime

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'b!ydx6z#0z%59+*@%(sfj&fynlk&73eyh4$+58%*ft%kfm43-c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('ATLAS_DEBUG', False)

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'atlas.apps.AtlasConfig',
    'rest_framework',
    'rest_framework_swagger',
    'authentication',
    'corsheaders',
    'django.contrib.postgres',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'atlas.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'atlas.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('ATLAS_DB_NAME', 'atlas'),
        'USER': os.getenv('ATLAS_DB_USER', 'atlas'),
        'PASSWORD': os.getenv('ATLAS_DB_PASSWORD', 'atlas'),
        'HOST': 'localhost',
        'PORT': '',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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

PROFILE_PICTURES = [
    'https://vignette.wikia.nocookie.net/civilization/images/d/d9/Ahmad_al-Mansur_%28Civ5%29.png/revision/latest?cb=20130517204913',
    'https://vignette.wikia.nocookie.net/civilization/images/a/a9/Alexander_%28Civ5%29.png/revision/latest?cb=20121104231732',
    'https://vignette.wikia.nocookie.net/civilization/images/5/51/Ashurbanipal_%28Civ5%29.png/revision/latest?cb=20130324151252',
    'https://vignette.wikia.nocookie.net/civilization/images/8/8a/Askia_%28Civ5%29.png/revision/latest?cb=20130209203053',
    'https://vignette.wikia.nocookie.net/civilization/images/9/96/Attila_%28Civ5%29.png/revision/latest?cb=20130209201310',
    'https://vignette.wikia.nocookie.net/civilization/images/0/04/Augustus_Caesar_%28Civ5%29.png/revision/latest?cb=20140321004305',
    'https://vignette.wikia.nocookie.net/civilization/images/7/73/Bismarck_%28Civ5%29.png/revision/latest?cb=20121104231408',
    'https://vignette.wikia.nocookie.net/civilization/images/0/0a/Boudicca_%28Civ5%29.png/revision/latest?cb=20130617020109',
    'https://vignette.wikia.nocookie.net/civilization/images/d/d6/Casimir_III_%28Civ5%29.png/revision/latest?cb=20130706023813',
    'https://vignette.wikia.nocookie.net/civilization/images/4/40/Catherine_%28Civ5%29.png/revision/latest?cb=20121104234913',
    'https://vignette.wikia.nocookie.net/civilization/images/0/0c/Darius_I_%28Civ5%29.png/revision/latest?cb=20121104234220',
    'https://vignette.wikia.nocookie.net/civilization/images/7/7d/Dido_%28Civ5%29.png/revision/latest?cb=20121102235143',
    'https://vignette.wikia.nocookie.net/civilization/images/9/9b/Elizabeth_%28Civ5%29.png/revision/latest?cb=20121104225904',
    'https://vignette.wikia.nocookie.net/civilization/images/0/01/Enrico_Dandolo_%28Civ5%29.png/revision/latest?cb=20130703062050',
    'https://vignette.wikia.nocookie.net/civilization/images/4/4b/Gajah_Mada_%28Civ5%29.png/revision/latest?cb=20130517204635',
    'https://vignette.wikia.nocookie.net/civilization/images/3/36/Gandhi_%28Civ5%29.png/revision/latest?cb=20121104232443',
    'https://vignette.wikia.nocookie.net/civilization/images/3/39/Genghis_Khan_%28Civ5%29.png/revision/latest?cb=20130209193221',
    'https://vignette.wikia.nocookie.net/civilization/images/3/3e/Gustavus_Adolphus_%28Civ5%29.png/revision/latest?cb=20121105000218',
    'https://vignette.wikia.nocookie.net/civilization/images/f/f6/Haile_Selassie_%28Civ5%29.png/revision/latest?cb=20121104230458',
    'https://vignette.wikia.nocookie.net/civilization/images/3/35/Harald_Bluetooth_%28Civ5%29.png/revision/latest?cb=20130209210121',
    'https://vignette.wikia.nocookie.net/civilization/images/e/e2/Harun_al-Rashid_%28Civ5%29.png/revision/latest?cb=20121102223913',
    'https://vignette.wikia.nocookie.net/civilization/images/c/ca/Hiawatha_%28Civ5%29.png/revision/latest?cb=20121104232842',
    'https://vignette.wikia.nocookie.net/civilization/images/9/9e/Isabella_%28Civ5%29.png/revision/latest?cb=20130209203454',
    'https://vignette.wikia.nocookie.net/civilization/images/7/75/Kamehameha_%28Civ5%29.png/revision/latest?cb=20130209205558',
    'https://vignette.wikia.nocookie.net/civilization/images/3/36/Maria_I_%28Civ5%29.png/revision/latest?cb=20130711024955',
    'https://vignette.wikia.nocookie.net/civilization/images/6/61/Maria_Theresa_%28Civ5%29.png/revision/latest?cb=20121102224429',
    'https://vignette.wikia.nocookie.net/civilization/images/6/67/Montezuma_%28Civ5%29.png/revision/latest?cb=20121102233719',
    'https://vignette.wikia.nocookie.net/civilization/images/7/7b/Napoleon_%28Civ5%29.png/revision/latest?cb=20130209210237',
    'https://vignette.wikia.nocookie.net/civilization/images/1/12/Nebuchadnezzar_II_%28Civ5%29.png/revision/latest?cb=20130209203541',
    'https://vignette.wikia.nocookie.net/civilization/images/7/74/Oda_Nobunaga_%28Civ5%29.png/revision/latest?cb=20121104233221',
    'https://vignette.wikia.nocookie.net/civilization/images/5/58/Pacal_%28Civ5%29.png/revision/latest?cb=20121104233526',
    'https://vignette.wikia.nocookie.net/civilization/images/7/76/Pachacuti_%28Civ5%29.png/revision/latest?cb=20130209193945',
    'https://vignette.wikia.nocookie.net/civilization/images/f/f8/Pedro_II_%28Civ5%29.png/revision/latest?cb=20130705142148',
    'https://vignette.wikia.nocookie.net/civilization/images/9/94/Pocatello_%28Civ5%29.png/revision/latest?cb=20130703062309',
    'https://vignette.wikia.nocookie.net/civilization/images/4/4e/Ramesses_II_%28Civ5%29.png/revision/latest?cb=20130209203700',
    'https://vignette.wikia.nocookie.net/civilization/images/6/64/Ramkhamhaeng_%28Civ5%29.png/revision/latest?cb=20130209203845',
    'https://vignette.wikia.nocookie.net/civilization/images/4/44/Sejong_%28Civ5%29.png/revision/latest?cb=20130209204204',
    'https://vignette.wikia.nocookie.net/civilization/images/2/22/Shaka_%28Civ5%29.png/revision/latest?cb=20130703061853',
    'https://vignette.wikia.nocookie.net/civilization/images/f/ff/Theodora_%28Civ5%29.png/revision/latest?cb=20121102234510',
    'https://vignette.wikia.nocookie.net/civilization/images/4/47/Washington_%28Civ5%29.png/revision/latest?cb=20121102222807',
    'https://vignette.wikia.nocookie.net/civilization/images/9/95/William_%28Civ5%29.png/revision/latest?cb=20121103000315',
    'https://vignette.wikia.nocookie.net/civilization/images/3/34/Wu_Zetian_%28Civ5%29.png/revision/latest?cb=20130209204220',
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

AUTH_USER_MODEL = 'authentication.Account'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR,'static')

STATIC_URL = '/static/'

STATICFILES_DIRS = (

)


# Rest Framework permissions and authentication middleware
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
    'UNAUTHENTICATED_USER': None,
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10,
}

# Default JWT preferences
JWT_AUTH = {
    'JWT_ENCODE_HANDLER':
    'rest_framework_jwt.utils.jwt_encode_handler',

    'JWT_DECODE_HANDLER':
    'rest_framework_jwt.utils.jwt_decode_handler',

    'JWT_PAYLOAD_HANDLER':
    'rest_framework_jwt.utils.jwt_payload_handler',

    'JWT_PAYLOAD_GET_USER_ID_HANDLER':
    'rest_framework_jwt.utils.jwt_get_user_id_from_payload_handler',

    'JWT_RESPONSE_PAYLOAD_HANDLER':
    'rest_framework_jwt.utils.jwt_response_payload_handler',

    'JWT_SECRET_KEY': SECRET_KEY,
    'JWT_ALGORITHM': 'HS256',
    'JWT_VERIFY': True,
    'JWT_VERIFY_EXPIRATION': True,
    'JWT_LEEWAY': 0,
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=3),
    'JWT_AUDIENCE': None,
    'JWT_ISSUER': None,

    'JWT_ALLOW_REFRESH': False,
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7),

    'JWT_AUTH_HEADER_PREFIX': 'JWT',
}

ADMINS = [('Yigit Ozkavci', 'yigitozkavci8@gmail.com'),
          ('Esref Ozdemir', 'esref.ozdemir27@gmail.com'),
          ('Talha Nisanci', 's.talhanisanci@gmail.com'),
          ('Aykut Bozkurt', 'aykut___1995@hotmail.com')]
