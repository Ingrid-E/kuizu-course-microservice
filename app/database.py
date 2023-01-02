from pymongo import MongoClient
from config import HerokuConfig

def dbConnection():
    try:
        client = MongoClient(HerokuConfig.MONGO_URI)
        db = client['Courses']
    except ConnectionError:
        print("Failed to connect to database")
    return db


