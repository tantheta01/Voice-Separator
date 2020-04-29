#this contains the preprocessing of the song

import librosa
import numpy as np
import pandas as pd


def load_file(filepath ,sr = None):
	# we shall get 2 channels as we read the filepath, i.e. 2 one dimensional arrays

	channel1, sr = librosa.load(filepath, sr)
	# we shall process the 2 channels separately
	stft_channel1 = librosa.stft(channel1)
	# stft_channel2 = librosa.stft(channel2)
	return stft_channel1, sr


def get_mag_phase(stft_channel):
	# compute the magnitude and phase of the channel
	mag_channel, phase_channel = librosa.magphase(stft_channel)
	return mag_channel, phase_channel

