import numpy as np
import pandas as pd
import missingno as missingno
import matplotlib.pyplot as plt

# 예제1. major.xlsx 파일을 읽어서 판다스 데이터프레임 major를 생성하시오
major = pd.read_excel("C:/data2/major.xlsx")
print(major)
# 예제2. 주어진 데이터값의 결측치를 탐색하시오. 
print("\n결측치 탐색\n")
print(major.isnull())

print(major.isnull().sum())


# 예제3. 변수 ‘글로컬영어‘의 결측치를 숫자 정수 0으로 채우시오. 
print("결측치 채우기")
print(major["글로컬영어"].fillna(0))

# 예제5. major 데이터프레임에 중복데이터가 있는지 확인하시오.
print(major[major.duplicated(keep=False)]) 

# 예제6. 중복데이터를 제거하시오. 제거된 인덱스에 번호도 새롭게 부여
print(major.drop_duplicates(subset=None, keep=False, ignore_index=True, inplace=False))


