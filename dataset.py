# To read our final list of songs and preprocesing them

# To read our final list of songs and preprocesing them
import numpy as np
import pandas as pd
from song import *
import os 

# input is in shape ()
def read_data(diretory_path):
	# This function reads the mixtures, bass, drums, vocals and others

	mixture_data = read_folder(diretory_path,'mixture')
	bass_data = read_folder(diretory_path,'bass')
	drums_data = read_folder(diretory_path,'drums')
	vocals_data = read_folder(diretory_path,'vocals')
	others_data = read_folder(diretory_path,'others')

	if len(mixture_data[0])!=len(bass_data[0]) or len(mixture_data[0])!=len(drums_data[0]) or len(mixture_data[0])!=len(vocals_data[0]) or len(mixture_data[0])!=len(others_data[0]):
		print("directory sizes me ghapla, plzz check")

	return mixture_data, bass_data, drums_data, vocals_data, others_data



#common function to read all instruments
def read_folder(diretory_path, file_type):

	instrument = [[], []]
	#2 lists, 1 for magnitude 1 for phase
	#here file contains the path
	for file in all_of_a_type(file_type,diretory_path):
		file_stft, sr = load_file(file)
		mag_channel, phase_channel = get_mag_phase(file_stft)
		instrument[0].append(mag_channel)
		instrument[1].append(phase_channel)
		return instrument



def all_of_a_type(file_type,path):
	#returns all filepaths of a type(here mixture,bass etc)  provided they are saved as file_type.wav
    l=[]
    for file_path in [os.path.join(path,file_name) for file_name in os.listdir(path)]:
        if(os.path.isdir(file_path)):
            l.extend(all_of_a_type(file_type,file_path))
        elif (os.path.splitext(os.path.basename(file_path))[0]==file_type and os.path.splitext(os.path.basename(file_path))[1]=='.wav'):
            l.append(file_path)
    return l
    