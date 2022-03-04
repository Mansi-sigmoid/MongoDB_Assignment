from pymongo import MongoClient

try:
    connection = MongoClient('localhost', 27017)
except:
    print("Error in Connection")

db = connection['mflix']

comments = db['comments']
users = db['users']
movies = db['movies']
theaters = db['theaters']
sessions = db['sessions']


def new_comments(mylist_comment):
    comments.insert_one(mylist_comment)

def new_movie(mylist_movie):
    comments.insert_one(mylist_movie)

def new_theater(mylist_theater):
    comments.insert_one(mylist_theater)

def new_user(mylist_user):
    comments.insert_one(mylist_user)






mylist_comment = [
    {
        "name": "Amy",
        "email": "Amy@fakegmail.com",
        "text": "This is my fav movie",
        "date": "08-02-2022"
    }
]

