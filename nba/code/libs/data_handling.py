
import pandas as pd

# conversion from draftkings team names to rotogrinders team names
team_change = {'NY': 'NYK', 'GS': 'GSW', 'NO': 'NOP', 'SA': 'SAS'}

# returns teams dataframes
def get_teams(team_csv):
	df = pd.read_csv(team_csv)
	df = df.replace({'Team': team_change})
	return df

# returns players dataframe, refactored to fit CSP formulations
def get_players(player_csv, teams):
	data = pd.read_csv(player_csv, header=None)
	
	players = pd.DataFrame({'Name' : data[data.columns[0]],
							'Salary' : data[data.columns[1]],
							'Team' : data[data.columns[2]],
							'PG' : 0,
							'SG' : 0,
							'SF' : 0,
							'PF' : 0,
							'C' : 0,
							'Opponent' : data[data.columns[4]],
							'Points' : data[data.columns[7]],
							'Ceiling' : data[data.columns[5]],
							'Floor' : data[data.columns[6]],})

	for i, p in data.iterrows():
		if 'PG' in p[3]:
			players.at[i, 'PG'] = 1
		if 'SG' in p[3]:
			players.at[i, 'SG'] = 1
		if 'SF' in p[3]:
			players.at[i, 'SF'] = 1
		if 'PF' in p[3]:
			players.at[i, 'PF'] = 1
		if 'C' in p[3]:
			players.at[i, 'C'] = 1
	
	# remove players on invalid teams
	drops = []
	for i, p in players[::-1].iterrows():
		if (teams['Team'].str.contains(p['Team']).sum() == 0):
			drops.append(i)

	for i in drops:
		players.drop(players.index[i], inplace=True)
	players.index = [i for i in range(players.count()[0])]
	
	return players


# returns solution lineup
def get_solution_lineup(model, players, verbose):
	lineup = []
	players['is_drafted'] = 0

	for var in model.variables():
		if var.varValue == 1:
			lineup.append(var)
		players.iloc[int(var.name[1:]),12] = var.varValue

	my_team = players[players["is_drafted"] == 1.0]

	if verbose:
		print(my_team)
		print("Salary: {}".format(my_team["Salary"].sum()))
		print("Points: {}".format(my_team["Points"].sum().round(1)))

	return my_team, lineup
