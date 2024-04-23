import pandas as pd
import matplotlib.pyplot as plt
from stemgraphic import stem_graphic
# 텍스트파일 -> 데이터프레임으로 변환
# cdc = pd.read_csv("C:\data2\cdc.txt", sep=" ")
# print(cdc)

# CSV 파일 -> 데이터프레임으로 변환
# cars93 = pd.read_csv("C:\data2\cars93.csv")
# print(cars93)

# Excel 파일 -> 데이터프레임으로 변환
# major = pd.read_excel("C:\data2\major.xlsx")
# print(major)

test = pd.read_excel("C:/data2/test.xlsx")
print(test)

# class_label = {1:'1반', 2:'2반', 3:'3반', 4:'4반', 5:'5반'}
# print(test['class'].map(class_label))

# print(test.value_counts('gender')) 
# print()
# print(test.groupby('gender').size())

# test 데이터셋의 변수 math 출력
print("test.math: \n", test.math)