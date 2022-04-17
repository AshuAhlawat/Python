def ipToBin(n):
    out = []
    for i in n:
        i = int(i)
        binary = bin(i).replace("0b", "")

        while len(binary)!=8:
            binary = "0"+binary

        out.append(binary)
    return out

def ipToDec(n):
    out = []

    for i in n:
        out.append(int(i,base=2))

    final = str(out[0])

    for i in range(1,len(out)):
        final+="."+str(out[i])

    return final

def cidrToBin(n):
    n=int(n)
    out = ""

    for i in range(n):
        out+="1"

    for i in range(32-n):
        out+="0"

    final = []

    for i in range(4):
        final.append(out[i*8:(i+1)*8])

    return final
    
def network(ip,cidr):

    first = []
    last = []
    x=0
    for byte in range(4):
        ans1 = ""
        ans2 = ""
        for bit in range(8):
            if cidr[byte][bit]=="1":
                ans1+= ip[byte][bit]
                ans2+= ip[byte][bit]
            else:
                ans1+="0"
                ans2+="1"
                x+=1

        first.append(ans1)
        last.append(ans2)
    
    return first,last,2**(x)


# hello hi

addr = input("Address: ")

ip, cidr = addr.split("/")
ip = ip.split(".")

ip = ipToBin(ip)
cidr = cidrToBin(cidr)

print("   IP: ",ip)
print(" CIDR: ",cidr)

first,last,net_range = network(ip,cidr)

print("\nFirst: ",first, ipToDec(first))
print(" Last: ",last, ipToDec(last))
print("Range: ", net_range)

