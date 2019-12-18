import json

import pandas as pd

from statistics import mean

class Backtester:
	def __init__(self, config, dataParser, constrainedModel, lineups_override=None):
		self.config = config
		self.dataParser = dataParser
		self.constrainedModel = constrainedModel
		self.lineups_override = lineups_override

		self.actual_scores = self.load_actual_scores()
		self.cash_lines = self.load_cash_lines()

		self.lineup_scores = None

	def load_actual_scores(self):
		with open(self.config.get_draftkings_actual_scores_json_filename()) as f:
			js = json.loads(f.read())
		return js

	def generate_lineup_scores(self):
		l_scores = []
		with open('potential_player_name_errors.json') as f:
			err = set(json.loads(f.read()))

		lineups = None
		if self.lineups_override is not None:
			lineups = self.lineups_override
		else:
			lineups = self.constrainedModel.lineups

		for lineup in lineups:
			l_score = 0
			for i,p in lineup.iterrows():
				p_score = 0
				if p['Name'] not in self.actual_scores:
					err.add('{};{};{}'.format(p['Name'], self.config.year, self.config.week))
				else:
					p_score = self.actual_scores[p['Name']]
				l_score += p_score
			l_scores.append(l_score)
		self.lineup_scores = l_scores

		#print('Players: {}'.format(len(err)))
		with open('potential_player_name_errors.json', 'w') as f:
			f.write(json.dumps(list(err)))

	def load_cash_lines(self):
		with open(self.config.get_draftkings_cash_lines_json_filename()) as f:
			js = json.loads(f.read())
		return js

	def calc_projection_error(self):
		pass

	def lineup_report(self):
		if self.lineup_scores is None:
			self.generate_lineup_scores()

		avg_cash_count = 0
		avg_gpp_count_13 = 0
		avg_gpp_count_12 = 0
		avg_gpp_count_11 = 0
		avg_gpp_count_10 = 0
		avg_150_count_13 = 0
		avg_150_count_12 = 0
		avg_150_count_11 = 0
		avg_150_count_10 = 0
		avg_20_count_13 = 0
		avg_20_count_12 = 0
		avg_20_count_11 = 0
		avg_20_count_10 = 0
		for lineup_score in self.lineup_scores:
			if lineup_score >= self.cash_lines["Avg Cash"]:
				avg_cash_count += 1

			if lineup_score >= self.cash_lines["Avg GPP"]*1.3:
				avg_gpp_count_13 += 1
			if lineup_score >= self.cash_lines["Avg GPP"]*1.2:
				avg_gpp_count_12 += 1
			if lineup_score >= self.cash_lines["Avg GPP"]*1.1:
				avg_gpp_count_11 += 1
			if lineup_score >= self.cash_lines["Avg GPP"]:
				avg_gpp_count_10 += 1

			if lineup_score >= mean(self.cash_lines["150"])*1.3:
				avg_150_count_13 += 1
			if lineup_score >= mean(self.cash_lines["150"])*1.2:
				avg_150_count_12 += 1
			if lineup_score >= mean(self.cash_lines["150"])*1.1:
				avg_150_count_11 += 1
			if lineup_score >= mean(self.cash_lines["150"]):
				avg_150_count_10 += 1
			if len(self.cash_lines["20"]) > 0:
				if lineup_score >= mean(self.cash_lines["20"])*1.3:
					avg_20_count_13 += 1
				if lineup_score >= mean(self.cash_lines["20"])*1.2:
					avg_20_count_12 += 1
				if lineup_score >= mean(self.cash_lines["20"])*1.1:
					avg_20_count_11 += 1
				if lineup_score >= mean(self.cash_lines["20"]):
					avg_20_count_10 += 1


		#print('{} {}: {} lineups'.format(self.config.year, self.config.week, len(self.lineup_scores)))
		#print('Avg Cash: {}'.format(avg_cash_count))
		#print('Avg GPP: 1.3: {}; 1.2: {}; 1.1: {}; 1.0: {}'.format(avg_gpp_count_13, avg_gpp_count_12, avg_gpp_count_11, avg_gpp_count_10))
		#print('Avg 150: 1.3: {}; 1.2: {}; 1.1: {}; 1.0: {}'.format(avg_150_count_13, avg_150_count_12, avg_150_count_11, avg_150_count_10))
		#print('Avg 20: 1.3: {}; 1.2: {}; 1.1: {}; 1.0: {}\n'.format(avg_20_count_13, avg_20_count_12, avg_20_count_11, avg_20_count_10))

		return {
			'Avg Cash': avg_cash_count,
			'Avg GPP': {
				'1.3': avg_gpp_count_13,
				'1.2': avg_gpp_count_12,
				'1.1': avg_gpp_count_11,
				'1.0': avg_gpp_count_10
			},
			'Avg 150': {
				'1.3': avg_150_count_13,
				'1.2': avg_150_count_12,
				'1.1': avg_150_count_11,
				'1.0': avg_150_count_10
			},
			'Avg 20': {
				'1.3': avg_20_count_13,
				'1.2': avg_20_count_12,
				'1.1': avg_20_count_11,
				'1.0': avg_20_count_10
			}
		}

		


		
