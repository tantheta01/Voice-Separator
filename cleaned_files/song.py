# given a song path, read the file in chunks, load it, compute stft, and yield sample rate and stft
import librosa
import os
from scipy.io.wavfile import write, read




def load_file(filepath):
	'''
	We load the song and check for the number of channels.
	If it has one channel then we return the stft and the samplerate. 
	Else we return the individual stft of each channel and the smple rate
	'''

	sr, song = read(filepath)
	stft_list = []
	for channel_num in song.shape[1]:
		channel_stft = librosa.stft(song[:, i], n_fft = 1024, hop_length = 256)
		stft_list.append(channel_stft)

	return stft_list, sr


	# return sr, song

def write_file(istft, rate, filepath):

'''
Given an ISTFT that is the prediction of the model it writes the istft to the corrresponding file path
ISTFT shape is (n_samples, n_channels)
'''
assert len(istft.shape) == 2, "Invalid ISTFT shape to write predictions"
assert istft.shape[1]<=2, "n_channels cannot exceed 2"
try:
	write(filepath, rate, istft)

except:
	print("Check the filepath, maybe invalid" + filepath)


def iterate_dir(directory_name, model):

	if directory_name[-1] != '/':
		directory_name += '/'

		
	L = os.listdir(directory_name)
	for file in L:
		if file[-4:] == '.wav':
			make_prediction(model, directory_name + file)
