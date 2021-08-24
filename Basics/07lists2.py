leaderboards=[100,100,80,60,45,45]
print("Leaderboards : ",leaderboards,"\n")

x=int(input("Your Score : "))

leaderboards.append(x)
leaderboards.sort()
leaderboards.reverse()

distinct=[]

for leader in leaderboards:
    if leader not in distinct:
        distinct.append(leader)

x=1
for leader in distinct:
    y=leaderboards.count(leader)
    
    print(("Score : "+str(leader)+ "\tRank: "+ str(x)+"\n\n")*y)
    x+=1

        

