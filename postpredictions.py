#this file is to convert the predicted mags back to stft, hen take the istft and write to file
#this file encompasses only one song file
import sys
import numpy as np
import librosa



def get_stft(input_stft,input_mag,predicted_mag):
	if input_stft.shape != predicted_mag.shape or input_stft.shape != input_mag.shape:
		print("input_stft, prdicted_mag, input_mag shape mismatch")
		sys.exit()

	else:
		return input_stft*predicted_mag/input_mag


def convert_to_wav(pred_stft, outfile, hop_length):
	librosa.output.write_wav(path=outfile, y=pred_stft, hop_length=hop_length, sr=22050)



def driver(y_pred,input_mag,input_stft): #recieves the predictins by models file
	#Complete this function it shall call convert to wav and get stft
	#dimensions of y_pred are (something,513,25,1) matlab 4D
	#input mag nd input stft, and the predicted mag has dimensions (513,25*something)
	