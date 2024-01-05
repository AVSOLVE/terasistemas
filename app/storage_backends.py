from django.conf import settings
from django.contrib.staticfiles.storage import ManifestStaticFilesStorage
from django.core.files.storage import get_storage_class
from storages.backends.s3 import S3Storage
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Storage):
    location = "static"
    default_acl = "public-read"

    # bucket_name = settings.STATIC_BUCKET_NAME
    # endpoint_url = settings.STATIC_ENDPOINT_URL


class PublicMediaStorage(S3Storage):
    location = "media"
    default_acl = "public-read"
    file_overwrite = False


class MediaStorage(S3Storage):
    location = "media-private"
    default_acl = "private"
    file_overwrite = False
