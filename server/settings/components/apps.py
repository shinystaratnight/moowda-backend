INSTALLED_APPS = (
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',

    # Default django apps:
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # django-admin:
    'django.contrib.admin',

    # vendors
    'django_extensions',
    'django_filters',
    'rest_framework',
    'drf_yasg',
    'corsheaders',
    'admin_auto_filters',
    'health_check',
    'health_check.db',
    'health_check.cache',
    'health_check.storage',

    # apps
    'apps.core',
    'apps.topics',
    'apps.users',
)
