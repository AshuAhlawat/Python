import pymongo as mg
import pandas as pd

cluster = mg.MongoClient("mongodb+srv://Capti:1234@firstcluster.evs0f.mongodb.net/school?retryWrites=true&w=majority")

db = cluster["school"]
table = db["class"]

results = table.find({})
print(pd.DataFrame(results))

# results = table.find({"year":2020})
# for result in results:
#     print(result["name"],result["_id"])
    
# results = table.find_one({"_id":1})
# print(results)