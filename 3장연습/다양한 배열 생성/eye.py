import numpy as np

a = np.eye(2)
print(a) # [[1. 0.]
         # [0. 1.]]

b = np.eye(N=2, M=5)
print(b) # [[1. 0. 0. 0. 0.]
         # [0. 1. 0. 0. 0.]]

c = np.eye(N=2, M=5, k=2)
print(c) # [[0. 0. 1. 0. 0.]
         # [0. 0. 0. 1. 0.]]