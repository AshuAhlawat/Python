#function
def intinputonly():
    
    while True:
        try:
            x = int(input("Integer input only : "))
            print("\n")
            break
        except Exception as e:
            print("\nError : ",e)
            print("Re-Enter Data\n")
        
    print("Successfully Submitted.")
    return x


print("\n")
print("Error Handeling using Try Except \n")

x=intinputonly()

        