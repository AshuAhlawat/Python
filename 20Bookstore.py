#Library
subAvail = ["Maths","Physics","Chemistry"]
mathsAvail = ["10th","11th","12th","1st Year"]
phyAvail = ["10th","11th","12th"]
chemAvail = []

#main
user = input("Bookstore ID : ")
print("Welcome " + user + ", just write the position of the book you want \n-- " + str(subAvail))

subAskedint = int(input(""))
subNum = subAskedint-1
subAsked = subAvail[subNum]

if subAsked in subAvail:
    x = 0
    while subAsked != subAvail[x]:
        x=x+1
    
    if subNum == 0 :
        subSelected = mathsAvail 
    elif subNum == 1 :
        subSelected = phyAvail
    elif subNum == 2 :
        subSelected = chemAvail 
    
    p = ("We have {} books for  {}")
    print(p.format(len(subSelected),subAvail[x]))
    
    userReply = input("Wanna see the books available ? (y/n) -- ")
    if userReply == "y" :
        for r in subSelected :
            print(r)
    else :
        print("whaa-WHY?? why were u even here?!")
else :
    print("Sorry, we don\'t have that subject")