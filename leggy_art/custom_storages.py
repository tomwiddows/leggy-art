# Import settings.py file
from django.conf import settings
# Import S3's Boto3 which is required for collectstatic to run
from storages.backends.s3boto3 import S3Boto3Storage


# Set storage for static files upon collectstatic
class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION


# Set storage for media files upon collectstatic
class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
