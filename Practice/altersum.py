list1 = [1,5,10,15,20,25]
list2 = [2,4,5,9,15]

def altersum(list1,list2):
    print(list1,list2)
    sum = 0

    for i1 in range(len(list1)):
        for i2 in range(len(list2)):
            if list1[i1]==list2[i2]:
                
                sum1=0
                sum2=0
                    
                for i in range(i1+1):
                    sum1+=list1[i]
                for i in range(i2+1):
                    sum2+=list2[i]

                if sum1>=sum2:
                    sum+=sum1
                else:
                    sum+=sum2

                for i in range(i1+1):
                    list1.pop(0)
                for i in range(i2+1):
                    list2.pop(0)

                return sum+altersum(list1,list2)
    
    sum1 = 0
    sum2 = 0
    
    for i in list1:
        sum1+=i 
    for i in list2:
        sum2+=i
    
    if sum1>=sum2:
        return sum1
    else:
        return sum2
    
    return 0

        
        
         
            
print(altersum(list1,list2))