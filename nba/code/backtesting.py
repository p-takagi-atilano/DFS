'''
General Backtesting Methods
'''

# TODO: change actual_csv var name to actual_json

import json
import multiprocessing

import pandas as pd

from solver import solve, solve_one
from filters import g_and_center, f_and_center, double_g, lim_teams, pg_and_c

train = ['p1_name', 'p1_sal', 'p1_team', 'p1_pg', 'p1_sg', 'p1_sf', 'p1_pf', 'p1_c', 'p1_opp', 'p1_pts', 'p1_ceil', 'p1_floor', 'p2_name', 'p2_sal', 'p2_team', 'p2_pg', 'p2_sg', 'p2_sf', 'p2_pf', 'p2_c', 'p2_opp', 'p2_pts', 'p2_ceil', 'p2_floor', 'p3_name', 'p3_sal', 'p3_team', 'p3_pg', 'p3_sg', 'p3_sf', 'p3_pf', 'p3_c', 'p3_opp', 'p3_pts', 'p3_ceil', 'p3_floor', 'p4_name', 'p4_sal', 'p4_team', 'p4_pg', 'p4_sg', 'p4_sf', 'p4_pf', 'p4_c', 'p4_opp', 'p4_pts', 'p4_ceil', 'p4_floor', 'p5_name', 'p5_sal', 'p5_team', 'p5_pg', 'p5_sg', 'p5_sf', 'p5_pf', 'p5_c', 'p5_opp', 'p5_pts', 'p5_ceil', 'p5_floor', 'p6_name', 'p6_sal', 'p6_team', 'p6_pg', 'p6_sg', 'p6_sf', 'p6_pf', 'p6_c', 'p6_opp', 'p6_pts', 'p6_ceil', 'p6_floor', 'p7_name', 'p7_sal', 'p7_team', 'p7_pg', 'p7_sg', 'p7_sf', 'p7_pf', 'p7_c', 'p7_opp', 'p7_pts', 'p7_ceil', 'p7_floor', 'p8_name', 'p8_sal', 'p8_team', 'p8_pg', 'p8_sg', 'p8_sf', 'p8_pf', 'p8_c', 'p8_opp', 'p8_pts', 'p8_ceil', 'p8_floor', 'meta', 'y']
test = ['p1_name', 'p1_sal', 'p1_team', 'p1_pg', 'p1_sg', 'p1_sf', 'p1_pf', 'p1_c', 'p1_opp', 'p1_pts', 'p1_ceil', 'p1_floor', 'p2_name', 'p2_sal', 'p2_team', 'p2_pg', 'p2_sg', 'p2_sf', 'p2_pf', 'p2_c', 'p2_opp', 'p2_pts', 'p2_ceil', 'p2_floor', 'p3_name', 'p3_sal', 'p3_team', 'p3_pg', 'p3_sg', 'p3_sf', 'p3_pf', 'p3_c', 'p3_opp', 'p3_pts', 'p3_ceil', 'p3_floor', 'p4_name', 'p4_sal', 'p4_team', 'p4_pg', 'p4_sg', 'p4_sf', 'p4_pf', 'p4_c', 'p4_opp', 'p4_pts', 'p4_ceil', 'p4_floor', 'p5_name', 'p5_sal', 'p5_team', 'p5_pg', 'p5_sg', 'p5_sf', 'p5_pf', 'p5_c', 'p5_opp', 'p5_pts', 'p5_ceil', 'p5_floor', 'p6_name', 'p6_sal', 'p6_team', 'p6_pg', 'p6_sg', 'p6_sf', 'p6_pf', 'p6_c', 'p6_opp', 'p6_pts', 'p6_ceil', 'p6_floor', 'p7_name', 'p7_sal', 'p7_team', 'p7_pg', 'p7_sg', 'p7_sf', 'p7_pf', 'p7_c', 'p7_opp', 'p7_pts', 'p7_ceil', 'p7_floor', 'p8_name', 'p8_sal', 'p8_team', 'p8_pg', 'p8_sg', 'p8_sf', 'p8_pf', 'p8_c', 'p8_opp', 'p8_pts', 'p8_ceil', 'p8_floor', 'meta']

teams = {'MIL':  0,
		 'NY':   1,
		 'NYK':  1, #
		 'OKC':  2,
		 'HOU':  3,
		 'PHI':  4,
		 'BOS':  5,
		 'LAL':  6,
		 'GS':   7,
		 'GSW':  7, #
		 'POR':  8,
		 'UTA':  9,
		 'MEM': 10,
		 'CHI': 11,
		 'CLE': 12,
		 'WAS': 13,
		 'IND': 14,
		 'MIA': 15,
		 'ORL': 16,
		 'DAL': 17,
		 'PHO': 18,
		 'BKN': 19,
		 'LAC': 20,
		 'CHA': 21,
		 'NO':  22,
		 'NOP': 22, #
		 'ATL': 23,
		 'DET': 24,
		 'MIN': 25,
		 'SAC': 26,
		 'DEN': 27,
		 'SA':  28,
		 'SAS': 28, #
		 'TOR': 29}

