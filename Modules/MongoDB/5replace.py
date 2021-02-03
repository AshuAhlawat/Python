import pymongo
from pymongo import collection 


client = pymongo.MongoClient("mongodb+srv://Capti:1234@firstcluster.evs0f.mongodb.net/school?retryWrites=true&w=majority")

db = client["school"]
collection = db["class"]

query = {
    "_id":1
}

new = {
    "_id":1,
    "name":"God",
    "year":0,
    "group":None
}

collection.replace_one(query, new)

print("Successfully Replaced")