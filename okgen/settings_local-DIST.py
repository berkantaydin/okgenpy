from settings_default import *

# The backend to use for sending emails. For the list of available backends
# see https://docs.djangoproject.com/en/1.3/topics/email/.
EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
# The directory used by the file email backend to store output files.
EMAIL_FILE_PATH = '/tmp/django-mail'
# this email address would be used as default email from address For
# email that are beeing sent to maintainers.
DEFAULT_FROM_EMAIL = 'noreply@localhost'

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'bekowebmaster1@gmail.com'
EMAIL_HOST_PASSWORD = '94649464'

INSTALLED_APPS += ('debug_toolbar',)