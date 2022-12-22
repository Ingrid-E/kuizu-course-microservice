import os
class Config(object):
    DEBUG = False
    TESTING = False
    MONGO_URI = ''
    GATEWAY_URL = ''
    PORT = 3001
    
class HerokuConfig(Config):
    if 'MONGO_URI' in os.environ:
        MONGO_URI = os.environ["MONGO_URI"]
    if 'GATEWAY_URL' in os.environ:
        GATEWAY_URL = os.environ["GATEWAY_URL"]
    if 'PORT' in os.environ:
        PORT = os.environ["PORT"]
