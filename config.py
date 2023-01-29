import os
class Config(object):
    DEBUG = False
    TESTING = False
    MONGO_URI = ''
    GATEWAY_URL = ''
    S3_ACCESS_KEY = ''
    S3_SECRET_ACCESS_KEY = ''
    S3_BUCKET_REGION = ''
    S3_BUCKET_NAME = ''

class HerokuConfig(Config):
    if 'MONGO_URI' in os.environ:
        MONGO_URI = os.environ["MONGO_URI"]
    if 'GATEWAY_URL' in os.environ:
        GATEWAY_URL = os.environ["GATEWAY_URL"]
    if 'S3_ACCESS_KEY' in os.environ:
        S3_ACCESS_KEY = os.environ["S3_ACCESS_KEY"]
    if 'S3_SECRET_ACCESS_KEY' in os.environ:
        S3_SECRET_ACCESS_KEY = os.environ["S3_SECRET_ACCESS_KEY"]
    if 'S3_BUCKET_REGION' in os.environ:
        S3_BUCKET_REGION = os.environ["S3_BUCKET_REGION"]
    if 'S3_BUCKET_NAME' in os.environ:
        S3_BUCKET_NAME = os.environ["S3_BUCKET_NAME"]



