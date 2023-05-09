# players.py

import os
import csv
import json
from fastapi import HTTPException

from .utils import cd, _get_model, find_path, BASE_DIR


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

	path = find_path(root=BASE_DIR, dir='player_data')
	
	with cd(path) as cm:
		for file in (files := os.listdir()):
			if (file.find(str(year)+'-'+season)) == 0:
				
				for row in (csv_reader := csv.DictReader(open(file, 'r'))):
					# change directories for access to data.json models
					os.chdir(cm.twoUpPath)

					stats = _get_model(row)

					_players.append({
						'ID': row['\ufeffID'],
						'First Name': row['First Name'],
						'Last Name': row['Last Name'],
						'Jersey': row['Jersey'],
						'Position': row['Position'],
						'Stats': stats
					})

	return _players