from pymongo import MongoClient
from config import DevConfig

def dbConnection():
    try:
        client = MongoClient(DevConfig.MONGO_URI)
        db = client['Courses']
    except ConnectionError:
        print("Failed to connect to database")
    return db


