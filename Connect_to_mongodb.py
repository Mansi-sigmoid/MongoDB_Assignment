from pymongo import MongoClient

try:
    connection = MongoClient('localhost', 27017)
    print("Connection Successful!!")
except:
    print("Error in Connection")

db = connection['mflix']

collection = db['comments']

l1={"name" : "Amilea"}
l2={"name" : "jenelia"}

collection.insert_many([l1,l2])