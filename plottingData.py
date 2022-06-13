import numpy as np
import arff
import matplotlib.pyplot as plt

dataset = list(arff.load('EEG_Eyes.arff'))
data = np.zeros((len(dataset),len(dataset[0])))
min = np.array([[1030,3924,4197,2453,2089,2768,3581,4567,4152,4152,4100,4201,86,1366],[4198,3905,4212,4058,4309,4574,4026,4567,4147,4174,4130,4225,4510,4246]])
mean = np.array([[4297,4013,4263,4123,4341,4620,4071,4615,4200,4229,4200,4277,4601,4356],[4305,4005,4265,4121,4341,4618,4073,4616,4202,4233,4204,4281,4610,4367]])
max = np.array([[4504,7804,5762,4250,4463,4756,4178,7264,4586,6674,5170,7002,4833,4573],[4445,4138,4367,4214,4435,4708,4167,4695,4287,4323,4319,4368,4811,4552]])
outlier = []

for i in xrange(len(dataset)):
	for j in xrange(len(dataset[0])):
		data[i][j] = dataset[i][j]

for i in xrange(len(data)):
	breaker = 0
	for j in xrange(len(data.T)-1):
		if data[i][len(data.T)-1] == 0:
			if max[0][j] < data[i][j] or data[i][j] < min[0][j]:
				if breaker == 0:
					outlier.append(i)
					breaker += 1
				else:
					break
		if data[i][len(data.T)-1] == 1:
			if max[1][j] < data[i][j] or data[i][j] < min[1][j]:
				if breaker == 0:
					outlier.append(i)
					breaker += 1
				else:
					break

for i in sorted(outlier,reverse=True):
	data = np.delete(data,i,0)

np.savetxt('EEG_Eyes.csv', data, delimiter=',')
# for idx, x in enumerate(data.T[:len(data.T)-1]):
# 	plt.figure(idx)
# 	plt.plot(x)
# 	plt.show()

# Eye closed open
# State min mean max min mean max
# AF3 4198 4305 4445 1030 4297 4504
# F7 3905 4005 4138 3924 4013 7804
# F3 4212 4265 4367 4197 4263 5762
# FC5 4058 4121 4214 2453 4123 4250
# T7 4309 4341 4435 2089 4341 4463
# P7 4574 4618 4708 2768 4620 4756
# O1 4026 4073 4167 3581 4071 4178
# O2 4567 4616 4695 4567 4615 7264
# P8 4147 4202 4287 4152 4200 4586
# T8 4174 4233 4323 4152 4229 6674
# FC6 4130 4204 4319 4100 4200 5170
# F4 4225 4281 4368 4201 4277 7002
# F8 4510 4610 4811 86 4601 4833
# AF4 4246 4367 4552 1366 4356 4573