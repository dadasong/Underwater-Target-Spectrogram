#-*- coding:utf-8 -*-
from PIL import Image
import os
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
import numpy as np
from convert import cov
def predict(path):
#----------定义需要的变量——————-------------------------
	train_array=[]
	test_array=[]
	train_label_array=[]
	test_label_array=[]
	k=0
	Psum1=0
	Psum2=0
	Psum3=0
	Psum4=0
	# Psum5=0
	PDiver = 0
	PNoTarget = 0
	POxygen = 0

	Nsum1=0
	Nsum2=0
	Nsum3=0
	Nsum4=0
	# Nsum5=0
	RDiver = 0
	RNoTarget = 0
	ROxygen = 0

	dict_list=[]
	file=open(path+'/'+"train.txt","r")
	for line in file:
		#print(line.split()[0])
		im=Image.open(line.split()[0])
		im_array = np.array(im)
		im_array_2=im_array.flatten()
		train_array.append(im_array_2)
	#print(train_array)
  #读训练样本

	file2=open(path+'/'+"test.txt","r")
	for line in file2:

		dict_list.append(line[:len(line)-1])
		im=Image.open(line[:len(line)-1])
		im_array = np.array(im)
		im_array_2=im_array.flatten()
		test_array.append(im_array_2)
 #读测试样本

	#print(test_array)
	file3=open(path+'/'+"train_label.txt","r")
	for line in file3:
		train_label_array.append(int(line[:len(line)-1]))
 #读训练标签
		file4=open(path+'/'+"test_label.txt","r")
	for line in file4:
		test_label_array.append(int(line[:len(line)-1]))
	n=10
	for k in range(0,n):
		
		num1=0
		num2=0
		num3=0
		num4=0
		# num5=0
	 
		clf = RandomForestClassifier(n_estimators =100 )   #预测
		#clf=svm.SVC()
		s = clf.fit(train_array , train_label_array)
		g = clf.score(test_array , test_label_array)
		
		result = clf.predict(test_array)
		result=result.tolist()
		#print(result)
		lenth=len(result)
		lenth1=len(test_label_array)
		# for o in range(0,lenth):
		# 	if result[o]==1: 
		# 		print(dict_list[o],"")
		# 	elif result[o]==2:
		# 		print(dict_list[o],"")
		# #print(lenth)
		#print(lenth1)
		#print(result)
		#print(test_label_array)
		num1=test_label_array.count(1)
		num2=test_label_array.count(2)
		#print(num1,num2)
		num3=test_label_array.count(3)
		# num4=test_label_array.count(4)
		# num5=test_label_array.count(5)

		i=0
		list1=[0]*25
		

		while i<len(result):
			if i<num1:
				if result[i]==1:
					list1[0]+=1  #1-1
				if result[i]==2:
					list1[1]+=1  #1-2
				if result[i]==3:
					list1[2]+=1	 #1-3
				# if result[i]==4:
				# 	list1[3]+=1	 #1-4
				# if result[i]==5:
				# 	list1[4]+=1	 #1-5
			elif i<(num2+num1):
				if result[i]==1:
					list1[5]+=1  #2-1
				if result[i]==2:
					list1[6]+=1  #2-2
				if result[i]==3:
					list1[7]+=1	 #2-3
				# if result[i]==4:
				# 	list1[8]+=1	 #2-4
			# 	if result[i]==5:
			# 		list1[9]+=1	 #2-5
			elif i<(num2+num1+num3):
				if result[i]==1:
					list1[10]+=1 #3-1
				if result[i]==2:
					list1[11]+=1 #3-2
				if result[i]==3:
					list1[12]+=1 #3-3	
			# 	if result[i]==4:
			# 		list1[13]+=1 #3-4	
			# # 	if result[i]==5:
			# # 		list1[14]+=1 #3-5
			# elif i<(num2+num1+num3+num4):
			# 	if result[i]==1:
			# 		list1[15]+=1 #4-1
			# 	if result[i]==2:
			# 		list1[16]+=1 #4-2
			# 	if result[i]==3:
			# 		list1[17]+=1 #4-3 
			# 	if result[i]==4:
			# 		list1[18]+=1 #4-4
			# 	if result[i]==5:
			# 		list1[19]+=1 #4-5
			# elif i>=(num2+num1+num3+num4):
			# 	if result[i]==1:
			# 		list1[20]+=1 #5-1
			# 	if result[i]==2:
			# 		list1[21]+=1 #5-2
			# 	if result[i]==3:
			# 		list1[22]+=1 #5-3
			# 	if result[i]==4:
			# 		list1[23]+=1 #5-4
			# 	if result[i]==5:
			# 		list1[24]+=1 #5-5
			i+=1
		#print(list1)
		#Nsum1+=list1[5]/(lenth-num1)
		#Nsum2+=list1[1]/(lenth-num2)
		# Nsum3+=(list1[2]+list1[7]+list1[17]+list1[22])/(lenth-num3)
		# Nsum4+=(list1[3]+list1[8]+list1[13]+list1[23])/(lenth-num4)

		
		#Nsum5+=(list1[4]+list1[9]+list1[14]+list1[19])/(lenth-num5)
		Nsum1+=(list1[5]+list1[10])/(lenth-num1)
		Nsum2+=(list1[1]+list1[11])/(lenth-num2)
		Nsum3+=(list1[2]+list1[7])/(lenth-num3)
		Psum1+=list1[0]/num1
		Psum2+=list1[6]/num2
		Psum3+=list1[12]/num3
		# Psum3+=list1[12]/num3
		# Psum4+=list1[18]/num4
		# Psum5+=list1[24]/num5
		#k+=1
		#if(k%10==0):
			#print("进行第%d次预测"%k)
	# print("预测评分")
	# print("样本噪声方差为%s" %path)	

	PDiver = list1[0]/(list1[0]+list1[5]+list1[10])
	PNoTarget = list1[6]/(list1[1]+list1[6]+list1[11])
	POxygen = list1[12]/(list1[2]+list1[7]+list1[12])

	RDiver = list1[0]/(list1[0]+list1[1]+list1[2])
	RNoTarget = list1[6]/(list1[5]+list1[6]+list1[7])
	ROxygen = list1[12]/(list1[10]+list1[11]+list1[12])

	FDiver = 2*list1[0]/(list1[0]+list1[5]+list1[10]+list1[0]+list1[1]+list1[2])
	FNoTarget = 2*list1[6]/(list1[1]+list1[6]+list1[11]+list1[5]+list1[6]+list1[7])
	FOxygen = 2*list1[12]/(list1[2]+list1[7]+list1[12]+list1[10]+list1[11]+list1[12])
	# print("蛙人平均识别率:",Psum1/n)
	# print("无目标平均识别率:",Psum2/n)
	# print("氧气瓶平均识别率:",Psum3/n)


	# print("蛙人平均虚警率:",Nsum1/n)
	# print("无目标平均虚警率:",Nsum2/n)
	# print("氧气瓶平均虚警率:",Nsum3/n)

	print("蛙人识别精确率：",PDiver)
	print("无目标识别精确率：",PNoTarget)
	print("氧气瓶识别精确率：",POxygen)

	print("蛙人识别召回率：",RDiver)
	print("无目标识别召回率：",RNoTarget)
	print("氧气瓶识别召回率：",ROxygen)

	print("蛙人识别调和均值：",FDiver)
	print("无目标识别调和均值：",FNoTarget)
	print("氧气瓶识别调和均值：",FOxygen)

	print("score:",g)
	print("--------------------------数据分割线-----------------------")

if __name__ == "__main__":
	path="C:/Users/Administrator/Desktop/UnderwaterSepctrogram"
	# ALL_Path=os.listdir(path) #读文件目录
	# for i in ALL_Path:
	# 	if os.path.isdir(path+"/"+i)==1: #是文件夹 再搞
	# 		predict(path+"/"+i)
	predict(path)
	






















 










