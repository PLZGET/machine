import pandas as pd

test = pd.read_excel("C:/Users/niko3/OneDrive/바탕 화면/삼육/2024_1학기/기계학습/test.xlsx")
print(test)
print()
print("----------test['class']----------")
print(test['class'])
class_label = {'1':'1반','2':'2반','3':'3반','4':'4반','5':"5반"}
test['class'] = test['class'].astype("str")
test['class'] = test['class'].map(class_label)
print(test)
print('===============================================')

test.loc[test["class"]<='2반', 'group'] = 'A'
# test.loc[test["class"]>='3반', 'group'] = 'B'

print(test)
