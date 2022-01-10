#https://pymongo.readthedocs.io/en/stable/tutorial.html
import pymongo as mg

cluster = mg.MongoClient("mongodb+srv://Capti:1234@firstcluster.evs0f.mongodb.net/school?retryWrites=true&w=majority")
db = cluster["school"]
table = db["class"]

def main():
    
    try: 
        
        no=int(input("\nNo of documents to post : "))
        posts=[]
        1
        for i in range(no):
            regno = int(input("\nRegisteration Number : "))
            name = str(input(   "        Name         : "))
            year = int(input(   "  Year of admission  : "))
            group = str(input(  "        Group        : "))

            post = {"_id":regno, "name":name, "year":year, "group":group}
            posts.append(post)
        
        table.insert_many(posts)
        print("\n\n     SUCCESS")
        
    except :
    
        print("\n\n     WRONG DATA, RE-ENTER")
        main()

main()
