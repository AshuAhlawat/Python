import  pymongo

username = str(input("Username : "))
password = str(input("Password : "))

cluster = pymongo.MongoClient("mongodb+srv://"+username+":"+password+"@firstcluster.evs0f.mongodb.net/school?retryWrites=true&w=majority")

db = cluster["school"]
collection = db["class"]

query = {
    "_id":1
}

changes = {
    "$set": {"name":"God", "modified": "$NOW"}
    #"$currentDate": {"lastModified":True}
}

collection.update_one(query, changes)
#collection.update_many(query, changes)

print("\nSuccessfully Updated")