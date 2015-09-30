import numpy
import random
import math



#global parameters
vector_input_1=[]   #4*5
vector_1_2=[]     #5
input_data=[]   #16*4
firstlayer_data=[]
secondlayer_data=[]
delta_1_2=[]

num_choose=10
numofsecondlayer=1
numoffirstlayer=4
numberofinputlayer=4
bias1=random.uniform(-1,1)
bias2=random.uniform(-1,1)
desire=[0,1,1,0,1,0,0,1,1,0,0,1,0,1,1,0]
a=1 # for sigmoid function derivative
ita=0.05  #0.05--0.5
iteration_times=1    # because of the logic of NN_propagation()
#init input_data
for i in range(0,2):
	for j in range(0,2):
		for m in range(0,2):
			for n in range(0,2):
				input_data.append((i,j,m,n,bias1))

#init weight vector
for i in range(numoffirstlayer):
	temp_vector=[]
	for j in range(numberofinputlayer+1):   # 1 for the bias
		temp_vector.append(random.uniform(-1,1))
	vector_input_1.append(temp_vector)

for i in range(numofsecondlayer):
	for j in range(numoffirstlayer+1):
		vector_1_2.append(random.uniform(-1,1))  #############change logic when second layer not 1

#absolute error
def error_function():
	sum=pow(desire[num_choose]-secondlayer_data[0],2)
	#for i in range(k):
	#	sum=sum+pow(d[i]-y[i],2)
	#result=desire[num_choose]-secondlayer_data[0]
	return math.sqrt(sum/2)



#utility func
#sigmoid
def sigmoid(x):
	return 1/(1+math.exp(-x))

def sigmoid_derivative(x):
	global a
	sigmoid_=sigmoid(x)
	return a*sigmoid_*(1-sigmoid_)


#training
def go_forward():
	#print vector_input_1
	for j in range(numoffirstlayer):
		sum=0

		for i in range(numberofinputlayer+1):
			sum=sum+input_data[num_choose][i]*vector_input_1[j][i]     # sum of 5 input multi weight
			#print sum
		firstlayer_data.append(sigmoid(sum))
	#print("fisrtlayer:")
	#print firstlayer_data

	firstlayer_data.append(bias2)
	#print len(firstlayer_data)
	sum=0
	for i in range(numoffirstlayer+1):
		sum=sum+firstlayer_data[i]*vector_1_2[i]
	secondlayer_data.append(sigmoid(sum))
	#print("secondlayer_data")
	#print secondlayer_data


def go_back():
	#updata 1_2
	for i in range(len(vector_1_2)):
		delta_=a*secondlayer_data[0]*(1-secondlayer_data[0])*(desire[num_choose]-secondlayer_data[0])
		vector_1_2[i]=vector_1_2[i]+ita*firstlayer_data[i]*delta_
		delta_1_2.append(delta_)

	for j in range(5):
		for i in range(4):
			vector_input_1[i][j]=vector_input_1[i][j]+a*firstlayer_data[i]*(1- firstlayer_data[i])*vector_1_2[i]*delta_1_2[0]
	#updata inpit_1    ##################
###

#for i in range(1000):
#	secondlayer_data=[]
#	firstlayer_data=[]
#	delta_=[]
#	go_forward()
#	#print vector_1_2
#	go_back()
#	print vector_1_2
#	#print secondlayer_data
#	print error_function()
#	#if (error_function<0.05):
#	#	break
def NN_propagation():
	global iteration_times
	#error_=999999.0
	go_forward()
	go_back()
	while(error_function()>0.05):
		secondlayer_data=[]
		firstlayer_data=[]
		delta_=[]
		go_forward()
		go_back()
		#error_=error_function()
		iteration_times=iteration_times+1
		print error_function()
	print iteration_times
#NN_propagation()

#go_forward()
#go_back()
#while(error_function()>0.05):
#	secondlayer_data=[]
#	firstlayer_data=[]
#	delta_=[]
#	go_forward()
#	go_back()
#	#error_=error_function()
#	iteration_times=iteration_times+1
#print error_function()
#print iteration_times

check_array=[]
for i in range(16):
	check_array.append(0)
def check_complete(a):
	num_=0
	for i in range(len(a)):
		if a[i]==1:
			num_=num_+1
	return num_!=16

num_choose=0
test_n=0
go_forward()
go_back()
#while(check_complete(check_array)):
while(test_n<20):
	#check_num=0
	#num_choose=0
	test_n=test_n+1
	if error_function()<0.05:
		check_array[num_choose]=1
		print num_choose
		num_choose=num_choose+1
		if num_choose==16:
			num_choose=0
		#check_num=check_num+1
	else:
		#check_array[num_choose]=0
		check_array=[]
		for i in range(16):
			check_array.append(0)
		while(error_function()>0.05):
			secondlayer_data=[]
			firstlayer_data=[]
			delta_=[]
			go_forward()
			go_back()
			#error_=error_function()
			iteration_times=iteration_times+1
	print error_function()
print iteration_times







       # 1 for the bias