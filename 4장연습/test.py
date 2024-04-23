import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# from stemgraphic import stem_graphic
gender = np.array(['M','M','M','M',
                    'M','M','M','M',
                    'F','F','F','F','F',
                    'F','F','F','F','F'])
score = np.array([98,90,96,54,
                43,87,88,90,
                94,92,81,79,85,
                91,79,88,89,83])
              
# plt.hist(score) #넘파이 배열 score 넣어줌
# plt.title("Histogram of score") # 제목 지정
# plt.xlabel('Score')  # x축 제목 지정
# plt.ylabel("Frequency") # y축 제목 지정
# plt.show() # 그래프 보이게 하기

# 한 화면에 두 개의 히스토그램 그리기
# plt.subplot(1,2,1) # 1행 2열의 1번쨰  
# plt.hist(score, color="Green")

# plt.title("histogram")
# plt.xlabel('score')
# plt.ylabel('Frequency')

# plt.subplot(1,2,2) #  1행 2열의 2번쨰 
# plt.hist(score, color="Blue")

# plt.title("histogram")
# plt.xlabel('score')
# plt.ylabel('Frequency')

# plt.show()


# 줄기-잎 그림
# stem_graphic(score)

# 질적 자료 요약(표 and 그래프)
# 1차원 빈도표(frequency table)

# gender_sr = pd.Series(gender)
# print("--value_counts() 함수 gender 시리즈 자료에 적용--")
# y = gender_sr.value_counts()
# print(len(y)) # 2 나옴..

# 높이 값을 직접 지정
heights = [170, 165, 180, 172, 168]

# x축 값 지정 (0부터 4까지 인덱스)  
x = range(len(heights))

# 바 차트 출력
plt.bar(x, heights)
plt.xticks(x, ['ps1', 'ps2', 'ps3', 'ps4', 'ps5'])
plt.xlabel('ps')
plt.ylabel('height(cm)') 
plt.title('people\'s height')
plt.show()
