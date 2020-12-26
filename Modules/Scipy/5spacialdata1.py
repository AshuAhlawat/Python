import matplotlib.pyplot as plt
import scipy.spatial as sp
import numpy as np

points = np.random.normal(scale =20,size = (40,2))

for i in range(len(points)):
    for j in range(2):
        points[i][j]=int(points[i][j])

print(points)

simplices = sp.Delaunay(points).simplices

plt.triplot(points[:, 0],points[:, 1], simplices)
plt.scatter(points[:, 0],points[:, 1], c = "r")

plt.show()

hull = sp.ConvexHull(points)
hull_points = hull.simplices

plt.scatter(points[:, 0], points[:, 1], c = "r")

for simplex in hull_points:
    plt.plot(points[simplex,0], points[simplex,1], 'k-')

plt.show()