from pathlib import Path

# ============================
# مسار المشروع BASE_DIR
# ============================
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-oks87q08h9ccv0khri6m^yx0mi+fd4!4rq$cpfo6ejans_egj%'
DEBUG = True

ALLOWED_HOSTS = []

# ============================
# التطبيقات المثبّتة
# ============================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # تطبيقات المشروع
    'core',
    'accounts',
    'catalog',
    'cart',
    'orders',
    'payments',
    'marketing',
]

# ============================
# الميدلويرات
# ============================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    # دعم اللغة العربية
    'django.middleware.locale.LocaleMiddleware',

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'vogastyle.urls'

# ============================
# القوالب Templates
# ============================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        # ⭐⭐ جميع مسارات القوالب بناءً على مجلداتك ⭐⭐
        'DIRS': [
            BASE_DIR / 'templates',
            BASE_DIR / 'templates/core-templates',
            BASE_DIR / 'templates/accounts-templates',
            BASE_DIR / 'templates/cart-templates',
            BASE_DIR / 'templates/catalog-templates',
            BASE_DIR / 'templates/orders-templates',
            BASE_DIR / 'templates/payments-templates',
            BASE_DIR / 'templates/marketing-templates',
        ],

        # نستخدم APP_DIRS = False لأننا نحدد المسارات يدويًا
        'APP_DIRS': False,

        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                # دعم media في القوالب
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'vogastyle.wsgi.application'

# ============================
# قاعدة البيانات (SQLite)
# ============================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ============================
# التحقق من كلمات المرور
# ============================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ============================
# اللغة والمنطقة الزمنية
# ============================
LANGUAGE_CODE = 'ar'
TIME_ZONE = 'Asia/Riyadh'

USE_I18N = True
USE_TZ = True

# ============================
# الملفات الثابتة Static
# ============================
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / "static",      # المجلد الصحيح داخل vogastyle
]

STATIC_ROOT = BASE_DIR.parent / "staticfiles"  # تجميع الإنتاج

# ============================
# ملفات الوسائط Media
# ============================
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"

# ============================
# الإعداد الافتراضي
# ============================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
