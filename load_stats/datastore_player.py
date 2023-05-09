# players.py

import os
import csv
import json

from . import utils


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

	path = utils.find_path(root=utils.BASE_DIR, dir='player_data')
	
	with utils.cd(path) as cm:
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
