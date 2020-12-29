#function
def palindrom(strall):
    
    begin=[]
    
    strfinalbegin=""
    strfinalend=""
    
    for char in strall:
        if strall.count(char)>=2:
            begin.append(strall.pop(strall.index(char)))
    
    for char in begin:
        strfinalbegin+=char
        
    begin.reverse()
    begin.pop(0)
    for char in begin:
        strfinalend+=char
    
    print(strfinalbegin+strfinalend)

str1=str(input("Word 1 : "))
str2=str(input("Word 2 : "))
strall=str1+str2
strall=list(strall)

palindrom(strall)

