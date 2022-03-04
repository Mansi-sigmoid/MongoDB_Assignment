from pymongo import MongoClient
import json
from bson import ObjectId

try:
    connection = MongoClient('localhost', 27017)
except:
    print("Error in Connect")

db = connection['mflix']
collection = db['users']
upd_item_list = []

with open('sample_mflix/users.json') as f:
    for obj in f:
        if obj:
            upd_my_dict = json.loads(obj)
            upd_my_dict["_id"] = ObjectId(upd_my_dict["_id"]["$oid"])
            upd_item_list.append(upd_my_dict)

collection.insert_many(upd_item_list)





