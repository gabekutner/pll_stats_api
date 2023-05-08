# utils.py

import json
import os

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