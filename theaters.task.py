from pymongo import MongoClient

try:
    connection = MongoClient('localhost', 27017)
except:
    print("Error in Connection")

db = connection['mflix']

theaters = db['theaters']

def theaters_near_given_coordinates(lat,long):
    result=theaters.aggregate([
        {"$geoNear":{"near":{"type":"Point","coordinates":[-91.24,43.85]},
        "maxDistance":10000000,"distanceField":"distance"}},
        {"$project":{"location.address.city":1,"_id":0,"location.geo.coordinates":1}},
         {"$limit":8}])
    for i in result:
        print(i)

theaters_near_given_coordinates(-91.24,43.85)

#
# def city_with_max_theaters(n):
#     result=theaters.aggregate([
#         {"$group":{"_id":"$location.address.city","count":{"$sum":1}}},
#         {"$project":{"location.address.city":1,"count":1}},
#         {"$sort":{"count":-1}},
#         {"$limit":n}
#
#
#     ])
#
#     for i in result:
#         print(i)
#
# city_with_max_theaters(8)












