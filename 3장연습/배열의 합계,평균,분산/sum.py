import numpy as np

arr = np.arange(1,9) # 1 ~ 8 1차원 배열 생성
print(arr) # [1 2 3 4 5 6 7 8]

z1 = arr.reshape(2,4)
print(z1) # [[1 2 3 4]
          # [5 6 7 8]]

print("열합계: ",np.sum(z1, axis=0)) # [ 6  8 10 12]
print("행합계: ",np.sum(z1, axis=1)) # [10 26]

print("열평균: ",np.mean(z1, axis=0)) # [3. 4. 5. 6.]
print("행평균: ",np.mean(z1, axis=1)) # [2.5 6.5]

print("모분산: ", np.var(z1))
print("표본분산: ", np.var(z1, ddof=1))

print("모표준편차: ", np.std(z1))
print("표본표준편차: ", np.std(z1, ddof=1))

a = np.std(z1) # 2.29128784747792
print(np.round(a,3)) #2.291