from pymongo import MongoClient

try:
    connection = MongoClient('localhost', 27017)
except:
    print("Error in Connection")

db = connection['mflix']

comments = db['comments']
# users = db['users']
# movies = db['movies']
# theaters = db['theaters']
# sessions = db['sessions']

# def top_ten_users_max_commnen(n):
#     result=comments.aggregate([{"$group": {"_id":{"name":"$name"},"total_commments":{"$sum":1}}},
#                               {"$sort":{"total_commments":-1}},
#                               {"$limit":n}])
#
#     for r in result:
#         print(r)
#
#
# top_ten_users_max_commnen(10)



# def top_ten_movies_having_most_comment(n):
#     result=comments.aggregate([{"$group": {"_id":{"name":"$movie_id"},"total_commments":{"$sum":1}}},
#                               {"$sort":{"total_commments":-1}},
#                               {"$limit":n}])
#
#     for r in result:
#         print(r)
#
# top_ten_movies_having_most_comment(10)
def comment_for_each_month_for_year(year):
    result=comments.aggregate(
        [{"$project": { "_id": 0,"date":{ "$toDate":{"$convert":{"input":"$date","to":"long"}}}}},
         {"$group":{"_id":{"year":{"$year":"$date"},"month":{"$month":"$date"}},"total_comments":{"$sum":1}}},
         {"$match":{"_id.year":{"$eq":year}}},
         {"$sort":{"_id.month":1}}
        ])

    for r in result:
        print(r)

comment_for_each_month_for_year(1978)






