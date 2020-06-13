from postpredictions import *
from song import *
from model import *
import pickle
import numpy as np
import tensorflow as tf

#takes path to song and pickled model as input
def make_prediction(song_path, model_path):
	try:
		song_stft, sample_rate=load_file(song_path)
		song_mag, song_phase= get_mag_phase(song_stft)
	except:
		print("Invalid song path")
		return
	try:
		model = tf.keras.load_model(model_path, compile=False)	
	except:
		print("Invalid model path")
		return
	freq, time_length= song_mag.shape
	truncation_length=time_length%25
	if truncation_length!=0:
		song_mag=song_mag[:,:-truncation_length]
		song_stft=song_stft[:,:-truncation_length]
		song_phase=song_phase[:,:-truncation_length]
	freq, time_length= song_mag.shape
	x_for_model=np.zeros((time_length//25, 513, 25, 1))
	for i in range(time_length//25):
		x_for_model[i,:,:,:]=song_mag[:,i*25:(i+1)*25].reshape(1,513,25,1)
	temp_dataset={'x_test':x_for_model}
	y_pred=test_model(temp_dataset, model)
	output_path=song_path[:-4]+"_output"+".wav"
	driver(y_pred, song_mag, song_stft, output_path)
	print("Output saved at "+output_path)
	return output_path	#cuz why not
