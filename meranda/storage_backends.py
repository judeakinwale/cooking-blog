from storages.backends.s3boto3 import S3Boto3Storage

# For handling media files on aws s3
class MediaStorage(S3Boto3Storage):
    location = 'media'
    file_overwrite = False