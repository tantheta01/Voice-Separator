import librosa
import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import *
from tensorflow.keras.models import *

#This model implements our functional API model
#Functional API shall make possible greater connections between input and output and ensuring greater flexibility
#Above all we are trying to make 3 parallel predictions using a single model.



def func_model(input_shape=(25, 513, 1), Con1 = None, MaxP=None, Con2 = None, dense=None, reshape=None, ConT2 = None, Ups = None, ConT1 = None):
# Con1 is like [64, (3,3)]
# Maxp is like (2,2)
# Con2 is a dict, {'bass' : [64, (3,3)], 'vocals' : [32, (2,2)], etc, etc}
# dense is a dict, {'bass' : [512,512,1234], etc}
# reshape is a dict, (values are tuples)
# ConT2 is a dict
# Ups is a dict
# ConT1 is a dict


# Extracting Parameters
 	Con2_bass, Con2_vocals, Con2_drums, Con2_others = Con2['bass'], Con2['vocals'], Con2['drums'], Con2['others']
 	dense_bass, dense_vocals, dense_drums, dense_others = dense['bass'], dense['vocals'], dense['drums'], dense['others']
 	reshape_bass, reshape_vocals, reshape_drums, reshape_others = reshape['bass'], reshape['vocals'], reshape['drums'], reshape['others']
 	ConT2_bass, ConT2_vocals, ConT2_drums, ConT2_others = ConT2['bass'], ConT2['vocals'], ConT2['drums'], ConT2['others']
 	Ups_bass, Ups_vocals, Ups_drums, Ups_others = Ups['bass'], Ups['vocals'], Ups['drums'], Ups['others']
 	ConT1_bass, ConT1_vocals, ConT1_drums, ConT1_others = ConT1['bass'], ConT1['vocals'], ConT1['drums'], ConT1['others']
	
	inp = Input(shape = input_shape)
	inp_ = Conv2D(Con1[0], Con1[1])(inp)
	inp_ = MaxPool2D(MaxP)(inp_)

	inp_bass = Conv2D(Con2_bass[0], Con2_bass[1])(inp_)
	inp_vocals = Conv2D(Con2_vocals[0], Con2_vocals[1])(inp_)
	inp_drums = Conv2D(Con2_drums[0], Con2_drums[1])(inp_)
	inp_others = Conv2D(Con2_others[0], Con2_others[1])(inp_)

	inp_bass = Flatten()(inp_bass)
	inp_vocals = Flatten()(inp_vocals)
	inp_drums = Flatten()(inp_drums)
	inp_others = Flatten()(inp_others)

	for layer in dense_bass:
		inp_bass =Dense(layer, activation='relu')(inp_bass)
	for layer in dense_vocals:
		inp_vocals =Dense(layer, activation='relu')(inp_vocals)
	for layer in dense_drums:
		inp_drums =Dense(layer, activation='relu')(inp_drums)
	for layer in dense_others:
		inp_others =Dense(layer, activation='relu')(inp_others)

	inp_bass = Reshape(reshape_bass)(inp_bass)
	inp_drums = Reshape(reshape_drums)(inp_drums)
	inp_others = Reshape(reshape_others)(inp_others)
	inp_vocals = Reshape(reshape_vocals)(inp_vocals)

	inp_bass = Conv2DTranspose(ConT2_bass[0], ConT2_bass[1])(inp_bass)
	inp_vocals = Conv2DTranspose(ConT2_vocals[0], ConT2_vocals[1])(inp_vocals)
	inp_drums = Conv2DTranspose(ConT2_drums[0], ConT2_drums[1])(inp_drums)
	inp_others = Conv2DTranspose(ConT2_others[0], ConT2_others[1])(inp_others)

	inp_bass = UpSampling2D(Ups_bass)(inp_bass)
	inp_others = UpSampling2D(Ups_others)(inp_others)
	inp_drums = UpSampling2D(Ups_drums)(inp_drums)
	inp_vocals = UpSampling2D(Ups_vocals)(inp_vocals)

	inp_bass = Conv2DTranspose(ConT1_bass[0], ConT1_bass[1])(inp_bass)
	inp_vocals = Conv2DTranspose(ConT1_vocals[0], ConT1_vocals[1])(inp_vocals)
	inp_drums = Conv2DTranspose(ConT1_drums[0], ConT1_drums[1])(inp_drums)
	inp_others = Conv2DTranspose(ConT1_others[0], ConT1_others[1])(inp_others)


	model = Model(inp, [inp_bass, inp_drums, inp_others, inp_vocals])
	model.compile(loss = 'mean_squared_error', optimizer = 'adam')
	return model




Con1 = [1, (2,2)]
MaxP = (2,2)
Con2 = {
	'bass' : [1, (2,2)],
	'vocals' : [1, (2,2)],
	'others' : [1, (2,2)],
	'drums' : [1, (2,2)]
}
dense = {
	'bass' : [1024, 1024, 255*11],
	'vocals' : [1024, 1024, 255*11],
	'others' : [1024, 1024, 255*11],
	'drums' : [1024, 1024, 255*11]
}
reshape = {
	'bass' : (255,11,1),
	'vocals' : (255,11,1),
	'others' : (255,11,1),
	'drums' : (255,11,1),
}
ConT2 = {
	'bass' : [1, (2,2)],
	'vocals' : [1, (2,2)],
	'others' : [1, (2,2)],
	'drums' : [1, (2,2)]
}

Ups = {
	'bass' : (2,2),
	'vocals' : (2,2),
	'others' : (2,2),
	'drums' : (2,2),
}

ConT1 = {
	'bass' : [1, (2,2)],
	'vocals' : [1, (2,2)],
	'others' : [1, (2,2)],
	'drums' : [1, (2,2)]
}

model = func_model(Con1 = Con1, MaxP = MaxP, Con2 = Con2, dense = dense, reshape = reshape, ConT2 = ConT2, Ups = Ups, ConT1 = ConT1)





	



