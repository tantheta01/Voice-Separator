from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, Conv2D, Conv2DTranspose
import tensorflow.keras.backend as K
from tensorflow.keras.layers import ZeroPadding2D, Concatenate, Flatten, Input, Reshape
import tensorboard
import datetime
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler
import librosa
import os
import numpy as np
import random
random.seed(0)
import musdb
mus = musdb.DB(root = 'drive/My Drive/')
tf.compat.v1.disable_eager_execution()


def custom_loss(drums, vocals, others):

  def loss_fun(y_true, y_pred):
    l1 = K.mean((K.square(y_true-y_pred)), axis=-1)
    l2 = K.mean((K.square(y_pred-others)), axis=-1) + K.mean((K.square(drums-others)), axis=-1)
    l3 = K.mean((K.square(vocals-others)), axis=-1)
    l4 = K.mean((K.square(drums-y_pred)), axis=-1) + K.mean((K.square(vocals-y_pred)), axis=-1) + K.mean((K.square(vocals-drums)), axis=-1)
    return l1 - 0.1*l2 - 0.3*l3 - 0.1*l4

  return loss_fun

 def custom_loss2(y_true, y_pred, penalty = 10):
 	def penalty_loss(y_true, y_pred):
 		return penalty*K.mean(K.square(y_true - y_pred))

def model_get(inp_shape = (513, 50, 1), hconv = (449,1), vconv = (1,25), Dense_b = (512, 512, 65*26), reshape_block = (65, 26, 1)):
	inp = Input(inp_shape)
	houtp = Conv2D(1, hconv)(inp)
	voutp = Conv2D(1, vconv)(inp)
	houtp = Conv2D(1, vconv)(houtp)
	voutp = Conv2D(1, hconv)(voutp)
	outp = Concatenate()([houtp, voutp])
	outp = Flatten()(outp)
	outp = Dense(units= Dense_b[0], activation = 'relu')(outp)
	bass = Dense(units = Dense_b[1], activation = 'relu')(outp)
	drums = Dense(units = Dense_b[1], activation = 'relu')(outp)
	vocals = Dense(units = Dense_b[1], activation = 'relu')(outp)
	others = Dense(units = Dense_b[1], activation = 'relu')(outp)
	bass = Dense(units = Dense_b[2], activation = 'relu')(bass)
	drums = Dense(units = Dense_b[2], activation = 'relu')(drums)
	vocals = Dense(units = Dense_b[2], activation = 'relu')(vocals)
	others = Dense(units = Dense_b[2], activation = 'relu')(others)
	r = Reshape(reshape_block)
	bass = r(bass)
	drums = r(drums)
	vocals = r(vocals)
	others = r(others)
	bass = Conv2DTranspose(1, vconv)(bass)
	bass = Conv2DTranspose(1, hconv)(bass)
	drums = Conv2DTranspose(1, vconv)(drums)
	drums = Conv2DTranspose(1, hconv)(drums)
	vocals = Conv2DTranspose(1, vconv)(vocals)
	vocals = Conv2DTranspose(1, hconv)(vocals)
	others = Conv2DTranspose(1, vconv)(others)
	others = Conv2DTranspose(1, hconv)(others)
	model = Model(inp, [bass, drums, vocals, others])
	return model



def compile_model(model, loss = None, optimizer = 'adam'):
	if loss is None:
		drums = model.get_layer(name='drums').output
		vocals = model.get_layer(name='vocals').output
		others = model.get_layer(name='others').output
		loss = {'bass' : custom_loss(model, drums, vocals, others), 'vocals' : customloss2(penalty=10), 'drums' : 'mean_squared_error', 'others' : customloss2}

	model.compile(loss=loss, optimizer = optimizer)
	return model






