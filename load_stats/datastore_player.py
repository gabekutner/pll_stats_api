# players.py

import os
import csv
import json

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
def init(year, season):
	""" Initialize the players module. """
	_load_players(year, season)


def players():
	""" Load players from disk. """
	global _players
	return _players


# Private definitions
def _load_players(year, season):
	""" Load players from data directory. """
	global _players
	_players = []
	
	with cd('load_stats/data/player_data') as cm:
		for file in (file := os.listdir()):
			if (file.find(str(year)+'-'+season)) == 0:
				
				for row in (csv_reader := csv.DictReader(open(file, 'r'))):
					# change directories for access to data.json models
					os.chdir(cm.twoUpPath)

					stats = utils._get_model(row)

					_players.append({
						'ID': row['\ufeffID'],
						'First Name': row['First Name'],
						'Last Name': row['Last Name'],
						'Jersey': row['Jersey'],
						'Position': row['Position'],
						'Stats': stats
					})

	return _players






