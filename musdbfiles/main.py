# To train the network run python3 main.py (There must be the directories test and train in your cwd) or python3 main.py train path/to/dir/containing/train/and/test
# To make predictions on a particular song, python3 main.py path/to/song


import sys
import os


def main():
	if len(sys.argv) == 1 or len(sys.argv) == 3:

		train_and_test_dir = os.pardir()

		if len(sys.argv) == 3:
			train_and_test_dir = sys.argv[-1]

		dataset = create_dataset(train_and_test_dir)
		model = perform_training(dataset)

	elif len(sys.argv) == 2:
		if 'trained_model' not in os.listdir(os.pardir()):
			print('pretrained model not found')
			sys.exit()

		predict(trained_model, sys.argv[-1])
