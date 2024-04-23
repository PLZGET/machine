import numpy as np

# 1부터 100 사이에서 40개의 서로 다른 정수를 임의로 선택하여 저장
myarr = np.random.randint(1,101,40)
print("myarr:\n",myarr)
print()

# 1-1) 만들어진 벡터를 사용하여 5행 8열의 행렬을 생성
print("예제1-1")
rearr = myarr.reshape(5,8)
print("reshpaed myarr:\n", rearr)
print()

# 1-2) 예제 1에서 생성된 행렬에서 2행과 3행만을 추출하고 저장
print("예제1-2")
rearr2 = rearr[1:3,:]
print("2~3 row in rearr:\n", rearr2)
print()

# 1-3) 예제 1에서 생성된 행렬에서 (1,4,7,8)열을 추출하여 저장
print("예제1-3")
rearr3 = rearr[:,[0,3,6,7]]
print("1,4,7,8 columns in rearr:\n", rearr3)
print()

# 1-4) 예제 1에서 생성된 행렬의 7번째 열의 평균과 분산 구하기
# rearr에서 7번쨰 열만 먼저 슬라이싱하고 변수 seventh_column_fr_rearr에 저장
print("예제1-4")
seventh_column_fr_rearr = rearr[:,6]
print("seventh_column_fr_rearr:\n",seventh_column_fr_rearr)
print()

# 7번째 열의 분산(variance)과 표준편차(standard deviation)
print("Variance of the seventh colum: ")
print(np.var(seventh_column_fr_rearr,axis=0))
print()

print("Standard deviation of the seventh colum: ")
print(np.std(seventh_column_fr_rearr,axis=0))
print()



