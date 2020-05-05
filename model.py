# Contains the model

# Contains the model
import librosa
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import Dropout
from keras.layers import Flatten
from keras.layers import Reshape
from keras.layers import Dense
from keras.layers import UpSampling2D
from keras.layers import Conv2DTranspose
from keras.layers import BatchNormalization
from keras.layers import MaxPool2D
import numpy as np
from keras.layers import BatchNormalization
import keras
import sys

def custom_loss(y_actual,y_pred):
	loss=y_actual-y_pred
	loss=tf.keras.backend.abs(loss)
	loss=loss*loss
	loss=tf.keras.backend.sum(loss)
	return loss

def build_model(conv1st=None,maxPooling=None,conv2nd=None,Connected=None,reshape=None,convT2nd=None,upSampling=None,convT1st=None,optimizer='adam',loss='mean_squared_error'):
  classifier=Sequential()
  if conv1st is not None:
    classifier.add(Conv2D(conv1st[0], (conv1st[1],conv1st[2]),input_shape=(513,25,1),kernel_initializer='uniform'))
  if maxPooling is not None:
    classifier.add(MaxPool2D(pool_size=(maxPooling[0],maxPooling[1])))
  if conv2nd is not None:
    # adding padding(pata nhi kyu)
    classifier.add(Conv2D(conv2nd[0],(conv2nd[1],conv2nd[2]),kernel_initializer='uniform', padding='same'))
  classifier.add(Flatten())
  if Dense is not None:
    for layer in Connected:
      classifier.add(Dense(layer,activation='relu',kernel_initializer='uniform'))
      #adding extra batch normalization
      # classifier.add(BatchNormalization())
  if reshape is not None:
    classifier.add(Reshape(reshape))
  if convT2nd is not None:
    classifier.add(Conv2DTranspose(convT2nd[0],(convT2nd[1],convT2nd[2])))
  if upSampling is not None:
    classifier.add(UpSampling2D(size=(upSampling[0],upSampling[1])))
  if convT1st is not None:
    classifier.add(Conv2DTranspose(convT1st[0],(convT1st[1],convT1st[2])))
  classifier.compile(optimizer=optimizer, loss=loss,metrics=['accuracy'])
  return classifier

conv1st = (128,513,1)
maxPooling=None
conv2nd=(128,1,13)
connected=[512,512,512,128*25]
reshape=(1,25,128)
convT2nd=None
upSampling=None
convT1st=(1,513,1)
classifier1 = build_model(conv1st=conv1st, maxPooling=maxPooling,conv2nd=conv2nd,Connected=connected,reshape=reshape,convT2nd=convT2nd,upSampling=upSampling,convT1st=convT1st)


def train_model(dataset, epochs):
	#dataset shall be a dictionary which shall contain the appropriate x and y
	train_x = None
	train_y = None
	if 'train_x' not in dataset.keys():
		sys.exit('training set not found')
	else:
		train_x = dataset['train_x']

	if 'train_y' not in dataset.keys():
		sys.exit('train y not found')
	else:
		train_y = dataset['train_y']

	
	classifier1.fit(train_x, train_y, epochs = epochs)
	return classifier1


def test_model(dataset, model):
	x_test=None
	if 'x_test' not in dataset.keys():
		sys.exit('Test set not found')
	else x_test = dataset['x_test']
	y_pred = model.predict(x_test)
	return y_pred
