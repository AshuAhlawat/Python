import pymongo
from pymongo import collection 

cluster = pymongo.MongoClient("mongodb+srv://Capti:1234@firstcluster.evs0f.mongodb.net/mongodb+srv://Capti:1234@firstcluster.evs0f.mongodb.net")

db = cluster["school"]
collection = db["class"]

query = {
    "_id":1
}

new = {
    "_id":0,
    "name":"God",
    "year":0,
    "group":None
}

collection.replace_one(query, new)

print("Successfully Replaced")