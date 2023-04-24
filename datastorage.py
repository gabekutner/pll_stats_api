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

# load list of players from .csv depending on year and season
# and put into dict
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
			p.append({
				'ID': row['\ufeffID'],
				'First Name': row['First Name'],
				'Last Name': row['Last Name'],
				'Jersey': row['Jersey'],
				'Position': row['Position'],
				'Stats': {
					'Games Played': row['Games Played'],
					'Points': row['Points'],
					'Total Goals': row['Total Goals'],
					'1pt Goals': row['1pt Goals'],
					'2pt Goals': row['2pt Goals'],
					'Scoring Points': row['Scoring Points'],
					'Assists': row['Assists'],
					'Shots': row['Shots'],
					'Shot Pct': row['Shot Pct'],
					'Shots On Goal': row['Shots On Goal'],
					'SOG Pct': row['SOG Pct'],
					'2pt Shots': row['2pt Shots'],
					'2pt Shot Pct': row['2pt Shot Pct'],
					'2pt Shots On Goal': row['2pt Shots On Goal'],
					'Groundballs': row['Groundballs'],
					'Turnovers': row['Turnovers'],
					'Caused Turnovers': row['Caused Turnovers'],
					'Faceoffs': row['Faceoffs'],
					'Faceoff Wins': row['Faceoff Wins'],
					'Faceoff Losses': row['Faceoff Losses'],
					'Faceoff Pct': row['Faceoff Pct'],
					'Saves': row['Saves'],
					'Save Pct': row['Save Pct'],
					'Scores Against': row['Scores Against'],
					'Scores Against Average': row['Scores Against Average'],
					'2pt Goals Against': row['2pt Goals Against'],
					'2pt GAA': row['2pt GAA'],
					'Time On Field': row['Time On Field'],
					'Total Penalties': row['Total Penalties'],
					'Penalty Minutes': row['Penalty Minutes'],
					'Power Play Goals': row['Power Play Goals'],
					'Power Play Shots': row['Power Play Shots'],
					'Short Handed Goals': row['Short Handed Goals'],
					'Short Handed Shots': row['Short Handed Shots'],
					'Short Handed Goals Against': row['Short Handed Goals Against'],
					'Power Play Goals Against': row['Power Play Goals Against']
				}
			})

	_players = p

#############################################################################
#
# Testing

if __name__ == '__main__':
	init(2022, 'regular')
	print(players())