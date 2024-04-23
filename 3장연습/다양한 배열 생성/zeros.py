import numpy as np

a = np.zeros(5)
print(a) # [0. 0. 0. 0. 0.]

b = np.zeros(shape=(2,3))
print(b) # [[0. 0. 0.]
         # [0. 0. 0.]]

c = np.zeros(shape=(2,3), dtype=int)
print(c) # [[0 0 0]
         # [0 0 0]]