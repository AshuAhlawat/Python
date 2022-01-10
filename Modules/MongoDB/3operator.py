import pymongo as mg

cluster = mg.MongoClient("mongodb+srv://Capti:1234@firstcluster.evs0f.mongodb.net/school?retryWrites=true&w=majority")

db = cluster["school"]
collection = db["class"]

query = {
    "name":{ "$in": ["Ashu", "Ashwani Ahlawat"]},
    "$or":[
        {
            "year":{ "$gt": 2000}
            #$eq,$lt,$gte,$ne,$nin
        },
        {
            "group":{"$regex":"^KO"}
        }
        
    ]
}

results = collection.find(query)
        
for result in results:
    print(result)