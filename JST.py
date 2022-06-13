import numpy as np
import random
from random import sample
import math
import sys
import time
import Loader as load

def decodeWeight(weights,num_input_decode,num_hidden_decode,num_output_decode):

	weight1 = np.array([weights[i*num_hidden_decode:(i+1)*num_hidden_decode] for i in xrange(num_input_decode)])

	weight2 = np.array([weights[(num_input_decode*num_hidden_decode)+(i*num_output_decode):(num_input_decode*num_hidden_decode)+((i+1)*num_output_decode)] for i in xrange(num_hidden_decode)])

	return weight1, weight2

def sumFunction(inp, weight):
	return np.dot(inp, weight)

def actFunction(x):
	return 1/(1 + np.exp(-x))
	# return np.exp(-0.001*x*x)

def neuron(inp, weight):
	return actFunction(sumFunction(inp, weight))

def correct(inp,w):
	output = neuron(neuron(inp[0:-1], w[0]), w[1])
	print ((np.argmax(output)),int(inp[-1]))
	#print (output,int(inp[-1]))
	if (np.argmax(output) == int(inp[-1])):
	# if output == int(inp[-1]):
	#np.savetxt('data.csv', np.array(, newline=',')
		return True
	else:
		return False

def encodeTargetClass(inp):
	ret = np.zeros((len(inp),num_output))
	for i in xrange(len(inp)):
		ret[i][inp[i][-1]] = 1
	return ret

def mse(inp, weight, num_inputx, num_hiddenx, num_outputx):
	global num_hidden
	global num_input
	global num_output
	num_hidden = num_hiddenx
	num_input = num_inputx
	num_output = num_outputx
	mse = np.zeros((len(weight),1))
	# split = np.array_split(inp, 5)
	x = inp[0:,0:-1]
	# target = inp[0:,-1:]
	target = encodeTargetClass(inp)
	for i in xrange(len(weight)):
		w = decodeWeight(weight[i], num_inputx, num_hiddenx, num_outputx)
		output = neuron(neuron(x,w[0]),w[1])
		err = target - output
		# print np.sum(np.power(err,2))/(len(inp)*num_output)
		mse[i] = np.mean(np.power(err,2))
	return mse

def vmse(inp, weight, num_inputx, num_hiddenx, num_outputx):
	global num_hidden
	global num_input
	global num_output
	num_hidden = num_hiddenx
	num_input = num_inputx
	num_output = num_outputx
	w = decodeWeight(weight, num_inputx, num_hiddenx, num_outputx)
	mse = 0
	x = inp[0:,0:-1]
	# target = inp[0:,-1:]
	target = encodeTargetClass(inp)
	output = neuron(neuron(x,w[0]),w[1])
	err = target - output
	mse = np.sum(np.power(err,2))/(len(inp)*num_output)
	return mse	

def measure(inp,w,tp,fp,fn):
	output = neuron(neuron(inp[0:-1], w[0]), w[1])
	recall = [0 for i in xrange(len(output))]
	presisi = [0 for i in xrange(len(output))]
	measure = [0 for i in xrange(len(output))]
	for i in xrange(len(output)):
		if ((np.argmax(output) == i == int(inp[-1]))):
			tp[i] += 1
		if ((np.argmax(output) != i) and (int(inp[-1]) == i)):
			fn[i] += 1
		if ((np.argmax(output) == i) and (int(inp[-1]) != i)):
			fp[i] += 1
		presisi[i] = (tp[i]*1.0)/(tp[i]+fp[i]+0.0000001)
		recall[i] = (tp[i]*1.0)/(tp[i]+fn[i]+0.0000001)
		measure[i] = 2*(presisi[i]*recall[i])/((presisi[i]+recall[i])+0.0000001)
	return measure, presisi, recall

# def nonlin(x, deriv = False):
# 	if (deriv == True):
# 		return x*(1-x)
# 	return 1/(1+np.exp(-x))


# train = load.trainData("EEG_Eyes.csv")
# test = load.testData("EEG_Eyes.csv")
# data = load.loadNormalizedCsv("EEG_Eyes.csv")


# global num_hidden
# global num_input
# global num_output
# # num_hidden = 4
# # num_input = 3
# # num_output = 1

# num_hidden = 6
# num_input = 14
# num_output = 2

# # x = np.array([[0,0,1],
# #             [0,1,1],
# #             [1,0,1],
# #             [1,1,1]])
                
# # y = np.array([[0],
# # 			[1],
# # 			[1],
# # 			[0]])

# x = train[0:,0:-1]
# y = encodeTargetClass(train)
# #y = inp[0:,-1:]
# # np.random.seed(2)
# random.seed(1)
# syn0 = 2*np.random.random((num_input,num_hidden))
# syn1 = 2*np.random.random((num_hidden,num_output))
# l0 = x

# for i in xrange(500):
	
# 	l1 = nonlin(np.dot(l0,syn0))
# 	l2 = nonlin(np.dot(l1,syn1))

# 	l2_error = y - l2

# 	if (i% 100) == 0:
# 		print "Error:" + str(np.mean(np.power(l2_error,2)))
	        
# 	l2_delta = l2_error*nonlin(l2, deriv=True)

# 	l1_error = l2_delta.dot(syn1.T)

# 	l1_delta = l1_error * nonlin(l1, deriv=True)

# 	syn1 += l1.T.dot(l2_delta)
# 	syn0 += l0.T.dot(l1_delta)

