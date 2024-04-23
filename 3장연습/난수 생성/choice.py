import numpy as np

a = np.random.choice(10, 5) # 0 ~ 9 사이에서 5개의 표본 복원추출해서 배열로 만듬
print(a) # [2 5 9 6 5]

b = np.random.choice(10, 5, replace=False) # 0 ~ 9 사이에서 5개의 표본 비복원추출
print(b) # [2 4 1 7 8]

c = np.random.choice(5, 3, p=[0.7, 0, 0, 0.1, 0.2]) # 각 요소의 추출확률을 정한거임
print(c) # [4 0 0]

x = np.arange(1, 101) # 1 ~ 100 배열 생성
d1 = np.random.choice(x, 3)
d2 = np.random.choice(x, size=3)
print(d1) # [74 57 16]
print(d2) # [42 33 17]


