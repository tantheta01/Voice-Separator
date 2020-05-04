# Driver Function
import song
import dataset
import preprocessing
import model
import sys


def main():
	data = str(input("Directory where the files exist"))	#the name of the directory
	mixture_data, bass_data, drums_data, vocals_data, others_data = read_data(data)

	print("Kindly select instrument to separate")
	print("1.bass 2.drums 3.vocals 4.others")
	x = int(input())
	instrument=None
	if x==1:
		instrument=bass_data
	elif x==2:
		instrument=drums_data
	elif x==3:
		instrument=vocals_data
	elif x==4:
		instrument=others_data

	if instrument is not None:
		dataset = get_train_data(mixture_data, instrument, 25)
	else:
		print("Kindly give input b/w 1 to 4")
		sys.exit()

	trained_model = train_model(dataset, 100)

