import numpy as np

arr = np.arange(1,9)
print(arr) # [1 2 3 4 5 6 7 8]

print(arr.reshape(2,4)) # [[1 2 3 4]
                        # [5 6 7 8]]

print(arr) #[1 2 3 4 5 6 7 8] 원본이 변경되지는 않음

print()

re_arr = np.reshape(arr,(2,4))
print(re_arr)