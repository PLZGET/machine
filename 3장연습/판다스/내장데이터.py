import seaborn as sns

iris = sns.load_dataset('iris') # iris 데이터프레임(데이터셋) 로드해서 iris 변수에 저장
print(iris)

table = iris.groupby("species").size()
print(table)