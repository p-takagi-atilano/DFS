import json
import multiprocessing
import os

import pandas as pd

from solver import solve_one

# 14+ teams
tbigs = [('02-11-2018', 'teams_700.csv'),
		 ('03-11-2018', 'teams_700.csv'),
		 ('04-11-2018', 'teams_600.csv'),
		 ('05-11-2018', 'teams_700.csv'),
		 ('07-11-2018', 'teams_700.csv'),
		 ('09-11-2018', 'teams_700.csv'),
		 ('10-11-2018', 'teams_700.csv'),
		 ('21-11-2018', 'teams_700.csv'),
		 ('23-11-2018', 'teams_700.csv'),
		 ('26-11-2018', 'teams_700.csv'),
		 ('28-11-2018', 'teams_700.csv'),
		 ('21-12-2018', 'teams_700.csv'),
		 ('03-12-2018', 'teams_700.csv'),
		 ('05-12-2018', 'teams_700.csv'),
		 ('07-12-2018', 'teams_700.csv'),
		 ('08-12-2018', 'teams_700.csv')]

# 8 to 12 teams
tmeds = [('01-11-2018', 'teams_700.csv'),
		 ('06-11-2018', 'teams_700.csv'),
		 ('08-11-2018', 'teams_800.csv'),
		 ('21-11-2018', 'teams_800.csv'),
		 ('23-11-2018', 'teams_800.csv'),
		 ('24-11-2018', 'teams_730.csv'),
		 ('25-11-2018', 'teams_600.csv'),
		 ('27-11-2018', 'teams_700.csv'),
		 ('28-11-2018', 'teams_800.csv'),
		 ('01-12-2018', 'teams_700.csv'),
		 ('03-12-2018', 'teams_730.csv'),
		 ('04-12-2018', 'teams_700.csv'),
		 ('05-12-2018', 'teams_800.csv'),
		 ('09-12-2018', 'teams_600.csv')]

tbm = []
for t in tbigs:
	tbm.append(t)
for t in tmeds:
	tbm.append(t)

newcols = ['p1_sal', 'p1_team', 'p1_team', 'p1_pg', 'p1_sg', 'p1_sg', 'p1_pf', 'p1_c', 'p1_opp', 'p1_pts', 'p1_ceil', 'p1_floor', 'p2_sal', 'p2_team', 'p2_team', 'p2_pg', 'p2_sg', 'p2_sg', 'p2_pf', 'p2_c', 'p2_opp', 'p2_pts', 'p2_ceil', 'p2_floor', 'p3_sal', 'p3_team', 'p3_team', 'p3_pg', 'p3_sg', 'p3_sg', 'p3_pf', 'p3_c', 'p3_opp', 'p3_pts', 'p3_ceil', 'p3_floor', 'p4_sal', 'p4_team', 'p4_team', 'p4_pg', 'p4_sg', 'p4_sg', 'p4_pf', 'p4_c', 'p4_opp', 'p4_pts', 'p4_ceil', 'p4_floor', 'p5_sal', 'p5_team', 'p5_team', 'p5_pg', 'p5_sg', 'p5_sg', 'p5_pf', 'p5_c', 'p5_opp', 'p5_pts', 'p5_ceil', 'p5_floor', 'p6_sal', 'p6_team', 'p6_team', 'p6_pg', 'p6_sg', 'p6_sg', 'p6_pf', 'p6_c', 'p6_opp', 'p6_pts', 'p6_ceil', 'p6_floor', 'p7_sal', 'p7_team', 'p7_team', 'p7_pg', 'p7_sg', 'p7_sg', 'p7_pf', 'p7_c', 'p7_opp', 'p7_pts', 'p7_ceil', 'p7_floor', 'p8_sal', 'p8_team', 'p8_team', 'p8_pg', 'p8_sg', 'p8_sg', 'p8_pf', 'p8_c', 'p8_opp', 'p8_pts', 'p8_ceil', 'p8_floor', 'y']
path = 'train_ml/{}'


# configs are tuples: (num_lineups, overlap, to_max, name, player_csv, team_csv, actual_csv)
def gen_csv():
	df = pd.DataFrame(columns = newcols)
	if not os.path.isfile(path.format(config[3])):
		with open(path.format(config[3])) as f:
			pass

	


