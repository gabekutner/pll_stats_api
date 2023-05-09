# teams.py

import os
import csv
import json

from . import utils


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

	path = utils.find_path(root=utils.BASE_DIR, dir='team_data')
	
	with utils.cd(path) as cm: 
		for file in (file := os.listdir()):
			if (file.find(str(year)+'-t')) == 0:
				
				for row in (csv_reader := csv.DictReader(open(file, 'r'))):

					_teams.append(row)

	return _teams