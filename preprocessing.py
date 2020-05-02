# In this file we take as input the magnitudes calculated from dataset file and 
# Conveert it to useable form by models
# All the audio dataset which is supplied by dataset file shall be made into a single array. 
# Kindly read code before use
import numpy as np
import sys

def divide_data(audio_list, length):
	# converts our lists to np arrays
	data=None
	for mag in data[0]:
		for x in range(int(mag.shape[1]/length) - 1):
			if data is None:
				data=mag[:, x*length : (x+1)*length]
			else:
				data = np.vstack(data, mag[:, x*length: (x+1)*length])
	return data


def get_train_data(mixture_list, instrument_list, length):
	# This list is the one returned by the dataset file i.e. contains 2 concatenated lists.
	# We shall use only the magnitude data here.

	num_mixtures = len(mixture_list[0])
	num_instruments = len(instrument_list[0])

	if num_mixtures!=num_instruments:
		print("Length of mixtures and instruments mismatch")
		sys.exit("Byee")
	else:
		train_data = divide_data(mixture_list, length)
		test_data = divide_data(instrument_list, length)
	dataset = {}
	dataset['train_data'] = train_data
	dataset['test_data'] = test_data
	return dataset