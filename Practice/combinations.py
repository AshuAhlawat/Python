
def combinations(vals):
    if len(vals)==2:
        return [vals, list(reversed(vals))]
    
    combs = []
    
    for i in range(len(vals)):
        other = vals[:i]+vals[i+1:]

        other_combs = combinations(other)

        for o in other_combs:
            total = [vals[i]] + o 

            combs.append(total)

    return combs


x = [1,2,3,4,5,6]


combs = combinations(x)

for comb in combs:
    diff = comb[0] - 1
    for i in range(len(x)):
        if abs(comb[i] - (i+1)) == diff:
            pass
        else:
            diff = 0
            break

    if diff != 0:
        print(diff , comb)

