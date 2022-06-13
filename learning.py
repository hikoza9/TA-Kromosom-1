# import Loader
import JST
import ES
import os
# import coba
import sys
import time
import numpy as np

num_input = int(sys.argv[1])
num_hidden = int(sys.argv[2])
num_output = int(sys.argv[3])

#weight_interval = int(sys.argv[4])
pop_size = int(sys.argv[4])
gen_limit = int(sys.argv[5])
pC = float(sys.argv[6])
pM = float(sys.argv[7])

train_ke = int(sys.argv[8])
#data = sys.argv[9]

# format = data_learning[-4:-1]+data_learning[-1]


# save_weights_to = sys.argv[8]

start = time.time()

# inps = Loader.loadNormalizedCsv(data)

# if (format == '.dat'):
# 	inps = loader.loadDat(data_learning)
# elif (format == '.csv'):
# 	inps = loader.loadCsv(data_learning)

# inps = loader.stringifyVar(inps,loader.normalizeVar(loader.getVar(inps)))
# print inps
for i in xrange(5):
	data_name = "train"+str(i)+".csv"
	data_path = '.\\data training\\'
	data = data_path+data_name
	save_path = './weight/'
	save_weights_to = data_name+"_"+str(num_input)+"_"+str(num_hidden)+"_"+str(num_output)+"_"+str(pop_size)+"_"+str(gen_limit)+"_"+str(pC)+"_"+str(pM)+"_"+str(train_ke)+".csv"
	weights = ES.es((num_output*num_hidden)+(num_hidden*num_input),pop_size,gen_limit,pC,pM,num_input,num_hidden,num_output,data)
# weights = coba.es((num_output*num_hidden)+(num_hidden*num_input),weight_interval,pop_size,gen_limit,num_input,num_hidden,num_output,data)
	new_folder = str(num_input)+"_"+str(num_hidden)+"_"+str(num_output)+"_"+str(pop_size)+"_"+str(gen_limit)+"_"+str(pC)+"_"+str(pM)
	directory = save_path+new_folder
	save = directory+"/"+save_weights_to
	if not os.path.exists(directory):
		os.makedirs(directory)
	np.savetxt(save, np.array(weights), delimiter=',')

end = time.time()
# print 'waktu = ',(end - start)/3600, 'jam'
print 'waktu = ',end - start