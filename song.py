#this contains the preprocessing of the song

import librosa
import numpy as np
import pandas as pd


def load_file(filepath ,sr = None):
	# we shall get 2 channels as we read the filepath, i.e. 2 one dimensional arrays
	# librosa returns the array and the sampling rate. we get both the arrays if we set mono= False in load function, else we get mean of both arrays
	channel, sampling_rate = librosa.load(filepath, sr)
	# we shall process the 2 channels separately
	stft_channel1 = librosa.stft(channel1)
# 	stft_channel2 = librosa.stft(channel2)
	return stft_channel1, sampling_rate


def get_mag_phase(stft_channel):
	# compute the magnitude and phase of the channel
	mag_channel, phase_channel = librosa.magphase(stft_channel)
	return mag_channel, phase_channel

def add_zeros(matrix_original, new_size):
	new_matrix = np.zeros(new_size, dtype=float)
	new_matrix[:,:matrix_original.shape[1]]=matrix_original
	return new_matrix

#now the length of each magnitude matrix has been made multiple of 25 by padding with zeros. phase matrix is still the same shape

def padding(file_mag):
	file_mag = add_zeros(file_mag, (file_mag.shape[0], int((file_mag.shape[1]-1)/25)+1))
	return file_mag


def data_augmentation(stft):
	augmented_stft = np.zeros(stft.shape, dtype=complex)
	for i in range(stft.shape[1]):
		augmented_stft[:, i] = stft[:, stft.shape[1]-1-i]
	return augmented_stft
