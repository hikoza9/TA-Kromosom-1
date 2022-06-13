import Loader
import JST
import ES
import os
import time
import sys
import numpy as np

num_input = int(sys.argv[1])
num_hidden = int(sys.argv[2])
num_output = int(sys.argv[3])

pop_size = int(sys.argv[4])
gen_limit = int(sys.argv[5])
pC = float(sys.argv[6])
pM = float(sys.argv[7])
# file_data_testing = (sys.argv[8])
test_ke = int(sys.argv[8])


# inps = Loader.testData(file_data_testing)
# inps = Loader.trainData(file_data_testing)
# inps = Loader.loadNormalizedCsv(file_data_testing)
f1measure = np.zeros(5)
akurasi = np.zeros(5)
msex = np.zeros(5)
path_weight = '.\\Kr 1\\weight\\'

new_folder = str(num_input)+"_"+str(num_hidden)+"_"+str(num_output)+"_"+str(pop_size)+"_"+str(gen_limit)+"_"+str(pC)+"_"+str(pM)
path_weight1 = path_weight+new_folder

for j in xrange(5):
	data_name = "Test"+str(j)+".csv"
	data_path = 'D:\\Running\\NEW!!\\Kr 1\\data testing\\'
	# data_name = "train"+str(j)+".csv"
	# data_path = '.\\Kr 1\\data training\\'
	file_data_testing = data_path+data_name
	inps = Loader.loadCsv(file_data_testing)

	file_weights = path_weight1+"\\"+"train"+str(j)+".csv_"+str(num_input)+"_"+str(num_hidden)+"_"+str(num_output)+"_"+str(pop_size)+"_"+str(gen_limit)+"_"+str(pC)+"_"+str(pM)+"_"+str(test_ke)+".csv"




	weights = JST.decodeWeight(Loader.loadCsv(file_weights),num_input,num_hidden,num_output)

	match = 0
	tp1 = 0
	pp1 = 0
	tn1 = 0
	pn1 = 0
	fn1 = 0
	m = [0 for i in xrange(num_output)]
	tp = [0 for i in xrange(num_output)]
	fp = [0 for i in xrange(num_output)]
	fn = [0 for i in xrange(num_output)]

	for i in range(len(inps)):
 		if(JST.correct(inps[i],weights)):
 			match += 1
 		m = JST.measure(inps[i], weights, tp, fp, fn)

# print m
	f1measure[j] = m[0][0]
	akurasi[j] = (match*100)/len(inps)
	msex[j] = JST.vmse(inps,Loader.loadCsv(file_weights),num_input,num_hidden,num_output)
	a=np.random.random((3,4))
	result = int(num_hidden),int(pop_size),int(gen_limit),pC,pM,m[0][0], m[1][0], m[2][0], JST.vmse(inps,Loader.loadCsv(file_weights),num_input,num_hidden,num_output), (match*100)/len(inps)
	#print np.array(result)
	#np.savetxt(save, np.array(result), newline=',')

# save_path = './Kr 1/result/test thd train/'
save_path = './Kr 1/result/test thd test/'
directory = save_path
if not os.path.exists(directory):
	os.makedirs(directory)
weight_name = str(num_input)+"_"+str(num_hidden)+"_"+str(num_output)+"_"+str(pop_size)+"_"+str(gen_limit)+"_"+str(pC)+"_"+str(pM)+"_"+str(test_ke)+".csv"
save_to = "result_"+weight_name
save = directory+"/"+save_to
print 
final_result = int(num_hidden),int(pop_size),int(gen_limit),pC,pM,np.mean(f1measure), np.mean(msex), np.mean(akurasi)
# print np.array(final_result)
print "F1-Measure : " + str(np.mean(f1measure)*100)
print "Akurasi : " + str(np.mean(akurasi))
np.savetxt(save, np.array(final_result), newline=',')

# match = 0
# for i in range(len(inps)):
#  	if(jst.correct(inps[i],weights)):
#  		match += 1
# print match,len(inps)
# print "Persentase kecocokan = "+str((match*100)/len(inps))+"%"

#print num_hidden,weight_interval,pop_size,gen_limit,'ret = 1/(1+np.exp((-0.001*x)))'
