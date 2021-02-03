import pymongo

client = pymongo.MongoClient("mongodb+srv://Capti:1234@firstcluster.evs0f.mongodb.net/school")
db = client["school"]
collection = db["class"]

# to delete all
# collection.delete_many({})
query = {
    "name":"Randomn"
}

collection.delete_one(query)

print("delete successful")