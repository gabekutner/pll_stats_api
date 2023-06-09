# teams.py

import os
import csv
import json

from .utils import cd, find_path, _get_model, BASE_DIR


# Public definitions
def init(year=2022):
	""" Initialize the teams module. """
	_load_teams(year)


def get_teams():
	""" Load teams from disk. """
	global _teams
	return _teams


def get_team(*,id):
	""" Load team from disk. """
	global _teams
	try:
		assert 0 <= id <= len(_teams)
	except AssertionError:
		return None

	return _teams[id-1]

# Private definitions
def _load_teams(year):
	""" Load the teams from the data directory. """
	global _teams
	_teams = []

	path = find_path(root=BASE_DIR, dir='team_data')
	
	with cd(path) as cm: 
		for file in (file := os.listdir()):
			if (file.find(str(year)+'-t')) == 0:
				
				for row in (csv_reader := csv.DictReader(open(file, 'r'))):
					_teams.append(row)

	return _teams