# Contains the model

# Contains the model
import librosa
import keras
import IPython as ip
import numpy as np
import tensorflow as tf
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers import MaxPool2D
from keras.layers import Conv2D
from keras.layers import Dropout
from keras.layers import Reshape
from keras.layers import Deconvolution2D
import sys

def custom_loss(y_actual,y_pred):
	loss=y_actual-y_pred
	loss=tf.keras.backend.abs(loss)
	loss=loss*loss
	loss=tf.keras.backend.sum(loss)
	return loss

def model():
	# these input dimensions are as of now 
	# we may modify them later if need be
	model=keras.models.Sequential()
	model.add(Conv2D(50,(513,1),input_shape=(513,25,1)))
	model.add(Conv2D(30,(1,12)))
	model.add(Flatten())
	model.add(Dense(128))
	model.add(Dense(420))
	model.add(Reshape((1,14,30)))
	model.add(Deconvolution2D(50,(1,12)))
	model.add(Deconvolution2D(1,(513,1)))
	model.compile(optimizer='adadelta',loss=custom_loss, metrics=['accuracy'])
	return model


def train_model(dataset, epochs):
	#dataset shall be a dictionary which shall contain the appropriate x and y
	x_train = None
	y_train = None
	if 'x_train' not in dataset.keys():
		sys.exit('training set not found')
	else:
		x_train = dataset['x_train']

	if 'y_train' not in dataset.keys():
		sys.exit('train y not found')
	else:
		y_train = dataset['y_train']

	regressor = model()
	regressor.fit(x_train, y_train, epochs = epochs)
	return regressor


def test_model(dataset, model):
	x_test=None
	if 'x_test' not in dataset.keys():
		sys.exit('Test set not found')
	else x_test = dataset['x_test']
	y_pred = model.predict(x_test)
	return y_pred
