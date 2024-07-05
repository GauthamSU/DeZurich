from .base import *

DEBUG = env.bool('DJANGO_DEBUG', default=False)

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["*"])

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DATABASE_NAME'),
        'USER': env('DATABASE_USER'),
        'PASSWORD': env('DATABASE_PASSWORD'),
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}



# Cross-Origin Resource Sharing settings (CORS)

CORS_ALLOWED_ORIGINS = ['http://127.0.0.1:8000', 'https://dezurich.gauthamupadhyaya.in']
