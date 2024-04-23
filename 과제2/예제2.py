import numpy as np

# 1부터 20 사이에서 1개의 숫자를 임의로 선택하여 저장
myNum = np.random.randint(1,21)
if myNum >= 10:
    print(myNum," P")
else:
    print(myNum, " NP")