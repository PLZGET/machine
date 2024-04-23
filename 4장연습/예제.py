import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

#  예제 1. genhlth 변수에 대해 적절한 방법을 이용하여 요약해보자. 범주형 자료의 경우에는 어떠한 요약 방법을 사용할 수 있는가?
# genhlth 변수는 질적자료이므로 
# 1차원 빈도표(frequency table), 막대도포(Bar Chart), 원도표(Pie Chart) 등의 표와 그래프를 이용한 요약 방법을 사용할 수 있다.

cdc = pd.read_csv("C:\data2\cdc.txt", sep=" ") #외부 텍스트 파일로부터 데이터프레임 생성
print(cdc) # 생성한 DF 출력
print("==============================================================\n")
#  예제 2. weight 변수에 대한 수치적 요약 값을 구해보자. 전체 응답자의 평균 몸무게는 얼마인가?
mean_weight = cdc['weight'].mean() # cdc.weight.mean()과 같음
print(f"전체 weight 평균: {mean_weight}")
print("==============================================================\n")
#  예제 3. weight 변수와 wtdesire 변수의 산점도를 그려보자. 두 변수 사이에는 어떠한 관계가 존재한다고 보여지는가? 두 변수의 상관계수는 무엇은 나타내고 있는가?
 # weight와 wtdesire 열 추출
weight = cdc['weight']
wtdesire = cdc['wtdesire']


# 산점도 그리기
plt.scatter(weight, wtdesire)
plt.xlabel('Weight')
plt.ylabel('Wtdesire')
plt.title('Weight vs Wtdesire Scatterplot')
plt.show()

# 상관계수 계산
corr_coef = np.corrcoef(weight, wtdesire) # weight.corr(wtdesire) 와 같음
print(f"Weight와 Wtdesire의 상관계수: {corr_coef}")
print("==============================================================\n") 

#  weight와 wtdesire 두 변수 사이에 강한 양의 상관관계가 있음을 보인다

#  예제 4. wtdesire 변수와 weight 변수의 차를 계산하여 새로운 변수 wdiff 를 만들어보자. wdiff 의 분포는 어떠한가? 
# 수치적 요약과 그래프 요약을 통해 살펴보자. 이것이 의미하는 바는 무엇인가?

# wdiff 변수 생성
cdc['wdiff'] = cdc['wtdesire'] - cdc['weight'] # cdc.widiff = cdc.wtdesire - cdc.weight 와 같음

# wdiff 변수 수치 요약
wdiff_desc = cdc['wdiff'].describe()
print(wdiff_desc)

# wdiff 변수 분포 시각화
plt.figure(figsize=(8, 6))
plt.hist(cdc['wdiff'], bins=20, edgecolor='black')
plt.xlabel('wdiff')
plt.ylabel('Frequency')
plt.title('Distribution of wdiff')
plt.show()

# 예제 5. age 변수를 이용하여 히스토그램을 그려보자. 그리고 구간의 수를 50, 100으로 바꿔가며 동일한 히스토그램을 그린 후 비교해보자. 
#  (참고) 히스토그램은 자료의 형태를 파악하기 위한 쉬운 방법이지만 구간의 수가 달라짐에 따라 그 모양이 조금씩 달라질 수 있다.

# age 변수 추출
age = cdc['age']

# 구간 수 20으로 히스토그램 그리기
plt.figure(figsize=(10, 6))
# plt.subplot(1, 3, 1)
# plt.hist(age, bins=20, edgecolor='black')
# plt.title('Histogram (bins=20)')

# 구간 수 50으로 히스토그램 그리기
plt.subplot(1, 2, 1)
plt.hist(age, bins=50, edgecolor='black')
plt.title('Histogram (bins=50)')

# 구간 수 100으로 히스토그램 그리기
plt.subplot(1, 2, 2)
plt.hist(age, bins=100, edgecolor='black')
plt.title('Histogram (bins=100)')

plt.show()




# 그래프를 이용한 "양적자료" 요약

# 1) 히스토그램
# - 일변량 자료의 분포
# 2) 상자그림
# - 데이터 분포
# - 자료의 산포도 및 대칭성의 정도, 이상치의 유무
# 3)줄기-잎 그림(stem and leaf plot)
# - 전체 자료를 display하는 그래프임

# 그래프(표)를 이용한 "질적자료" 요약

# 1) 1차원빈도표(frequency table)
# - 질적 자료의 빈도표(수치표) (Pandas)
# (sr_data.value_counts()랑 groupby() + size()로 구할 수 있음)

# 2) 막대도표
# - 각 범주별 빈도를 막대로 표현

# 3) 원도표
# - 질적자료의 각 범주별 빈도를 원의 형태로 표현
# - 각 범주별 빈도표(frequency table)을 이용해 원도표를 그릴 수 있다

# @ plot 함수가 있어 (Pandas 데이터프레임)
# table = iris.groupby("species").size() //종별 빈도수 표
# table.polt( kind='bar', x = table.index, y=table.valuses,
# title='bar chart of iris.species')

# table = iris.groupby("species").size()
# table.plot(kind='pie',
# x=table.index, y=table.values, 
# title='bar chart of iris.species', 
# autopct='$1.1f%%')


# describe 함수(pandas 데이터프레임)
# df_name.describe()
# - df의 양적 변수들에 대한 간단한 요약통계량 값 출력
# df_name.describe(include='object')
# - df의 질적 변수에 대한 요약 통계량 값 출력
# df_name.describe(include='all')
# - 양적, 질적 변수 모두에 대한 요약 통계량 값 출력
# df_name.변수명.describe()
# - 지정된 변수에서 양적, 질적에 대한 요약통계량 출력
# df_name[['변수1', ... '변수2']].describe()
# - 지정된 여러 변수에 대한 양적, 질적 ~~


# Pandas 데이터프레임에서 기술통계량 함수
#  df_name.변수명.함수를 사용하여 양적자료의 기술통계량을 구할 수 있다!
