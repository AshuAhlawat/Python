with open("./flag.enc","r") as f:
    x = f.read()
    targets = x.split(" ")

fib = [1,1]
for i in range(2, 11):
	fib.append(fib[i - 1] + fib[i - 2])

def c2f(n):
	b = ''
	for i in range(10, -1, -1):
		if n >= fib[i]:
			n -= fib[i]
			b += '1'
		else:
			b += '0'
	return b

ptval= []
ptkey= []
for i in range(32,127):
    ptkey.append(chr(i))
    ptval.append(c2f(i))
    
for target in targets:
    for val in ptval:
        if target==val:
            print(ptkey[ptval.index(val)],end="")


