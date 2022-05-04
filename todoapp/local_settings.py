SECRET_KEY = 'django-insecure-!y$8w*tcy*g##ha@6(gmby_x_!a@(6z88rgf1qh^uzfv47085w'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'todoapp',
        'USER': 'postgres',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

