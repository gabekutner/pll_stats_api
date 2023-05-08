# teams.py

import os
import json
import csv

from load_stats import utils

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


# Public definitions
def init(year):
	""" Initialize the teams module. """
	_load_teams(year)


def teams():
	""" Load teams from disk. """
	global _teams
	return _teams


# Private definitions
def _load_teams(year):
	""" Load the teams from the data directory. """
	global _teams
	_teams = []

	# depending on where this is run there is an error
	# run in players.py -> use data/player_data
	# run in main.py -> use load_stats/data/player_data
	with cd('load_stats/data/team_data') as cm: 
		for file in (file := os.listdir()):
			if (file.find(str(year)+'-t')) == 0:
				print(file)
				
				for row in (csv_reader := csv.DictReader(open(file, 'r'))):

					_teams.append(row)

	return _teams

