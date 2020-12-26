import numpy as np
import scipy.sparse as sp
from scipy.sparse.csr import csr_matrix

lis = [[0, 0, 0], [0, 0, 1], [1, 0, 2]]
arr = np.array(lis)

print(sp.csr_matrix(arr), "\n\n", sp.csr_matrix(arr).data, "\n\n", sp.csr_matrix(arr).count_nonzero())

sp.csr_matrix(arr).eliminate_zeros()
#eliminating duplicate enteries mat.sum_duplicates()
print(sp.csr_matrix(arr))