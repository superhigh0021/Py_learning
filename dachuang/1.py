#定义房间
###########################
import numpy
wall=numpy.zeros((6,20))
#四周墙壁
for i in range(20):
	wall[0][i]=9
	# wall[i][0]=9
	wall[5][i]=9
	# wall[i][5]=9
#出口
# wall[2][5]=0
# wall[3][5]=0
# print(wall)

############################


# 人为 定义行人
############################
wall[1][3]=1
wall[2][2]=1     #先选取这一个当做行人，现在房间是空的，初步预测
wall[3][2]=1
wall[3][3]=1
wall[4][1]=1
wall[4][2]=1
wall[4][4]=1
# p=[wall[1][3],wall[2][2],wall[3][2],wall[3][3],wall[4][1],wall[4][2],wall[4][4]]
# print(p)
# print(wall)
# print(wall[2][2])

##############################
#
#
# # 储存行人的列表
#

#
#
#
# 定义运动倾向D
# D=0
#
# px=D+(1-D)/3
# p_y=(1-D)/3
# py=(1-D)/3
#
#

# x=20
# # while(x>0):
# 	i=2
# 	j=2
# # 对于往右边行走的行人：（8种情况）
# 	if wall[i-1][j]=0 and wall[i+1][j]=0 and wall[i][j+1]=0:     # 上下右
# 		wall[i][j + 1] = wall[i][j]
#
# 	if wall[i - 1][j]=1 and wall[i+1][j]=0 and wall[i][j+1]=0:
# 		wall[i][j + 1] = wall[i][j]
#
# 	if wall[i - 1][j]=0 and wall[i+1][j]=1 and wall[i][j+1]=0:
# 		wall[i][j + 1] = wall[i][j]
#
# 	if wall[i - 1][j]=0 and wall[i+1][j]=0 and wall[i][j+1]=1:
# 		两个或者关系
# 	if wall[i - 1][j]=1 and wall[i+1][j]=1 and wall[i][j+1]=0:
# 		wall[i][j + 1] = wall[i][j]
#
# 	if wall[i - 1][j]=0 and wall[i+1][j]=1 and wall[i][j+1]=1:
# 		wall[i - 1][j] = wall[i][j]
#
# 	if wall[i - 1][j]=1 and wall[i+1][j]=0 and wall[i][j+1]=1:
# 		wall[i + 1][j] = wall[i][j]
#
# 	if wall[i - 1][j]=1 and wall[i+1][j]=1 and wall[i][j+1]=1:
# 		wall[i][j] = wall[i][j]


	# # 对于往右边行走的行人：（8种情况）
	# if wall[i-1][j]=0 and people[i+1][j]=0 and people[i][j+1]=0:      #上下右
	# 	pepole[i][j+1]=pepole[i][j]
	#
	# if people[i - 1][j]=1 and people[i+1][j]=0 and people[i][j+1]=0:
	# 	pepole[i][j + 1] = pepole[i][j]
	#
	# if people[i - 1][j]=0 and people[i+1][j]=1 and people[i][j+1]=0:
	# 	pepole[i][j + 1] = pepole[i][j]
	#
	# if people[i - 1][j]=0 and people[i+1][j]=0 and people[i][j+1]=1:
	# 	两个或者关系
	# if people[i - 1][j]=1 and people[i+1][j]=1 and people[i][j+1]=0:
	# 	pepole[i][j + 1] = pepole[i][j]
	#
	# if people[i - 1][j]=0 and people[i+1][j]=1 and people[i][j+1]=1:
	# 	pepole[i-1][j] = pepole[i][j]
	#
	# if people[i - 1][j]=1 and people[i+1][j]=0 and people[i][j+1]=1:
	# 	pepole[i+1][j] = pepole[i][j]
	#
	# if people[i - 1][j]=1 and people[i+1][j]=1 and people[i][j+1]=1:
	# 	pepole[i][j] = pepole[i][j]
	# x-=1

# print(wall.shape)    #输出矩阵行，列
# print(wall.shape[0])   #输出矩阵的行
# print(wall.shape[1])    #输出矩阵的列


