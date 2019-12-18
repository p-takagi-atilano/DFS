from solver import solve_one



def get_lineuips(config):
	lineups = solve_one(config, verbose=True)

	return lineups

# configs are tuples: (num_lineups, overlap, to_max, name, player_csv, team_csv)

base = 'history/07-12-2018/'
preds = base + 'rotogrinders_predictions.csv'
teams = base + 'teams.csv'

config = (10, 7, 'Points', 'asdf', preds, teams)

get_lineuips(config)