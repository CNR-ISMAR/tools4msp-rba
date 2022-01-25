from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '68%g6l%*kz!iyus4$-@v9#^*s@$zc(-bqdrm$xnrrwh%@%*llb'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['localhost'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *
except ImportError:
    pass
