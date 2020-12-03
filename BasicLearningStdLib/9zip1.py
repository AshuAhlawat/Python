x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = []
for point in zip(labels,x_coord,y_coord,z_coord):
    points.append("{} : {},{},{}".format(*point))
    justpoints=list(zip(x_coord,y_coord,z_coord))

for point in points:
    print(point)

print("Just Coordinates : {}".format(justpoints))

zplane={}

for point in points:
    zplane=dict(zip(zip(x_coord,y_coord),labels))

print("Z plane points : {}".format(zplane))