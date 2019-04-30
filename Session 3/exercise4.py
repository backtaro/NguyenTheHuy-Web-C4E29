from pymongo import MongoClient
from bson.objectid import ObjectId

uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(uri)
c4e = client.c4e
river = c4e["river"]

# Exercise 5:
all_river = river.find()

for i in all_river:
    if i['continent'] == 'Africa':
        print(i)

# Exercise 6:
for n in all_river:
    if n['continent'] == 'S. America' and n['length'] < 1000:
        print(n)