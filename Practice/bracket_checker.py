def is_well_paired(value):
    check = []
    
    if value[0]==")":
        check.append(0)
    
    else:
        for i in value:
            if i == "(":
                check.append(0)
                
            else:
                pt = len(check)-1
                while True:
                    if check[pt]==0:
                        check[pt]=1
                        break
                    else:
                        pt -= 1
                        
                    if pt<0:
                        check.append(0)
                        break
    
    print(check)
    return all(check)
                
    
        
print(is_well_paired("(()())"))
print(is_well_paired("(())())"))
print(is_well_paired("((()())(()))"))
print(is_well_paired("(()))()("))
print(is_well_paired(")(())("))