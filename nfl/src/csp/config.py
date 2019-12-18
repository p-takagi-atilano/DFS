BASE = '/Users/Paolo/Desktop/employment/dfs/nfl/backtesting_data'

# Configuration information for Solver classes
class Config:
	def __init__(self, num_lineups, overlap, to_max, year, week, backtest, fltr=None):
		self.num_lineups = num_lineups
		self.overlap = overlap
		self.to_max = to_max
		self.year = year
		self.week = week
		self.backtest = backtest
		self.filter = fltr

	def get_teams_csv_filename(self):
		return '{}/{}/{}/{}'.format(BASE, self.year, self.week, 'teams.csv')

	def get_rotogrinders_predictions_csv_filename(self):
		return '{}/{}/{}/{}'.format(BASE, self.year, self.week, 'rotogrinders_predictions.csv')

	def get_draftkings_actual_scores_json_filename(self):
		return '{}/{}/{}/{}'.format(BASE, self.year, self.week, 'draftkings_actual_scores.json')

	def get_draftkings_cash_lines_json_filename(self):
		return '{}/{}/{}/{}'.format(BASE, self.year, self.week, 'cash_lines.json')
