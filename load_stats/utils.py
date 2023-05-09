# utils.py

import json
import os


# assuming the top level project directory is the second directory up
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class cd:
	""" Context manager for changing the working directory. """
	def __init__(self, newPath):
		# expanduser changes ~/file.txt -> /home/files/file.txt
		self.newPath = os.path.expanduser(newPath)

	def __enter__(self):
		self.savedPath = os.getcwd()
		self.oneUpPath = os.path.abspath(os.path.join(self.newPath, os.pardir))
		self.twoUpPath = os.path.abspath(os.path.join(self.oneUpPath, os.pardir))
		# change working directory
		os.chdir(self.newPath)
		return self

	# etype, value, traceback for throwing exceptions
	def __exit__(self, etype, value, traceback):
		# change back to original directory
		os.chdir(self.savedPath)


def _get_model(row):
	""" Returns JSON model for _load_players(). """
	try:
		with open('data.json', 'r') as file:
			data = json.load(file)
			for i in (model := data[row['Position']]):
				model[i] = row[i]

			return model

	except FileNotFoundError:
		print(os.listdir())


def find_path(*, root, file="", dir=""):
	for relPath,dirs,files in os.walk(root):
		if(file in files):
			full_path = os.path.join(root,relPath,file)
			return full_path
		if(dir in dirs):
			full_path = os.path.join(root,relPath,dir)
			return full_path