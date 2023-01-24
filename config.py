import os
class Config(object):
    DEBUG = False
    TESTING = False
    
class HerokuConfig(Config):
    MONGO_URI = "mongodb+srv://MongoDB:N1mHcZvuzF8VJXLD@micro-courses-kuizu.1uhbtuv.mongodb.net/?retryWrites=true&w=majority"
    GATEWAY_URL = "https://hwnh2p84jl.execute-api.us-east-1.amazonaws.com/dev"


