from pymongo import MongoClient
import json
from bson import ObjectId

try:
    connection = MongoClient('localhost', 27017)
except:
    print("Error in Connect")

db = connection['mflix']

collection = db['theaters']

upd_item_list = []

with open('sample_mflix/theaters.json') as f:
    for json_obj in f:
        if json_obj:
            upd_my_dict = json.loads(json_obj)
            upd_my_dict["_id"] = ObjectId(upd_my_dict["_id"]["$oid"])
            upd_my_dict["location"]["geo"]["coordinates"][0]=float(upd_my_dict["location"]["geo"]["coordinates"][0]["$numberDouble"])
            upd_my_dict["location"]["geo"]["coordinates"][1]=float(upd_my_dict["location"]["geo"]["coordinates"][1]["$numberDouble"])
            upd_item_list.append(upd_my_dict)

collection.insert_many(upd_item_list)





