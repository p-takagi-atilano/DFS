import json

import pandas as pd

# Parses and stores team and player DataFrames for Solver class
class DataParser:
	def __init__(self, config):
		self.team_change = self.load_team_change_json()
		self.player_change = self.load_player_change_json()
		self.config = config
		self.teams = self.get_teams()
		self.players = self.get_players()

	def load_team_change_json(self):
		with open('team_change.json') as f:
			js = json.loads(f.read())
		return js

	def load_player_change_json(self):
		with open('player_change.json') as f:
			js = json.loads(f.read())
		return js

	def get_teams(self):
		df = pd.read_csv(self.config.get_teams_csv_filename())
		df = df.replace({'Team': self.team_change})
		return df

	def get_players(self):
		data = pd.read_csv(self.config.get_rotogrinders_predictions_csv_filename())

		players = pd.DataFrame({'Name' : data[data.columns[1]],
								'Salary' : data[data.columns[2]],
								'Team' : data[data.columns[3]],
								'QB' : 0,
								'RB' : 0,
								'WR' : 0,
								'TE' : 0,
								'DST' : 0,
								'Opponent' : data[data.columns[5]],
								'Points' : data[data.columns[8]],
								'Ceiling' : data[data.columns[6]],
								'Floor' : data[data.columns[7]],})
		players = players.replace({'Name': self.player_change})

		for i, p in data.iterrows():
			if 'QB' in p[4]:
				players.at[i, 'QB'] = 1
			if 'RB' in p[4]:
				players.at[i, 'RB'] = 1
			if 'WR' in p[4]:
				players.at[i, 'WR'] = 1
			if 'TE' in p[4]:
				players.at[i, 'TE'] = 1
			if 'DST' in p[4]:
				players.at[i, 'DST'] = 1
			
		# remove players on invalid teams
		drops = []

		for i, p in players[::-1].iterrows():
			if (self.teams['Team'].str.contains(p['Team']).sum() == 0):
				drops.append(i)

		for i in drops:
			players.drop(players.index[i], inplace=True)
		players.index = [i for i in range(players.count()[0])]
	
		return players

'''
		def get_player_change(self):
			return self.player_change

		def set_player_change(self, player_change):
			self.player_change = player_change
			with open('player_change.json', 'w') as f:
				f.write(json.dumps(self.player_change))
'''

