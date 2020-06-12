#this file is to convert the predicted mags back to stft, hen take the istft and write to file
#this file encompasses only one song file
import sys
import numpy as np
import librosa



def get_stft(input_stft,input_mag,predicted_mag):
	if input_stft.shape != predicted_mag.shape or input_stft.shape != input_mag.shape:
		print("input_stft, predicted_mag, input_mag shape mismatch")
		sys.exit()

	else:
		return input_stft*predicted_mag/input_mag


def convert_to_wav(pred_stft, outfile, hop_length=256):
    pred=librosa.istft(pred_stft,hop_length)
	librosa.output.write_wav(path=outfile, y=pred, hop_length=hop_length, sr=22050)



def driver(y_pred,input_mag,input_stft,output_path, hoplength=256): #recieves the predictions by models file
	#Complete this function it shall call convert to wav and get stft
	#dimensions of y_pred are (a,513,25,1) matlab 4D
	#input mag nd input stft, and the predicted mag has dimensions (513,25*a)## actually might be (25*a)+b; b<25
    #TODO deal with problem in previous line
    y_pred=y_pred.reshape(y_pred.shape[0],513,25)
    pred_mag=np.zeros((513,25*y_pred.shape[0]))
    for i in range(y_pred.shape[0]):
            curr_pred=y_pred[i,:,:].reshape(513,25)
            pred_mag[:,i*25:(i+1)*25]=curr_pred
    pred_stft=get_stft(input_stft,input_mag,pred_mag)
    convert_to_wav(pred_stft,output_path, hoplength)
    return output_path      #optional, couldnt think of anything else to return
	
