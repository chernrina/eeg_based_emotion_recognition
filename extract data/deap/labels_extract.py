import numpy as np
import pandas as pd
import cPickle

data = []

for elem in range(1,33):
	print(elem)

	name = 'data_preprocessed_python/s'
	if elem < 10:
		name += '0'
	name += str(elem) + '.dat'
	x = cPickle.load(open(name, 'rb'))
	if elem == 1:
		data = x['labels']
	else:
		data = np.vstack((data, x['labels']))

pd.DataFrame(data).to_csv('deap_all_labels.csv')