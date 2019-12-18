import os

import pandas as pd

newcols = ['p1_sal', 'p1_team', 'p1_pg', 'p1_sg', 'p1_sf', 'p1_pf', 'p1_c', 'p1_opp', 'p1_pts', 'p1_ceil', 'p1_floor', 'p2_sal', 'p2_team', 'p2_pg', 'p2_sg', 'p2_sf', 'p2_pf', 'p2_c', 'p2_opp', 'p2_pts', 'p2_ceil', 'p2_floor', 'p3_sal', 'p3_team', 'p3_pg', 'p3_sg', 'p3_sf', 'p3_pf', 'p3_c', 'p3_opp', 'p3_pts', 'p3_ceil', 'p3_floor', 'p4_sal', 'p4_team', 'p4_pg', 'p4_sg', 'p4_sf', 'p4_pf', 'p4_c', 'p4_opp', 'p4_pts', 'p4_ceil', 'p4_floor', 'p5_sal', 'p5_team', 'p5_pg', 'p5_sg', 'p5_sf', 'p5_pf', 'p5_c', 'p5_opp', 'p5_pts', 'p5_ceil', 'p5_floor', 'p6_sal', 'p6_team', 'p6_pg', 'p6_sg', 'p6_sf', 'p6_pf', 'p6_c', 'p6_opp', 'p6_pts', 'p6_ceil', 'p6_floor', 'p7_sal', 'p7_team', 'p7_pg', 'p7_sg', 'p7_sf', 'p7_pf', 'p7_c', 'p7_opp', 'p7_pts', 'p7_ceil', 'p7_floor', 'p8_sal', 'p8_team', 'p8_pg', 'p8_sg', 'p8_sf', 'p8_pf', 'p8_c', 'p8_opp', 'p8_pts', 'p8_ceil', 'p8_floor', 'y']

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

def make_one(fname):		
	df = pd.DataFrame(columns = newcols)
	#print(df)
	for i in range(100):
		filename = 'train_ml/{}.csv'.format(i)
		if os.path.isfile(filename):
			dftemp = pd.read_csv(filename, index_col='Unnamed: 0')
			'''
			dftemp = dftemp.replace({'p1_team': teams, 'p1_opp': teams,
									 'p2_team': teams, 'p2_opp': teams,
									 'p3_team': teams, 'p3_opp': teams,
									 'p4_team': teams, 'p4_opp': teams,
									 'p5_team': teams, 'p5_opp': teams,
									 'p6_team': teams, 'p6_opp': teams,
									 'p7_team': teams, 'p7_opp': teams,
									 'p8_team': teams, 'p8_opp': teams})
			'''
			df = df.append(dftemp, ignore_index=True, sort=False)
			os.remove(filename)

	df = df.sample(frac=1)
	#print(df)
	df.to_csv('train_ml/{}.csv'.format(fname))
	return df
