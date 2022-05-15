unsorted = ['17', '3142','3','1', '23','5', '3', '21', '45', '9']
lens = dict()


for el in unsorted:
    lens[len(el)] = []

for el in unsorted:
    key = len(el)
    val = lens[key]

    val.append(el)

    lens[key] = val

print(lens)


final = []

for key in sorted(lens):
    group = lens[key]

    final.extend(sorted(group))


print(final)