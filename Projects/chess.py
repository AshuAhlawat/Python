                                #functions
    
#board
boarde=[]
def board(b_x,b_y):
    
    for y in range(b_y):
        row=[]
        for x in range(b_x):
            row.append(" ")
        boarde.append(row)
    
    look=""
    for y in boarde:
        for x in boarde[boarde.index(y)]:
            look+=("|"+x+"|  ")
        look+=("\n\n")
    print(look)
    
#rook
def rookattack(b_x,b_y,q_xy):
    q_xy=str(q_xy)
    q_x=int(q_xy[0])
    q_y=int(q_xy[1])
    
    for row in range(b_y):
        boarde[row][q_x-1]="*"
    for col in range(b_x):
        boarde[q_y-1][col]="*"
    
    boarde[q_y-1][q_x-1]="R"
    
    look=""
    for y in boarde:
        for x in boarde[boarde.index(y)]:
            look+=("|"+x+"|  ")
        look+=("\n\n")
    print(look)   
        
#bishop
def bishopattack(b_x,b_y,q_xy):
    boardb=[]
    q_xy=str(q_xy)
    q_x=int(q_xy[0])
    q_y=int(q_xy[1])
    
    
    
    boardb[q_y-1][q_x-1]="B"
    
    look=""
    for y in boardb:
        for x in boardb[boardb.index(y)]:
            look+=("|"+x+"|  ")
        look+=("\n\n")
    print(look)

                                        #main

b_x=int(input("Board's Dimensions \n x : "))
b_y=int(input(" y : "))

print("\n\n")

board(b_x,b_y)
q_xy=int(input("Location \n xy : "))

print("\n\n")

print("Rook's Attack \n\n")
rookattack(b_x,b_y,q_xy)

print("\n\n")

print("Bishop's Attack \n\n")
rookattack(b_x,b_y,q_xy)
