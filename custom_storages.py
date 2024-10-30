from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage
import boto3
import os


class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION

s3 = boto3.client('s3', 
                  aws_access_key_id=os.environ.get('AWS_ACCES_KEY_ID'), 
                  aws_secret_access_keys=os.environ.get('AWS_SECRET_ACCES_KEY')
                )

s3.put_object(Bucket='your-bucket-name', Key='test.txt', Body='Hello, world!')
