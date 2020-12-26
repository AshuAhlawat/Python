import scipy.spatial as sp

p1 = (1, 0)
p2 = (10, 2)

res = sp.distance.euclidean(p1, p2)
print(res)

res = sp.distance.cityblock(p1, p2)
print(res)

res = sp.distance.cosine(p1, p2)
print(res)

p1 = (True, False, True)
p2 = (False, True, True)

res = sp.distance.hamming(p1, p2)
print(res)
