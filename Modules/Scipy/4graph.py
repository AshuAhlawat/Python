import numpy as np
import scipy.sparse as sp

arr = np.array([
  [0, 1, 2],
  [1, 0, 0],
  [2, 0, 0]
])

newarr = sp.csr_matrix(arr)

#all connected components
print(sp.csgraph.connected_components(newarr))
#shortest path from one element to another
print(sp.csgraph.dijkstra(newarr, return_predecessors = True, indices = 0))
#shortest path between all pairs of elements
print(sp.csgraph.floyd_warshall(newarr, return_predecessors=True))
#same as flyod_warshall but for even negative weights
print(sp.csgraph.bellman_ford(newarr, return_predecessors=True, indices=0))
#tells depth of the graph
arr = np.array([
  [0, 1, 0, 1],
  [1, 1, 1, 1],
  [2, 1, 1, 0],
  [0, 1, 0, 1]
])
print(sp.csgraph.depth_first_order(newarr, 1))
#tells breadth of the graph
print(sp.csgraph.breadth_first_order(newarr, 1))