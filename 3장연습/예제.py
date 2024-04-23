#예제1
import numpy as np

nums = np.random.randint(1,101,40)

re_nums = nums.reshape(5,8)

print(re_nums)
#1-2, 2행 3행 출력
print( re_nums[1:3] )


#1-3, (1,4,7,8)열을 출력
print( re_nums[:, [0,3,6,7] ] )
print()

#1-4, 7번째 열의 평균(mean)과 분산(variance) 
_7th_column = re_nums[:, 6] # 6이지만 7번쨰열임!!

# 평균구하기 (numpy 함수 사용)
print("7번째 열 평균: ", np.mean(_7th_column) )

# 분산구하기
print("7번째 열 분산: ", np.var(_7th_column) )


# #예제2
# import numpy as np

# # 1 ~ 20 사이 1개의 숫자 임의로 선택하고 저장
# num = np.random.randint(1, 21, 1)

# # num이 10 이상이면 P 출력 아니면 NP 출력
# if (num >= 10):
# 	print("P")
# else:
# 	print("NP")

# #예제3
# import numpy as np

# # 1 ~ 20 사이에 8개의 숫자 임의로 선택하고 저장
# nums = np.random.randint(1,21,8)
# for num in nums:
# 	if(num >= 10):
# 		print("P")
# 	else:
# 		print("NP")
























# import seaborn as sns

# iris = sns.load_dataset('iris')

# print(iris)
# print('------------------------------------')

# print("iris.loc[3:5,:] 출력결과:")
# print(iris.loc[3:5,:])   # 끝값 포함 O

# print("iris.iloc[3:5,:] 출력결과:")
# print(iris.iloc[3:5,:])  # 끝값 포함 X
