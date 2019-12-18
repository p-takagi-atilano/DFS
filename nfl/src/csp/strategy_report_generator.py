
import json
import pandas as pd

from config import Config
from data_parser import DataParser
from filters import QB_WR1_Stack
from solver import Solver


class StrategyReportGenerator:
	def __init__(self, name, configs, configs_json_filename=None):
		self.name = name
		#self.configs = load_configs(configs_json_filename)
		self.configs = configs

	def load_configs(self, configs_json):
		pass

	def generate_report(self):
		data = {
			'Avg Cash': 0,
			'Avg GPP': {
				'1.3': 0,
				'1.2': 0,
				'1.1': 0,
				'1.0': 0
			},
			'Avg 150': {
				'1.3': 0,
				'1.2': 0,
				'1.1': 0,
				'1.0': 0
			},
			'Avg 20': {
				'1.3': 0,
				'1.2': 0,
				'1.1': 0,
				'1.0': 0
			}
		}

		for config in self.configs:
			solver = Solver(config)
			solver.generate_lineups()
			new_data = solver.get_lineup_data()
			for k in data:
				if k == 'Avg Cash':
					data[k] += new_data[k]
				else:
					for j in data[k]:
						data[k][j] += new_data[k][j]

		print('{}: {} lineups'.format(self.name, self.configs[0].num_lineups*len(self.configs)))
		for k in data:
			if k == 'Avg Cash':
				print('Avg Cash: {}'.format(data[k]))
			else:
				for j in data[k]:
					print('{} {}: {}'.format(k, j, data[k][j]))
		print()


'''
num_lineups = 50
base = '/Users/Paolo/Desktop/employment/dfs/nfl/backtesting_data/'
team_csv = 'teams.csv'
player_csv = 'rotogrinders_predictions.csv'
backtest = False
#config1 = Config(num_lineups, overlap, to_max, '2018', 'week_1', backtest)
'''
'''
configs = []
configs.append(Config(num_lineups, 8, 'Floor', '2018', 'week_2', backtest, QB_WR1_Stack()))
s1 = StrategyReportGenerator('8Floor', configs)
s1.generate_report()
'''
'''
configs = []
configs.append(Config(num_lineups, 8, 'Ceiling', '2018', 'week_2', backtest, None))
s1 = StrategyReportGenerator('8Ceil', configs)
s1.generate_report()
'''

