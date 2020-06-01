import pymongo
from database_access import manufacturer

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
computer_parts_database = myclient["computer_parts"]


class DatabaseAccess:
    manufacturers_coll = computer_parts_database["manufacturers"]
    parts = computer_parts_database["parts"]
