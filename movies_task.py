from pymongo import MongoClient

try:
    connection = MongoClient('localhost', 27017)
except:
    print("Error in Connection")

db = connection['mflix']

movies = db['movies']

# def highest_IMDB_rating_n_movies(n):
#     result=movies.aggregate(
#         [{"$project":{"_id":0,"title":1,"imdb.rating":1}},
#          {"$sort":{"imdb.rating":-1}},
#          {"$limit":n}
#
#          ])
#
#     for r in result:
#         print(r)
#
# highest_IMDB_rating_n_movies(5)

# def movies_with_matching_string(n,string_match):
#     loop= [{"$addFields":{"tomatoes_Rating":"$tomatoes.viewer.rating","r":{"$cond":
#         {"if":{"$regexMatch":{"input":"$title","regex":string_match}},"then":"Y","else":"N"}}}},
#          {"$project":{"_id":0,"title":1,"tomatoes_rating":1,"r":1}},
#          {"$match":{"r":{"$eq":"Y"}}},
#          {"$sort":{"tomatoes_rating":-1}},
#          {"$limit":n}]
#     result=list(db.movies.aggregate(loop))
#     for r in result:
#         print(r)
#
# movies_with_matching_string(5,'the')

# def n_director_create_mx_movies(n):
#     result=movies.aggregate([{"$unwind":"$directors"},
#                              {"$group":{"_id":{"dir_name":"$directors"},"Movie_count":{"$sum":1}}},
#                              {"$project":{"dir_name":1,"Movie_count":1}},
#                              {"$sort":{"Movie_count":-1}},
#                              {"$limit":n}])
#
#     for r in result:
#         print(r)
#
#
# n_director_create_mx_movies(8)


# def top_n_director_mx_movie_in_year(year):
#     result=movies.aggregate([
#         {"$addFields":{"yr":{"$getField":{"field":{"$literal":"$numberInt"},"input":"$year"}}}},
#         {"$unwind":"$directors"},
#         {"$match":{"yr":{"$eq":year}}},
#         {"$group":{"_id":{"director_name":"$directors"},"count":{"$sum":1}}},
#         {"$project":{"director_name":1,"count":1}},
#         {"$sort":{"count":-1}},
#         {"$limit":1}
#     ])
#
#     for r in result:
#         print(r)
#
# top_n_director_mx_movie_in_year('1988')

#
# def top_n_director_mx_movie_in_genre(genre):
#     result=movies.aggregate([
#         {"$unwind":"$directors"},
#         {"$match":{"genres":{"$eq":genre}}},
#         {"$group":{"_id":{"director_name":"$directors"},"count":{"$sum":1}}},
#         {"$project":{"director_name":1,"count":1}},
#         {"$sort":{"count":-1}},
#         {"$limit":1}
#     ])
#
#     for r in result:
#         print(r)
#
# top_n_director_mx_movie_in_genre("Short")



# def N_top_movoies(n):
#     result=movies.aggregate([
#         {"$unwind":"$genres"},{"$sort":{"imdb.rating":-1}},
#         {"$group":{"_id":"$genres","title":{"$push":"$title"},
#                    "rating":{"$push":{"$getField":{"field":{"$literal":"$numberDouble"},"input":"$imdb.rating"}}}}},
#         {"$project":{"_id":1,"Movies":{"$slice":['$title',0,n]},
#         "ratings":{"$slice":["$rating",0,n]}}}])
#
#     for i in result:
#         print(i)
#
# N_top_movoies(3)

#
# def n_actor_starrred_in_max_Movies(n):
#     result=movies.aggregate(
#         [{"$unwind":"$cast"},
#          {"$group":{"_id":"$cast","count":{"$sum":1}}},
#          {"$project":{"cast":1,"count":1}},
#          {"$sort":{"count":-1}},
#          {"$limit":n}
#         ]
#     )
#     for r in result:
#         print(r)
#
# n_actor_starrred_in_max_Movies(6)

def top_n_actor_max_movie(n,genres):
    result=movies.aggregate(
        [{"$unwind":"$cast"},
         {"$match":{"genres":{"$eq":genres}}},
         {"$group":{"_id":{"actor_name":"$cast"},"count":{"$sum":1}}},
         {"$project":{"actor_name":1,"count":1}},
         {"$sort":{"count":-1}},
         {"$limit":n}]
    )
    for i in result:
        print(i)

top_n_actor_max_movie(6,"Short")








