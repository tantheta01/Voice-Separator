import numpy as np 
import librosa
import sys




def get_istft(mix_stft, input_mag, pred):
    #this function returns istft of the predictions
    #shape of pred and input_mag is (x,513,50,1) and shape of mix_stft is (513,y) where y=50*(x-1)+r and 0<r=<50 
    if pred.shape!=input_mag.shape :
        print("parameters size mismatch")
        sys.exit()
    else:
        input_mag , pred  =  input_mag(input_mag.shape[0],513,50) , pred.reshape(pred.shape[0],513,50)
        mix_mag , pred_mag = np.zeros((513,50*input_mag.shape[0])) , np.zeros((513,50*pred.shape[0]))


        for i in range(pred.shape[0]):
            ith_pred=input_mag[i,:,:].reshape(513,50)
            mix_mag[:,i*50:(i+1)*50]=ith_pred

        for i in range(pred.shape[0]):
            ith_pred=pred[i,:,:].reshape(513,50)
            pred_mag[:,i*50:(i+1)*50]=ith_pred
        
        mix_mag , pred_mag = mix_mag[:,:-(50*input_mag.shape[0]-mix_stft[1])] , pred_mag[:,:-(50*pred.shape[0]-mix_stft[1])] 
        
        if mix_stft.shape! = pred_mag.shape:
            print("mix_stft size mismatch")
            sys.exit()

        pred_stft=mix_stft*pred_mag/input_mag
        pred_istft=librosa.istft(pred_stft, hop_length = 256)

        return pred_istft