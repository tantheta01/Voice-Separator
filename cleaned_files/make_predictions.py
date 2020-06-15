from postpredictions import *
from song import *
from model import *
import pickle
import numpy as np
import tensorflow as tf

#takes path to song and pickled model as input
def make_prediction(song_path, model_path):
	try:
		for x, sample_rate in load_file(song_path):
			# song_stft, sample_rate=load_file(song_path)
			song_mag, song_phase= get_mag_phase(x)
			try:
				model = tf.keras.load_model(model_path, compile=False)	
			except:
				print("Invalid model path")
				return
			song_mag_padded, orig_time_length = zero_pad(song_mag)
			song_phase_padded, _ = zero_pad(song_phase)
			freq, time_length= song_mag_padded.shape
			x_for_model=np.zeros((time_length//50, 513, 50, 1))
			for i in range(time_length//50):
				x_for_model[i,:,:,:]=song_mag_padded[:,i*50:(i+1)*50].reshape(513,50,1)
			temp_dataset={'x_test':x_for_model}
			bass, drums, vocals, others=test_model(temp_dataset, model)
			bass_istft, drums_istft, vocals_istft, others_istft = get_istft(x, song_mag_padded, bass), get_istft(x,song_mag_padded,drums),get_istft(x,song_mag_padded,vocals),get_istft(x,song_mag_padded,others)
			# output_path=song_path[:-4]+"_output"+".wav"
			bass_path = song_path[:-4]+"_bass"+".wav"
			drums_path = song_path[:-4]+"_drums"+".wav"
			vocals_path = song_path[:-4]+"_vocals"+".wav"
			others_path = song_path[:-4]+"_others"+".wav"

			driver(bass_istft, bass_path)
			driver(drums_istft, drums_path)
			driver(vocals_istft, vocals_path)
			driver(vocals_istft, vocals_path)
			print("Output saving ")
	except:
		print("Invalid song path")
		return
			
	return output_path	#cuz why not


def zero_pad(arr):

	arr_new = np.zeros((arr.shape[0], int((arr.shape[1]-1)/50)*50 + 50))
	arr_new[:, :arr.shape[1]] = arr
	return arr_new, arr.shape[1]