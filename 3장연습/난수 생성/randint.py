import numpy as np

a = np.random.randint(10) # 0 ~ 9 사이 정수 난수 1개 생성
print(a) # 5

b = np.random.randint(0,10,3)
print(b) # [5 1 1]

c = np.random.randint(5, size=(2,5)) # 0~4 사이의 정수 난수 2x5 배열 생성
print(c) # [[0 3 1 0 2]
         # [4 3 4 3 1]]