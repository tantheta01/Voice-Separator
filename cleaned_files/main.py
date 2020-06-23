# Driver Function
import song
import dataset
import preprocessing
import model
import sys
import os
from make_predictions import make_prediction, load_pretrained_model
from song import iterate_dir

def main():
	
	if len(sys.argv) < 2:
		print("please enter valid directory name")

	######------loading model-------#####
	model = load_pretrained_model('Model/model/')


	song_path = str(sys.argv[1])
	if os.path.isdir(song_path):
		iterate_dir(model, song_path)

	else:
		try:
			if song_path.split('.')[-1] == 'wav':
				make_prediction(model, song_path)
				print("Prediction complete for" + song_path)

			else:
				print("Kindly enter a wav file for separation")

		except:
			print("please check th file again and retry")


if __name__ == "__main__":
	main()