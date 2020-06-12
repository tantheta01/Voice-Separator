# This file exists for training and making predictions 
import os
from model_new import compile_model

def apply_model(model_dir, datagen, train = True, output_write_path = 'test/predictions'):
	model = tf.keras.models.load_model(model_dir, compile = False)
	model = compile_model(model)

	if train:
		for x, y in datagen:
			model.fit(x, y)
			model.save(model_dir)

	else:
		if not os.is_dir(output_write_path):
			os.mkdir(output_write_path)
		for x in datagen:
			y = model.predict(x)
			Y = 

def separate_song(model, song, folder)

def predict(saved_model, song):

	model = compile_and_load(saved_model)
	if os.is_dir(song):
		os.mkdir(song + '/predictions')
		L = os.listdir(song)
		for l in L:
			if l.split('.')[-1] == 'wav':
				separate_song(model, song + '/' + l, song + '/' + 'predictions')


	else:
		separate_song(model, song, 'predictions')

