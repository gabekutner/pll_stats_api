# datastorage.py
#
# Our data is stored in 2 private globals 
# 
#   'players'
#   
#       The list of players. Each player in this list is a
#       {id, first_name, last_name, jersey, position, stats} dictionary where
#       stats is a nested dictionary containing the stats for the player.
#
#   'teams'
# 
#       The list of teams. Each team in this list is a       
#       {team_name, scores, stats} dictionary where scores is a string
#       representing the total goals scored and stats is a nested 
#       dictionary containing the rest of the teams stats. 

import csv
import os.path
import json


class cd:
	""" Context manager for changing the working directory. """

	# define newPath for use in __enter__ and __exit__ methods
	def __init__(self, newPath):
		# expanduser changes ~/file.txt -> /home/files/file.txt
		self.newPath = os.path.expanduser(newPath)

	def __enter__(self):
		# get current directory
		self.savedPath = os.getcwd()
		# change working directory
		os.chdir(self.newPath)
		return self

	# etype, value, traceback for throwing exceptions
	def __exit__(self, etype, value, traceback):
		# change working directory back to original path
		os.chdir(self.savedPath)

#############################################################################
#
# Public definitions:

def init(year, season):
    """Initialize the datastorage module.
    """
    _load_players(year, season)


def players():
	""" Return a dictionary of players

		Each item in the returned list will be a 
		{id, first_name, last_name, jersey, position, stats}
		dictionary.
	"""
	global _players
	return _players


def teams():
	""" Return a dict of teams

		Each item in the returned list will be a 
		{team_name, scores, stats} dictionary.
	"""
	# global _teams
	# return _teams
	pass

#############################################################################
#
#Private definitions:

# Load list of players from .csv depending on year and season
# and put into list
def _load_players(year, season):
	""" Load the list of players from disk """
	global _players
	p = []

	# Folder holding .csv stat files must be named 'stats'
	with cd('stats') as cm:

		# find .csv filename 
		# .csv name convention : [year]-[season]-[player or team].csv 
		# ex. 2022-post-p.csv
		files = os.listdir()
		for file in files:
			# Ex. year -> 2022, season -> regular / post
			if (file.find(str(year)+'-'+season)) == 0:
				x = file

		# get list of players 
		f = csv.DictReader(open(x, 'r'))
		for row in f:

			os.chdir(cm.savedPath)

			stats = _get_model(row)

			p.append({
				'ID': row['\ufeffID'],
				'First Name': row['First Name'],
				'Last Name': row['Last Name'],
				'Jersey': row['Jersey'],
				'Position': row['Position'],
				'Stats': stats
			})

	_players = p
	return _players


def _return_column_values(row, c, specStr="", specInt=0):
	""" Given the row and a column name: c and an optional parameter 
		for specifying parameters return str value of stat
	"""
	_stat = row[c]
	return _stat


def _get_model(row):
	""" Returns JSON model for _load_players() 
	"""

	stat_val = _return_column_values(row, 'Position')

	f = open('data.json', 'r')
	data = json.load(f)

	model = data[row['Position']]

	for i in model:
		data[row['Position']][i] = row[i]

	return model
	

#############################################################################
#
# Testing

if __name__ == '__main__':
	pass
	# init(2022, 'regular')
	# for player in players():
	# 	print(player['Position'])

	
	# f = csv.DictReader(open('stats/2022-regular-p.csv', 'r'))
	# for row in f:
	

	# 	f = open('data.json', 'r')
	# 	data = json.load(f)

	# 	model = data[row['Position']]
		
	# 	for i in model:
	# 		data[row['Position']][i] = row[i]


	# 	return model

	# with open('data.json', 'w') as output:
	# 	json.dump(data, output)