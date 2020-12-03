#functions
def areaof4(l,b):
    ans=int(l)*int(b)
    
    return ans

def areaof4s(s):
    return areaof4(int(s),int(s))

def areaof3(b,h):
    ans =int(b)*int(h)/2
    
    return ans

def areaofc(r):
    ans =22*int(r)*int(r)/7
    
    return ans

#main

shapes=["Triangle", "Square", "Rectangle", "Circle"]
nums=[]

for i in range(1,len(shapes)+1):
    nums.append(i)

shapes=dict(zip(shapes,nums))

print(shapes)
operation=int(input("Location of Shape  : "))

for shape in shapes:
    if operation>len(shapes):
        print("Not allowed bro.....")
        break
    if shapes[shape]==operation:
        x=shape
        break

print("{} dimetions -- ".format(x))
if operation==1:
    b = input("Base : ")
    h = input("Height : ")
    print("\n Area : {}".format(areaof3(b,h)))
elif operation==2:
    s = input("Side : ")
    print("\n Area : {}".format(areaof4s(s)))
elif operation==3:
    l=input("Length : ")
    b=input("Breadth : ")
    print("\n Area : {}".format(areaof4(l,b)))
else:
    r=input("Radius : ")
    print("\n Area : {}".format(areaofc(r)))