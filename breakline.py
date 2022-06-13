import Loader as load
import numpy as np

def breakline(file):
	data = load.loadCsv(file)
	lenght = len(data)
	col = 8
	row = 12
	k = 0
	dat = np.zeros((row,col))
	for i in xrange(row):
		for j in xrange(col):
			dat[i][j] = data[k]
			k += 1
	np.savetxt(file,np.array(dat), delimiter = ',')

breakline("merged.csv")