from pymongo import MongoClient

client = MongoClient("localhost", 27017)

db = client["progmod"]

class MongoService:
    @staticmethod
    def get_all_from_collection(collection):
        return db[collection].find()