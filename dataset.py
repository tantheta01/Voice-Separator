# To read our final list of songs and preprocesing them

# To read our final list of songs and preprocesing them

import numpy as np
import pandas as pd
from song import *
import os 

# input is in shape ()
def read_data(diretory_name):
	# This function reads the mixtures, bass, drums, vocals and others


	mixtures_path = '/mixtures/'
	bass_path = '/bass/'
	drums_path = '/drums/'
	vocals_path = '/vocals/'
	others_path = '/others/'


	mixture_data = read_folder(diretory_name, mixtures_path)
	bass_data = read_folder(diretory_name, bass_path)
	drums_data = read_folder(diretory_name, drums_path)
	vocals_data = read_folder(diretory_name, vocals_path)
	others_data = read_folder(diretory_name, others_path)

	if len(mixture_data[0])!=len(bass_data[0]) or len(mixture_data[0])!=len(drums_data[0]) or len(mixture_data[0])!=len(vocals_data[0]) or len(mixture_data[0])!=len(others_data[0]):
		print("directory sizes me ghapla, plzz check")

	return mixture_data, bass_data, drums_data, vocals_data, others_data



#common function to read all instruments
def read_folder(diretory_name, folder):

	instrument = [[], []]
	#2 lists, 1 for magnitude 1 for phase
	for file in os.listdir(folder_name):
		file_stft, sr = load_file(str(diretory_name) + str(folder_name) + str(file))
		mag_channel, phase_channel = get_mag_phase(file_stft)
		instrument[0].append(mag_channel)
		instrument[1].append(phase_channel)
	return instrument
