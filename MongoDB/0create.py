import pymongo as mg

cluster = mg.MongoClient("mongodb+srv://Capti:1234@firstcluster.evs0f.mongodb.net/")

mydb = cluster["mydatabase"]
table = mydb["mydata"]

post = {"name" : "Ashu"}
table.insert_one(post)

dbs = cluster.list_database_names()
print(dbs)