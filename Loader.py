import numpy as np
import random
from random import sample
import csv

def loadCsv(file):
	return np.loadtxt(file, delimiter=',',dtype=float)

def loadNormalizedCsv(file):
	dataset = np.loadtxt(file, delimiter=',',dtype=float)
	normalized = np.zeros((dataset.shape))
	maxVar = np.amax(dataset, 0)
	minVar = np.amin(dataset, 0)

	for i in xrange(len(dataset)):
		for j in xrange(len(dataset[0])):
			normalized[i][j] = (dataset[i][j] - minVar[j])/(maxVar[j]-minVar[j])
	return normalized

def loadArff(file):
	return list(arff.load(file))

def trainData(file):
	dataset = loadNormalizedCsv(file)
	random.seed(1)
	indices = sample(range(len(dataset)), int(round(len(dataset)*0.2)))
	# data = dataset[indices]
	# indices2 = sample(range(len(data)), int(round(len(data)*(5.0/7.0),2)))
	return dataset[indices]
	# data1 = sorted(dataset, key = lambda x:x[-1], reverse=True)[:len(dataset)/80]
	# data2 = sorted(dataset, key = lambda x:x[-1])[:len(dataset)/80]
	# return np.concatenate((data1,data2),axis=0)

def testData():
	# dataset = loadNormalizedCsv(file1)
	train0 = loadCsv('train0.csv')
	train1 = loadCsv('train1.csv')
	train2 = loadCsv('train2.csv')
	train3 = loadCsv('train3.csv')
	train4 = loadCsv('train4.csv')
	# random.seed(1)
	# indices = sample(range(len(dataset)),int(round(len(dataset)*0.7)))
	# return np.delete(dataset,indices,0)

	data_test = np.concatenate((train1,train2,train3,train4),axis=0)
	np.savetxt('test0.csv', np.array(data_test), delimiter=',')

	# dataset = np.delete(sorted(dataset, key = lambda x:x[-1], reverse=True),np.s_[:len(dataset)/8],0)
	# dataset = np.delete(sorted(dataset, key = lambda x:x[-1]),np.s_[:len(dataset)/8],0)
	return data_test

def divideData(file):
	dataset = loadCsv(file)
	random.seed(1)
	for i in xrange(5):
		nama = "data"+str(i)+".csv"
		indices = sample(range(len(dataset)), int(round(len(dataset)*(2.0/(10.0-(2.0*i))))))
		data = dataset[indices]
		dataset = np.delete(dataset,indices,0)
		np.savetxt(nama, np.array(data), delimiter=',')