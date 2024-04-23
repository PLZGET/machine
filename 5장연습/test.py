# 여기에 모든 5장 예제 적오놓은 예정임!

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
ts = pd.read_csv("C:/data2/ts.csv")
print(ts)
print()

# info() df의 정보 출력
print( ts.info() )
print()

# isnull() df의 결측치 확인
print( ts.isnull() )
print()

# df의 각 열별 결측치 개수 계산
print( ts.isnull().sum() )
print()

# df의 각 열별 결측치 비율 계산
print( ts.isnull().sum() / len(ts)) # len(ts) = 5
print()


# isna() df의 결측치 확인
print( ts.isna() )
print()

# isna() df의 결측치 비율 계산
print( ts.isna().sum() / len(ts) )
print()

# missingno 패키지 설치
# pip install missingno
import missingno as msno

# # 매트릭스 형태로 결측치값 시각화. 흰색으로 표시된 곳이 빈칸으로 추측되는 결측치 값
# msno.matrix(ts)
# plt.show()

# # 막대그래프 형태로 결측치값 시각화
# msno.bar(ts)
# plt.show()

# =================결측시 삭제(drop)해보기=================
ts.dropna() # df의 NaN이 있는 모든 데이터의 행을 삭제. 원데이터 변경X

# 결측치 삭제 후 결과물 저장 2가지 방법
# 1) 새로운 변수에 재할당 ex> ts_no_missing = ts.dropna()
# 2) inplace=True 옵션 사용


# how 매개변수: 어떤 조건을 입력하여 결측치를 삭제할 때 사용
# how = 'all' 옵션
ts.dropna(how='all') # 행에 있는 모든 값이 NaN일떄 해당 행 삭제

# how = 'any' 옵션 기본값임
ts.dropna(how='any') # 행에 하나의 NaN만 있어도 해당 행을 삭제. 기본값이 'any' 임

# dropna() 함수에서 축(axix)로 index(행)와 column(열)이 있음
# axix=0 or axix='index' : NaN 값이 포함된 행을 제거(기본값)
# axix=1 or axix='columns' : NaN 값이 포함된 열을 제거

ts['location'] = np.nan # ts에 location 이라는 열을 추가하는데 값을 모두 NaN으로 채움
ts.dropna(axis=1, how='all') # 열에 모든 값이 NaN이면 해당 열을 삭제
# locaiton 열이 삭제가 됨

# thresh 옵션 : dropna() 함수에서 데이터의 개수를 기준으로 삭제
# ex> thresh=1 : 데이터가 한 개라도 존재하는 행은 살림
ts.dropna(axis=0, thresh=1) # 행 기준으로 데이터가 1개라도 있으면 그 행은 살림
ts.dropna(thresh=5) # 데이터가 5개 이상 있어야 살림 4개 이하에 해당하는 행은 다 제거됨

# 일부 결측치만을 포함한 행 삭제하기
t1 = ts[ts.age.notnull()] # ts에서 age에 있는 NaN이 있는 행 삭제 후 t1에 저장
print(t1)

#=================결측치 채우기(fill)=================

# fillna(0) # 결측치를 0으로 채움
# ts.fillna(0) # ts에서 결측치를 0으로 채움
# ts["preTestScore"].fillna(ts["preTestScore"].mean(), inplace=True) # preTestScore의 결측치를 평균값으로 채움
# inplace=True 옵션을 사용하면 원본 데이터를 변경함

#  groupby함수와 transform 함수를 사용하여 변수(열)의 분포를 고려하여 결측치를 채움
# ts.groupby("gender")["preTestScore"].transform("mean") # gender별 preTestScore의 평균값을 구하고 결측치를 채움
# 그러니까 gender 별로 나누고 그 평균을 구하고 그 평균값으로 결측치를 채움


# ts["postTestScore"].fillna(ts.groupby("gender")["postTestScore"].transform("mean"), inplace=True)
# gender별 postTestScore의 평균값을 구하고 결측치를 채움


#=================이상치 처리=================
# 이상치(Outlier) : 데이터의 분포에서 벗어난 값

cl = pd.read_excel("C:/data2/class21.xlsx") # class21.xlsx 파일을 읽어옴
print(cl) 

# cl에 대한 age 상자그림 출력 (수평으로 그리고 그리드 없음)
cl.boxplot("age", vert=False, grid=False)
plt.show()
