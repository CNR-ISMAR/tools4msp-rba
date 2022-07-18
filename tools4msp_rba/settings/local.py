# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'elisabeth'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


DATABASES = {
    'default': {
         'ENGINE': 'django.contrib.gis.db.backends.postgis',
         'NAME': 'tools4msp_rba',
         'USER': 'ecoads',
         'PASSWORD': 'bubu',
         'HOST': 'localhost',
    },

}