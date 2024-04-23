import matplotlib.pyplot as plt
import pandas as pd

cdc = pd.read_csv("C:\data2\cdc.txt", sep=" ") #외부 텍스트 파일로부터 데이터프레임 생성
print(cdc) # 생성한 DF 출력

print("df에서 변수 불러오는 방법")
print("df.변수명으로 출력:\n",cdc.age) # df.변수명
print("df[변수명]으로 출력:\n", cdc['age']) # df['변수명']

# loc()함수와 iloc()함수 차이
# loc()함수: 인덱스 기준으로 개체 선택(끝값 포함임!)
print(cdc.loc[1:2,:]) # 인덱스 기준으로 1,2 행 출력됨

# iloc()함수: 행번호 기준으로 개체 선택(끝값 포함안함!)
print(cdc.iloc[0:1,:]) #행 번호 기준인데 0번쨰 행이니까 1행 출력


