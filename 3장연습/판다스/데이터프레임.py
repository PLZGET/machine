from pandas import DataFrame
import pandas as pd
import seaborn as sns
# rawData = {
#     'ID' : [1,2,3,4,5],
#     'Gender' : ['M','M','F','F','F'],
#     'Math' : [66,64,68,46,24],
#     'English' : [70,68,46,90,100]
# }

# score = DataFrame(rawData)
# print(score)
# print()

# # 변수 불러오기 
# print(score.Gender) # socre의 Gender 변수 불러옴
# print()
# print(score['Math']) # socre의 Math 변수 불러옴

iris = sns.load_dataset('iris')
print(iris)

print(iris.value_counts('species')) # 종별 빈도수
print()
print("위 아래 같은 결과")
print()
print(iris.groupby('species').size()) # 종별 빈도수


