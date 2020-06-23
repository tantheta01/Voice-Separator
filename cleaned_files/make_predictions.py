from postpredictions import *
from song import *
from model import *
import pickle
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler
import librosa


def load_pretrained_model(model_path):
	'''
We load the model withut custom obects since we just have to make predictions
It is necessary to compile model for predictions so we compile it with a vanilla loss
	'''
	try:
		model = tf.keras.models.load_model(model_path, compile=False)
		model.compile(loss= 'mean_squared_error', optimizer='adam')

#takes path to song and pickled model as input
def make_prediction(song_path, model):
'''
This function takes the mixture song path as the input, predicts and writes predictions
'''


	try:
		stfts, sr = load_file(song_path)
		channels = [[], [], [], []]
		for stft in stfts:


			song_mag, song_phase = librosa.magphase(stft)
			song_mag_padded, orig_time_length = zero_pad(song_mag)
			song_phase_padded, _ = zero_pad(song_phase)
			freq, time_length= song_mag_padded.shape
			x_for_model=np.zeros((time_length//50, 513, 50, 1))
			for i in range(time_length//50):
				x_for_model[i,:,:,:]=song_mag_padded[:,i*50:(i+1)*50].reshape(513,50,1)

			temp_dataset={'x_test':x_for_model}
			bass, drums, vocals, others=test_model(temp_dataset, model)
			bass_istft, drums_istft, vocals_istft, others_istft = get_istft(x, song_mag_padded, bass), get_istft(x,song_mag_padded,drums),get_istft(x,song_mag_padded,vocals),get_istft(x,song_mag_padded,others)
			channels[0].append(bass_istft)
			channels[1].append(drums_istft)
			channels[2].append(vocals_istft)
			channels[3].append(others_istft)
			# output_path=song_path[:-4]+"_output"+".wav"
		bass_path = song_path[:-4]+"_bass"+".wav"
		drums_path = song_path[:-4]+"_drums"+".wav"
		vocals_path = song_path[:-4]+"_vocals"+".wav"
		others_path = song_path[:-4]+"_others"+".wav"

		bass_audio = np.array(channels[0])
		drums_audio = np.array(channels[1])
		vocals_audio = np.array(channels[2])
		others_audio = np.array(channels[3])


		write_file(bass_audio, sample_rate bass_path)
		write_file(drums_audio, sample_rate, drums_path)
		write_file(vocals_audio, sample_rate, vocals_path)
		write_file(vocals_audio, sample_rate, vocals_path)
		print("Output saving ")
	except:
		print("Invalid song path")
		return
			
	return output_path	#cuz why not


def zero_pad(arr):

	arr_new = np.zeros((arr.shape[0], int((arr.shape[1]-1)/50)*50 + 50))
	arr_new[:, :arr.shape[1]] = arr
	return arr_new, arr.shape[1]
			# song_stft, sample_rate=load_file(song_path)
			song_mag, song_phase= get_mag_phase(x)
			# try:
			# 	model = tf.keras.load_model(model_path, compile=False)	
			# except:
			# 	print("Invalid model path")
			# 	return