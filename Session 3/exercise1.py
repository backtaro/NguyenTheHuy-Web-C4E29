from pymongo import MongoClient
from bson.objectid import ObjectId

uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(uri)
c4e = client.c4e
post = c4e["posts"]

my_post = [
    {
        "title" : "Get ready",
        "author" : "Huy Nguyen",
        "content" : "Brave yourself, winter is coming!"
    }
]

post.insert_many(my_post)