'''

configs = []
configs.append(Config(num_lineups, 8, 'Ceiling', '2018', 'week_2', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 8, 'Ceiling', '2018', 'week_3', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 8, 'Ceiling', '2018', 'week_4', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 8, 'Ceiling', '2018', 'week_5', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 8, 'Ceiling', '2018', 'week_6', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 8, 'Ceiling', '2018', 'week_7', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 8, 'Ceiling', '2018', 'week_8', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 8, 'Ceiling', '2018', 'week_9', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 8, 'Ceiling', '2018', 'week_10', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 8, 'Ceiling', '2018', 'week_11', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 8, 'Ceiling', '2018', 'week_12', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 8, 'Ceiling', '2018', 'week_13', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 8, 'Ceiling', '2018', 'week_14', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 8, 'Ceiling', '2018', 'week_15', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 8, 'Ceiling', '2018', 'week_16', backtest, QB_WR1_Stack()))
s1 = StrategyReportGenerator('8Ceil', configs)
s1.generate_report()

configs = []
configs.append(Config(num_lineups, 8, 'Points', '2018', 'week_2', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 8, 'Points', '2018', 'week_3', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 8, 'Points', '2018', 'week_4', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 8, 'Points', '2018', 'week_5', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 8, 'Points', '2018', 'week_6', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 8, 'Points', '2018', 'week_7', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 8, 'Points', '2018', 'week_8', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 8, 'Points', '2018', 'week_9', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 8, 'Points', '2018', 'week_10', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 8, 'Points', '2018', 'week_11', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 8, 'Points', '2018', 'week_12', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 8, 'Points', '2018', 'week_13', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 8, 'Points', '2018', 'week_14', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 8, 'Points', '2018', 'week_15', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 8, 'Points', '2018', 'week_16', backtest, QB_WR1_Stack()))
s2 = StrategyReportGenerator('8Points', configs)
s2.generate_report()

configs = []
configs.append(Config(num_lineups, 8, 'Floor', '2018', 'week_2', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 8, 'Floor', '2018', 'week_3', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 8, 'Floor', '2018', 'week_4', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 8, 'Floor', '2018', 'week_5', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 8, 'Floor', '2018', 'week_6', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 8, 'Floor', '2018', 'week_7', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 8, 'Floor', '2018', 'week_8', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 8, 'Floor', '2018', 'week_9', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 8, 'Floor', '2018', 'week_10', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 8, 'Floor', '2018', 'week_11', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 8, 'Floor', '2018', 'week_12', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 8, 'Floor', '2018', 'week_13', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 8, 'Floor', '2018', 'week_14', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 8, 'Floor', '2018', 'week_15', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 8, 'Floor', '2018', 'week_16', backtest, QB_WR1_Stack()))
s3 = StrategyReportGenerator('8Floor', configs)
s3.generate_report()

configs = []
configs.append(Config(num_lineups, 7, 'Ceiling', '2018', 'week_2', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 7, 'Ceiling', '2018', 'week_3', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 7, 'Ceiling', '2018', 'week_4', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 7, 'Ceiling', '2018', 'week_5', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 7, 'Ceiling', '2018', 'week_6', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 7, 'Ceiling', '2018', 'week_7', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 7, 'Ceiling', '2018', 'week_8', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 7, 'Ceiling', '2018', 'week_9', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 7, 'Ceiling', '2018', 'week_10', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 7, 'Ceiling', '2018', 'week_11', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 7, 'Ceiling', '2018', 'week_12', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 7, 'Ceiling', '2018', 'week_13', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 7, 'Ceiling', '2018', 'week_14', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 7, 'Ceiling', '2018', 'week_15', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 7, 'Ceiling', '2018', 'week_16', backtest, QB_WR1_Stack()))
s1 = StrategyReportGenerator('7Ceil', configs)
s1.generate_report()

configs = []
configs.append(Config(num_lineups, 7, 'Points', '2018', 'week_2', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 7, 'Points', '2018', 'week_3', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 7, 'Points', '2018', 'week_4', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 7, 'Points', '2018', 'week_5', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 7, 'Points', '2018', 'week_6', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 7, 'Points', '2018', 'week_7', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 7, 'Points', '2018', 'week_8', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 7, 'Points', '2018', 'week_9', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 7, 'Points', '2018', 'week_10', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 7, 'Points', '2018', 'week_11', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 7, 'Points', '2018', 'week_12', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 7, 'Points', '2018', 'week_13', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 7, 'Points', '2018', 'week_14', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 7, 'Points', '2018', 'week_15', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 7, 'Points', '2018', 'week_16', backtest, QB_WR1_Stack()))
s2 = StrategyReportGenerator('7Points', configs)
s2.generate_report()

configs = []
configs.append(Config(num_lineups, 7, 'Floor', '2018', 'week_2', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 7, 'Floor', '2018', 'week_3', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 7, 'Floor', '2018', 'week_4', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 7, 'Floor', '2018', 'week_5', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 7, 'Floor', '2018', 'week_6', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 7, 'Floor', '2018', 'week_7', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 7, 'Floor', '2018', 'week_8', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 7, 'Floor', '2018', 'week_9', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 7, 'Floor', '2018', 'week_10', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 7, 'Floor', '2018', 'week_11', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 7, 'Floor', '2018', 'week_12', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 7, 'Floor', '2018', 'week_13', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 7, 'Floor', '2018', 'week_14', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 7, 'Floor', '2018', 'week_15', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 7, 'Floor', '2018', 'week_16', backtest, QB_WR1_Stack()))
s3 = StrategyReportGenerator('7Floor', configs)
s3.generate_report()

configs = []
configs.append(Config(num_lineups, 6, 'Ceiling', '2018', 'week_2', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 6, 'Ceiling', '2018', 'week_3', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 6, 'Ceiling', '2018', 'week_4', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 6, 'Ceiling', '2018', 'week_5', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 6, 'Ceiling', '2018', 'week_6', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 6, 'Ceiling', '2018', 'week_7', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 6, 'Ceiling', '2018', 'week_8', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 6, 'Ceiling', '2018', 'week_9', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 6, 'Ceiling', '2018', 'week_10', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 6, 'Ceiling', '2018', 'week_11', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 6, 'Ceiling', '2018', 'week_12', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 6, 'Ceiling', '2018', 'week_13', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 6, 'Ceiling', '2018', 'week_14', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 6, 'Ceiling', '2018', 'week_15', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 6, 'Ceiling', '2018', 'week_16', backtest, QB_WR1_Stack()))
s1 = StrategyReportGenerator('6Ceil', configs)
s1.generate_report()

configs = []
configs.append(Config(num_lineups, 6, 'Points', '2018', 'week_2', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 6, 'Points', '2018', 'week_3', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 6, 'Points', '2018', 'week_4', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 6, 'Points', '2018', 'week_5', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 6, 'Points', '2018', 'week_6', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 6, 'Points', '2018', 'week_7', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 6, 'Points', '2018', 'week_8', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 6, 'Points', '2018', 'week_9', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 6, 'Points', '2018', 'week_10', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 6, 'Points', '2018', 'week_11', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 6, 'Points', '2018', 'week_12', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 6, 'Points', '2018', 'week_13', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 6, 'Points', '2018', 'week_14', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 6, 'Points', '2018', 'week_15', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 6, 'Points', '2018', 'week_16', backtest, QB_WR1_Stack()))
s2 = StrategyReportGenerator('6Points', configs)
s2.generate_report()

configs = []
configs.append(Config(num_lineups, 6, 'Floor', '2018', 'week_2', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 6, 'Floor', '2018', 'week_3', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 6, 'Floor', '2018', 'week_4', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 6, 'Floor', '2018', 'week_5', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 6, 'Floor', '2018', 'week_6', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 6, 'Floor', '2018', 'week_7', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 6, 'Floor', '2018', 'week_8', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 6, 'Floor', '2018', 'week_9', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 6, 'Floor', '2018', 'week_10', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 6, 'Floor', '2018', 'week_11', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 6, 'Floor', '2018', 'week_12', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 6, 'Floor', '2018', 'week_13', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 6, 'Floor', '2018', 'week_14', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 6, 'Floor', '2018', 'week_15', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 6, 'Floor', '2018', 'week_16', backtest, QB_WR1_Stack()))
s3 = StrategyReportGenerator('6Floor', configs)
s3.generate_report()

configs = []
configs.append(Config(num_lineups, 5, 'Ceiling', '2018', 'week_2', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 5, 'Ceiling', '2018', 'week_3', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 5, 'Ceiling', '2018', 'week_4', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 5, 'Ceiling', '2018', 'week_5', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 5, 'Ceiling', '2018', 'week_6', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 5, 'Ceiling', '2018', 'week_7', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 5, 'Ceiling', '2018', 'week_8', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 5, 'Ceiling', '2018', 'week_9', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 5, 'Ceiling', '2018', 'week_10', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 5, 'Ceiling', '2018', 'week_11', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 5, 'Ceiling', '2018', 'week_12', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 5, 'Ceiling', '2018', 'week_13', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 5, 'Ceiling', '2018', 'week_14', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 5, 'Ceiling', '2018', 'week_15', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 5, 'Ceiling', '2018', 'week_16', backtest, QB_WR1_Stack()))
s1 = StrategyReportGenerator('5Ceil', configs)
s1.generate_report()

configs = []
configs.append(Config(num_lineups, 5, 'Points', '2018', 'week_2', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 5, 'Points', '2018', 'week_3', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 5, 'Points', '2018', 'week_4', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 5, 'Points', '2018', 'week_5', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 5, 'Points', '2018', 'week_6', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 5, 'Points', '2018', 'week_7', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 5, 'Points', '2018', 'week_8', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 5, 'Points', '2018', 'week_9', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 5, 'Points', '2018', 'week_10', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 5, 'Points', '2018', 'week_11', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 5, 'Points', '2018', 'week_12', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 5, 'Points', '2018', 'week_13', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 5, 'Points', '2018', 'week_14', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 5, 'Points', '2018', 'week_15', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 5, 'Points', '2018', 'week_16', backtest, QB_WR1_Stack()))
s2 = StrategyReportGenerator('5Points', configs)
s2.generate_report()

configs = []
configs.append(Config(num_lineups, 5, 'Floor', '2018', 'week_2', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 5, 'Floor', '2018', 'week_3', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 5, 'Floor', '2018', 'week_4', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 5, 'Floor', '2018', 'week_5', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 5, 'Floor', '2018', 'week_6', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 5, 'Floor', '2018', 'week_7', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 5, 'Floor', '2018', 'week_8', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 5, 'Floor', '2018', 'week_9', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 5, 'Floor', '2018', 'week_10', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 5, 'Floor', '2018', 'week_11', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 5, 'Floor', '2018', 'week_12', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 5, 'Floor', '2018', 'week_13', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 5, 'Floor', '2018', 'week_14', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 5, 'Floor', '2018', 'week_15', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 5, 'Floor', '2018', 'week_16', backtest, QB_WR1_Stack()))
s3 = StrategyReportGenerator('5Floor', configs)
s3.generate_report()

configs = []
configs.append(Config(num_lineups, 4, 'Ceiling', '2018', 'week_2', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 4, 'Ceiling', '2018', 'week_3', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 4, 'Ceiling', '2018', 'week_4', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 4, 'Ceiling', '2018', 'week_5', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 4, 'Ceiling', '2018', 'week_6', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 4, 'Ceiling', '2018', 'week_7', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 4, 'Ceiling', '2018', 'week_8', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 4, 'Ceiling', '2018', 'week_9', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 4, 'Ceiling', '2018', 'week_10', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 4, 'Ceiling', '2018', 'week_11', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 4, 'Ceiling', '2018', 'week_12', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 4, 'Ceiling', '2018', 'week_13', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 4, 'Ceiling', '2018', 'week_14', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 4, 'Ceiling', '2018', 'week_15', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 4, 'Ceiling', '2018', 'week_16', backtest, QB_WR1_Stack()))
s1 = StrategyReportGenerator('4Ceil', configs)
s1.generate_report()

configs = []
configs.append(Config(num_lineups, 4, 'Points', '2018', 'week_2', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 4, 'Points', '2018', 'week_3', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 4, 'Points', '2018', 'week_4', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 4, 'Points', '2018', 'week_5', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 4, 'Points', '2018', 'week_6', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 4, 'Points', '2018', 'week_7', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 4, 'Points', '2018', 'week_8', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 4, 'Points', '2018', 'week_9', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 4, 'Points', '2018', 'week_10', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 4, 'Points', '2018', 'week_11', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 4, 'Points', '2018', 'week_12', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 4, 'Points', '2018', 'week_13', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 4, 'Points', '2018', 'week_14', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 4, 'Points', '2018', 'week_15', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 4, 'Points', '2018', 'week_16', backtest, QB_WR1_Stack()))
s2 = StrategyReportGenerator('4Points', configs)
s2.generate_report()

configs = []
configs.append(Config(num_lineups, 4, 'Floor', '2018', 'week_2', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 4, 'Floor', '2018', 'week_3', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 4, 'Floor', '2018', 'week_4', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 4, 'Floor', '2018', 'week_5', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 4, 'Floor', '2018', 'week_6', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 4, 'Floor', '2018', 'week_7', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 4, 'Floor', '2018', 'week_8', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 4, 'Floor', '2018', 'week_9', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 4, 'Floor', '2018', 'week_10', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 4, 'Floor', '2018', 'week_11', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 4, 'Floor', '2018', 'week_12', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 4, 'Floor', '2018', 'week_13', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 4, 'Floor', '2018', 'week_14', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 4, 'Floor', '2018', 'week_15', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 4, 'Floor', '2018', 'week_16', backtest, QB_WR1_Stack()))
s3 = StrategyReportGenerator('4Floor', configs)
s3.generate_report()

configs = []
configs.append(Config(num_lineups, 3, 'Ceiling', '2018', 'week_2', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 3, 'Ceiling', '2018', 'week_3', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 3, 'Ceiling', '2018', 'week_4', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 3, 'Ceiling', '2018', 'week_5', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 3, 'Ceiling', '2018', 'week_6', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 3, 'Ceiling', '2018', 'week_7', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 3, 'Ceiling', '2018', 'week_8', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 3, 'Ceiling', '2018', 'week_9', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 3, 'Ceiling', '2018', 'week_10', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 3, 'Ceiling', '2018', 'week_11', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 3, 'Ceiling', '2018', 'week_12', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 3, 'Ceiling', '2018', 'week_13', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 3, 'Ceiling', '2018', 'week_14', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 3, 'Ceiling', '2018', 'week_15', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 3, 'Ceiling', '2018', 'week_16', backtest, QB_WR1_Stack()))
s1 = StrategyReportGenerator('3Ceil', configs)
s1.generate_report()

configs = []
configs.append(Config(num_lineups, 3, 'Points', '2018', 'week_2', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 3, 'Points', '2018', 'week_3', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 3, 'Points', '2018', 'week_4', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 3, 'Points', '2018', 'week_5', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 3, 'Points', '2018', 'week_6', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 3, 'Points', '2018', 'week_7', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 3, 'Points', '2018', 'week_8', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 3, 'Points', '2018', 'week_9', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 3, 'Points', '2018', 'week_10', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 3, 'Points', '2018', 'week_11', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 3, 'Points', '2018', 'week_12', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 3, 'Points', '2018', 'week_13', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 3, 'Points', '2018', 'week_14', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 3, 'Points', '2018', 'week_15', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 3, 'Points', '2018', 'week_16', backtest, QB_WR1_Stack()))
s2 = StrategyReportGenerator('3Points', configs)
s2.generate_report()

configs = []
configs.append(Config(num_lineups, 3, 'Floor', '2018', 'week_2', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 3, 'Floor', '2018', 'week_3', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 3, 'Floor', '2018', 'week_4', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 3, 'Floor', '2018', 'week_5', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 3, 'Floor', '2018', 'week_6', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 3, 'Floor', '2018', 'week_7', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 3, 'Floor', '2018', 'week_8', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 3, 'Floor', '2018', 'week_9', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 3, 'Floor', '2018', 'week_10', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 3, 'Floor', '2018', 'week_11', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 3, 'Floor', '2018', 'week_12', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 3, 'Floor', '2018', 'week_13', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 3, 'Floor', '2018', 'week_14', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 3, 'Floor', '2018', 'week_15', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 3, 'Floor', '2018', 'week_16', backtest, QB_WR1_Stack()))
s3 = StrategyReportGenerator('3Floor', configs)
s3.generate_report()

configs = []
configs.append(Config(num_lineups, 2, 'Ceiling', '2018', 'week_2', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 2, 'Ceiling', '2018', 'week_3', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 2, 'Ceiling', '2018', 'week_4', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 2, 'Ceiling', '2018', 'week_5', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 2, 'Ceiling', '2018', 'week_6', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 2, 'Ceiling', '2018', 'week_7', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 2, 'Ceiling', '2018', 'week_8', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 2, 'Ceiling', '2018', 'week_9', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 2, 'Ceiling', '2018', 'week_10', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 2, 'Ceiling', '2018', 'week_11', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 2, 'Ceiling', '2018', 'week_12', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 2, 'Ceiling', '2018', 'week_13', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 2, 'Ceiling', '2018', 'week_14', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 2, 'Ceiling', '2018', 'week_15', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 2, 'Ceiling', '2018', 'week_16', backtest, QB_WR1_Stack()))
s1 = StrategyReportGenerator('2Ceil', configs)
s1.generate_report()

configs = []
configs.append(Config(num_lineups, 2, 'Points', '2018', 'week_2', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 2, 'Points', '2018', 'week_3', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 2, 'Points', '2018', 'week_4', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 2, 'Points', '2018', 'week_5', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 2, 'Points', '2018', 'week_6', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 2, 'Points', '2018', 'week_7', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 2, 'Points', '2018', 'week_8', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 2, 'Points', '2018', 'week_9', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 2, 'Points', '2018', 'week_10', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 2, 'Points', '2018', 'week_11', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 2, 'Points', '2018', 'week_12', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 2, 'Points', '2018', 'week_13', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 2, 'Points', '2018', 'week_14', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 2, 'Points', '2018', 'week_15', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 2, 'Points', '2018', 'week_16', backtest, QB_WR1_Stack()))
s2 = StrategyReportGenerator('2Points', configs)
s2.generate_report()

configs = []
configs.append(Config(num_lineups, 2, 'Floor', '2018', 'week_2', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 2, 'Floor', '2018', 'week_3', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 2, 'Floor', '2018', 'week_4', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 2, 'Floor', '2018', 'week_5', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 2, 'Floor', '2018', 'week_6', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 2, 'Floor', '2018', 'week_7', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 2, 'Floor', '2018', 'week_8', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 2, 'Floor', '2018', 'week_9', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 2, 'Floor', '2018', 'week_10', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 2, 'Floor', '2018', 'week_11', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 2, 'Floor', '2018', 'week_12', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 2, 'Floor', '2018', 'week_13', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 2, 'Floor', '2018', 'week_14', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 2, 'Floor', '2018', 'week_15', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 2, 'Floor', '2018', 'week_16', backtest, QB_WR1_Stack()))
s3 = StrategyReportGenerator('2Floor', configs)
s3.generate_report()

configs = []
configs.append(Config(num_lineups, 1, 'Ceiling', '2018', 'week_2', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 1, 'Ceiling', '2018', 'week_3', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 1, 'Ceiling', '2018', 'week_4', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 1, 'Ceiling', '2018', 'week_5', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 1, 'Ceiling', '2018', 'week_6', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 1, 'Ceiling', '2018', 'week_7', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 1, 'Ceiling', '2018', 'week_8', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 1, 'Ceiling', '2018', 'week_9', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 1, 'Ceiling', '2018', 'week_10', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 1, 'Ceiling', '2018', 'week_11', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 1, 'Ceiling', '2018', 'week_12', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 1, 'Ceiling', '2018', 'week_13', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 1, 'Ceiling', '2018', 'week_14', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 1, 'Ceiling', '2018', 'week_15', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 1, 'Ceiling', '2018', 'week_16', backtest, QB_WR1_Stack()))
s1 = StrategyReportGenerator('1Ceil', configs)
s1.generate_report()

configs = []
configs.append(Config(num_lineups, 1, 'Points', '2018', 'week_2', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 1, 'Points', '2018', 'week_3', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 1, 'Points', '2018', 'week_4', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 1, 'Points', '2018', 'week_5', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 1, 'Points', '2018', 'week_6', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 1, 'Points', '2018', 'week_7', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 1, 'Points', '2018', 'week_8', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 1, 'Points', '2018', 'week_9', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 1, 'Points', '2018', 'week_10', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 1, 'Points', '2018', 'week_11', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 1, 'Points', '2018', 'week_12', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 1, 'Points', '2018', 'week_13', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 1, 'Points', '2018', 'week_14', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 1, 'Points', '2018', 'week_15', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 1, 'Points', '2018', 'week_16', backtest, QB_WR1_Stack()))
s2 = StrategyReportGenerator('1Points', configs)
s2.generate_report()

configs = []
configs.append(Config(num_lineups, 1, 'Floor', '2018', 'week_2', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 1, 'Floor', '2018', 'week_3', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 1, 'Floor', '2018', 'week_4', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 1, 'Floor', '2018', 'week_5', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 1, 'Floor', '2018', 'week_6', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 1, 'Floor', '2018', 'week_7', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 1, 'Floor', '2018', 'week_8', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 1, 'Floor', '2018', 'week_9', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 1, 'Floor', '2018', 'week_10', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 1, 'Floor', '2018', 'week_11', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 1, 'Floor', '2018', 'week_12', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 1, 'Floor', '2018', 'week_13', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 1, 'Floor', '2018', 'week_14', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 1, 'Floor', '2018', 'week_15', backtest, QB_WR1_Stack()))
configs.append(Config(num_lineups, 1, 'Floor', '2018', 'week_16', backtest, QB_WR1_Stack()))
s3 = StrategyReportGenerator('1Floor', configs)
s3.generate_report()

'''