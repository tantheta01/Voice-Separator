# This file implements our preprocessing of the musdb18 dataset
import stempeg
import numpy as np
import librosa
from sklearn.preprocessing import MinMaxScaler
import os

def separate_track(song, channel=0):
	mix = song[0, :, channel].reshape((-1,))
	drums = song[1, :, channel].reshape((-1,))
	bass = song[2, :, channel].reshape((-1,))
	others = song[3, :, channel].reshape((-1, ))
	vocals = song[4, :, channel].reshape((-1, ))
	return (mix, bass, vocals, drums, others)

def stft_n_others(channel):
	stft = librosa.stft(channel, n_fft = 1024, hop_length = 256)
	mag_channel, phase_channel = librosa.magphase(stft)
	db = librosa.amplitude_to_db(mag_channel)
	return db
  # return stft, mag_channel, phase_channel, db


def get_data(matrix):
	fbins, tbins = matrix.shape
	data = np.zeros((int((tbins-1)/25) + 1, fbins, 25))
	for i in range(int(tbins/25)):
		data[i, :, :] = matrix[:, i*25: (i+1)*25]
	return data

def read_dir(dir_, nsongs=100, channel=0, train=True):
	
	L = os.listdir(dir_)[:nsongs]
	for l in L:
		song_path = str(dir_) + str(l)
		song, sample_rate = stempeg.load(song_path)
		if train=True:
			mix, bass, vocals, drums, others = separate_track(song, channel = channel)
			mix_db, bass_db, drums_db, others_db, vocals_db = stft_n_others(mix), stft_n_others(bass), stft_n_others(drums), stft_n_others(others), stft_n_others(vocals)
			mix_data, bass_data, drums_data, others_data, vocals_data = get_data(mix_db), get_data(bass_db), get_data(drums_db), get_data(others_db), get_data(vocals_db)
			yield mix_data, [bass_data, drums_data, others_data, vocals_data]

		


