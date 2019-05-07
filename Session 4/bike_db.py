from pymongo import MongoClient

uri = "mongodb+srv://admin:admin@huynguyen3105-oqvrt.mongodb.net/test?retryWrites=true"

client = MongoClient(uri)

bike_db = client.bike_database

bike_coll = bike_db["bike_collection"]