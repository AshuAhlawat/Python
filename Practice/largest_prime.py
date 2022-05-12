primes = [2,3]
for i in range(30000, 40000):
    no = 0
    for prime in primes:
        if i%prime==0:
            no = 1
            break
    
    if no:
        pass
    else:
        primes.append(i)

print(primes)