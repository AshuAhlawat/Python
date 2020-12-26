names=[]
usernames=[]

entries=int(input("No of Entries : "))

for i in range(0,entries):
    names.append(input("Entry {} ".format(i+1)))

for j in range(0,entries):
    usernames.append(names[j].lower().replace(" ","_"))

for user in usernames:
    print (user.title().replace("_"," "))

print(usernames)

