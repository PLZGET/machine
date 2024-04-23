import numpy as np

a = np.tile(0,5)
print(a) # [0 0 0 0 0]

b = np.tile("A", 3)
print(b) # ['A' 'A' 'A']

c = np.tile([1,2,3], 3)
print(c) # [1 2 3 1 2 3 1 2 3]