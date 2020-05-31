import pymongo
from database_access import manufacturer

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

computer_parts_database = myclient["computer_parts"]
parts = computer_parts_database["parts"]

class DatabaseAccess:
    manufacturers_coll = computer_parts_database["manufacturers"]


#da = DatabaseAccess()
#mf = manufacturer.Manufacturer.init2(1, "Advanced Micro Devices", "AMD")
#da.manufacturers_coll.insert_one(mf.toObject())