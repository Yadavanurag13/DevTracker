from pathlib import Path

from zango.config.settings.base import *  # noqa: F403


BASE_DIR = Path(__file__).resolve().parent.parent


class AttrDict(dict):
    """
    A dictionary subclass for managing global settings with attribute-style access.

    This class allows getting and setting items in the global namespace
    using both attribute and item notation.
    """

    def __getattr__(self, item):
        return globals()[item]

    def __setattr__(self, item, value):
        globals()[item] = value

    def __setitem__(self, key, value):
        globals()[key] = value


# Call setup_settings to initialize the settings
settings_result = setup_settings(AttrDict(vars()), BASE_DIR)

# Setting Overrides
# Any settings that need to be overridden or added should be done below this line
# to ensure they take effect after the initial setup

SECRET_KEY = "django-insecure-6fjr+2ki7t4jdsgqtm^0mxb9fqnyn^e0lc-m!$pt5l4nec)8!t"  # Shift this to .env


# To change the media storage to S3 you can use the BACKEND class provided by the default storage
# To change the static storage to S3 you can use the BACKEND class provided by the staticfiles storage
# STORAGES = {
#     "default": {"BACKEND": "zango.core.storage_utils.S3MediaStorage"},
#     "staticfiles": {"BACKEND": "zango.core.storage_utils.S3StaticStorage"},
# }


# INTERNAL_IPS can contain a list of IP addresses or CIDR blocks that are considered internal.
# Both individual IP addresses and CIDR notation (e.g., '192.168.1.1' or '192.168.1.0/24') can be provided.
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'yadavanurag1310@gmail.com'
EMAIL_HOST_PASSWORD = 'jjtk yvzz xxhh oznw'