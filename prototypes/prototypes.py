import sys

from django.conf import settings

settings.configure(
    DEBUG = True,
    SECRET_KEY = 'ph$ec4=hl8t6k-jo3uk@=xv2r-0wafm&t*q$+qei()ohytgjm$',
    ROOT_URLCONF = 'sitebuilder.urls',
    MIDDLEWARE_CLASSES=(
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ),
    INSTALLED_APPS = (
        'django.contrib.staticfiles',
        'sitebuilder'
    ),
    TEMPLATES = (
        {
            'BACKEND':'django.template.backends.django.DjangoTemplates',
            'DIRS':[],
            'APP_DIRS':True,
        },
    ),
    STATIC_URL = '/static/',
)

if __name__ == '__main__':
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)