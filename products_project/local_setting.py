# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-o()6hyvv^yeq8*i+2x8i-bx^ndnb!qu5!nb=s67@oe-3@sjr2z'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'products_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'password'
    }
}