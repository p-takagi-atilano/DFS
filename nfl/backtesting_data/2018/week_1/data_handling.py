import pandas as pd

# conversion from draftkings team names to rotogrinders team names
team_change = {}

# returns teams dataframe
def get_teams(team_csv):
	df = pd.read_csv(team_csv)
	df = df.replace({'Team': team_change})
	return df

# returns players dataframe, refactored to fit CSP formulations
def get_players(player_csv, teams):
	data pd.read_csv(player_csv, header=None)

	players = pd.DataFrame({'Name' : data[data.columns[0]],
							'Salary' : data[data.columns[1]],
							'Team' : data[data.columns[2]],
							'QB' : 0,
							'RB' : 0,
							'WR' : 0,
							'TE' : 0,
							'DST' : 0,
							'Opponent' : data[data.columns[4]],
							'Points' : data[data.columns[7]],
							'Ceiling' : data[data.columns[5]],
							'Floor' : data[data.columns[6]],})

	for i, p in data.iterrows():
		if 'QB' in p[3]:
			players.at[i, 'QB'] = 1
		if 'RB' in p[3]:
			players.at[i, 'RB'] = 1
		if 'WR' in p[3]:
			players.at[i, 'WR'] = 1
		if 'TE' in p[3]:
			players.at[i, 'TE'] = 1
		if 'DST' in p[3]:
			players.at[i, 'DST'] = 1

	# remove players on invalid teams
	drops = []
	for i, p in players[::-1].iterrows():
		if (teams['Team'].str.contains(p['Team']).sum() == 0):
			drops.append(i)

	for i in drops:
		players.drop(players.index[i], inplace=True)
	players.index = [i for i in range(players.count()[0])]
	
	return players