for i in range(wall.shape[0]):
	for j in range(wall.shape[1]-1):
		if wall[i][j]==1:
			if wall[i - 1][j] == 0 and wall[i + 1][j] == 0 and wall[i][j + 1] == 0:  # 上下右
				wall[i][j], wall[i][j + 1] = wall[i][j + 1], wall[i][j]
				if wall[i][wall.shape[1]==1]:
					break
				# print('第{}次'.format(j - 2))
				# print(wall)
			if wall[i - 1][j] !=0 and wall[i + 1][j] == 0 and wall[i][j + 1] == 0:  # 下右
				wall[i][j], wall[i][j + 1] = wall[i][j + 1], wall[i][j]
				if wall[i][wall.shape[1]==1]:
					break

			if wall[i - 1][j] == 0 and wall[i + 1][j] !=0 and wall[i][j + 1] == 0:  # 上右
				wall[i][j], wall[i][j + 1] = wall[i][j + 1], wall[i][j]
				if wall[i][wall.shape[1]==1]:
					break

			if wall[i - 1][j]==0 and wall[i+1][j]==0 and wall[i][j+1]!=0:      #上下
				wall[i - 1][j], wall[i - 1][j] = wall[i - 1][j], wall[i - 1][j]   #这里先规定默认是向上
				if wall[i][wall.shape[1]==1]:
					break

			if wall[i - 1][j] !=0 and wall[i + 1][j] !=0 and wall[i][j + 1] == 0:  # 右空
				wall[i][j], wall[i][j + 1] = wall[i][j + 1], wall[i][j]
				if wall[i][wall.shape[1]==1]:
					break

			if wall[i - 1][j] == 0 and wall[i + 1][j] !=0 and wall[i][j + 1] !=0:  # 上空
				wall[i][j],wall[i - 1][j] =wall[i - 1][j],wall[i][j]
				if wall[i][wall.shape[1]==1]:
					break

			if wall[i - 1][j] !=0 and wall[i + 1][j] == 0 and wall[i][j + 1] !=0:  # 下空
				wall[i][j],wall[i + 1][j] = wall[i + 1][j],wall[i][j]
				if wall[i][wall.shape[1]]==1:
					break

			if wall[i - 1][j] !=0 and wall[i + 1][j] !=0 and wall[i][j + 1] !=0:  # 无空
				wall[i][j]=wall[i][j]
			print()
			print(wall)


#
# for j in range(2,19):
#
# 	i = 2

	# if wall[i - 1][j] == 0 and wall[i + 1][j] == 0 and wall[i][j + 1] == 0:  # 上下右
	# 	wall[i][j],wall[i][j + 1] = wall[i][j + 1],wall[i][j]
	# 	print('第{}次'.format(j-2))
	# 	print(wall)
	# if wall[i - 1][j] == 1 and wall[i + 1][j] == 0 and wall[i][j + 1] == 0:   #下右
	# 	wall[i][j],wall[i][j + 1] = wall[i][j + 1],wall[i][j]
	#
	# if wall[i - 1][j] == 0 and wall[i + 1][j] == 1 and wall[i][j + 1] == 0:   #上右
	# 	wall[i][j],wall[i][j + 1] = wall[i][j + 1],wall[i][j]
	#
	# # if wall[i - 1][j]==0 and wall[i+1][j]==0 and wall[i][j+1]==1:      #上下
	# # 两个或者关系
	# if wall[i - 1][j] == 1 and wall[i + 1][j] == 1 and wall[i][j + 1] == 0:       #右空
	# 	wall[i][j + 1] == wall[i][j]
	#
	# if wall[i - 1][j] == 0 and wall[i + 1][j] == 1 and wall[i][j + 1] == 1:      #上空
	# 	wall[i - 1][j] == wall[i][j]
	#
	# if wall[i - 1][j] == 1 and wall[i + 1][j] == 0 and wall[i][j + 1] == 1:    #下空
	# 	wall[i + 1][j] == wall[i][j]
	#
	# if wall[i - 1][j] == 1 and wall[i + 1][j] == 1 and wall[i][j + 1] == 1:     #无空
	# 	wall[i][j] == wall[i][j]
	# print('第{}次'.format(x))
	# print(wall)
