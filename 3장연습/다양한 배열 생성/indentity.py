import numpy as np

a = np.identity(3)
print(a)    # [[1. 0. 0.]
            # [0. 1. 0.]
            # [0. 0. 1.]]

b = np.identity(4, int)
print(b)    # [[1 0 0 0]
            # [0 1 0 0]
            # [0 0 1 0]
            # [0 0 0 1]]