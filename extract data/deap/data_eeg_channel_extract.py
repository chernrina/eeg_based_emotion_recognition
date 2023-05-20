# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import cPickle

data = pd.DataFrame()

for elem in range(1,33):
	print(elem)

	name = 'data_preprocessed_python/s'
	if elem < 10:
		name += '0'
	name += str(elem) + '.dat'
	x = cPickle.load(open(name, 'rb'))
	eeg = []
	for i in range(40):
		eeg.append(x['data'][i,2,:]) # i - номер эксперимента, 2 - канал fp3, : - все значения
	data = pd.concat([data, pd.DataFrame(eeg)],ignore_index=True)
	print(data.shape)

pd.DataFrame(data).to_csv('eeg_fp3_all.csv')