# returns an array for every actual lineup score for every config
# configs are tuples: (num_lineups, overlap, to_max, name, player_csv, team_csv, actual_csv)
def backtest_some(configs, player_csv, team_csv, actual_csv):
	with open(actual_csv, 'r') as f:
		actuals = json.loads(f.read())['fpts']

	sols = solve(configs, player_csv, team_csv)

	scores = []
	for sol in sols:	# one sol per config
		score = []

		for lineup in sol:	# every solution lineup
			score.append(sum([actuals[player] for player in lineup if player in actuals]))

		scores.append(score)
	
	df = pd.DataFrame()
	for i in range(len(configs)):
		df[configs[i][3]] = pd.Series(scores[i])
	return df

# configs are tuples: (num_lineups, overlap, to_max, name, player_csv, team_csv, actual_csv)
def backtest_fast(configs, fltr=None, ml=False):
	scores_list = [None] * len(configs)
	processes = []
	scores_list = []
	for i in range(len(configs)):
		scores = multiprocessing.Array('d', configs[i][0])
		scores_list.append(scores)
		processes.append(multiprocessing.Process(target=backtest_fast_helper, 
			args=(configs[i], scores, fltr, i, ml)))

	for process in processes:
		process.start()

	for process in processes:
		process.join()

	df = pd.DataFrame()
	for i in range(len(scores_list)):
		df[configs[i][3]] = pd.Series(scores_list[i][:])
	return df



def backtest_fast_helper(config, scores, fltr, i, ml):
	tup = solve_one(config)
	lineups = tup[0]
	path = 'train_ml/{}.csv'
	
	if fltr is None:
		df = pd.DataFrame(columns=train)
	else:
		df = pd.DataFrame(columns=test)
	
	with open(config[6], 'r') as f:
		actuals = json.loads(f.read())['fpts']

	# train ml stuff
	if ml:
		k = 0
		for l in tup[1]:
			row = []
			scr = 0
			for _,p in l.iterrows():
				row.append(p['Name'])
				row.append(p['Salary'])
				row.append(p['Team'])
				row.append(p['PG'])
				row.append(p['SG'])
				row.append(p['SF'])
				row.append(p['PF'])
				row.append(p['C'])
				row.append(p['Opponent'])
				row.append(p['Points'])
				row.append(p['Ceiling'])
				row.append(p['Floor'])
				if p['Name'] in actuals:
					scr += actuals[p['Name']]
			#print('{};{}'.format(row, scr))
			row.append(config[3])
		
			if fltr is None:
				with open(config[4].replace('rotogrinders_predictions.csv', 'cash_stats.json')) as f:
					js = json.loads(f.read())
				if 'gpp' in js[config[3].split(':')[1].replace('teams_', '').replace('.csv', '')]:
					line = js[config[3].split(':')[1].replace('teams_', '').replace('.csv', '')]['gpp']
					if scr > line*1.05:
						row.append(1)
					else:
						row.append(0)
					
					df.loc[k] = row
					k += 1
			else:
				with open(config[4].replace('rotogrinders_predictions.csv', 'cash_stats.json')) as f:
					js = json.loads(f.read())
				if 'gpp' in js[config[3].split(':')[1].replace('teams_', '').replace('.csv', '')]:
					df.loc[k] = row
					k += 1

		df = df.replace({'p1_team': teams, 'p1_opp': teams,
						 'p2_team': teams, 'p2_opp': teams,
						 'p3_team': teams, 'p3_opp': teams,
						 'p4_team': teams, 'p4_opp': teams,
						 'p5_team': teams, 'p5_opp': teams,
						 'p6_team': teams, 'p6_opp': teams,
						 'p7_team': teams, 'p7_opp': teams,
						 'p8_team': teams, 'p8_opp': teams})
		if fltr is not None:
			df_temp = df[df.columns.difference(['p1_name', 'p2_name', 'p3_name', 'p4_name', 'p5_name', 'p6_name', 'p7_name', 'p8_name', 'meta'])]
			df = df.assign(y=pd.Series(fltr.predict(df_temp)).values)
		df.to_csv(path.format(i))
		

	# normal stuff
	'''
	for i in range(len(lineups)):
		for player in lineups[i]:
			if player not in actuals:
				print('{}: {}'.format(config[3], player))
		scores[i] = sum([actuals[player] for player in lineups[i] if player in actuals])
	'''

