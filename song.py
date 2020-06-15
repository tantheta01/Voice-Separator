# given a song path, read the file in chunks, load it, compute stft, and yield sample rate and stft
import librosa
import os




def load_file(filepath):

	sr = librosa.get_samplerate(filepath)

	frame_length = 1024
	hop_length = 256

	stream = librosa.stream(filepath, block_length = 128, frame_length = 1024, hop_length = 256)

	for x in stream:
		yield (librosa.stft(x, n_fft = 1024, hop_length=256), sr)

