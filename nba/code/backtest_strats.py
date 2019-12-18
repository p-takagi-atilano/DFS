import pandas as pd
import random

from sklearn.tree import DecisionTreeClassifier

from backtesting import backtest_fast
from ml_make_one import make_one
from eval_ml import eval_ml
#from libs.data_handling import get_teams, get_players

simple = [('16-10-2018', 'teams_700.csv')]

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

# 6 or fewer teams
tsmls = [('01-11-2018', 'teams_800.csv'),
		 ('02-11-2018', 'teams_800.csv'),
		 ('02-11-2018', 'teams_1000.csv'),
		 ('03-11-2018', 'teams_800.csv'),
		 ('03-11-2018', 'teams_900.csv'),
		 ('04-11-2018', 'teams_700.csv'),
		 ('04-11-2018', 'teams_900.csv'),
		 ('05-11-2018', 'teams_730.csv'),
		 ('05-11-2018', 'teams_900.csv'),
		 ('05-11-2018', 'teams_1030.csv'),
		 ('06-11-2018', 'teams_900.csv'),
		 ('07-11-2018', 'teams_800.csv'),
		 ('07-11-2018', 'teams_1000.csv'),
		 ('08-11-2018', 'teams_1000.csv'),
		 ('09-11-2018', 'teams_800.csv'),
		 ('09-11-2018', 'teams_930.csv'),
		 ('21-11-2018', 'teams_900.csv'),
		 ('23-11-2018', 'teams_1200.csv'),
		 ('23-11-2018', 'teams_1030.csv'),
		 ('24-11-2018', 'teams_800.csv'),
		 ('24-11-2018', 'teams_830.csv'),
		 ('25-11-2018', 'teams_330.csv'),
		 ('25-11-2018', 'teams_800.csv'),
		 ('26-11-2018', 'teams_800.csv'),
		 ('26-11-2018', 'teams_900.csv'),
		 ('27-11-2018', 'teams_730.csv'),
		 ('27-11-2018', 'teams_900.csv'),
		 ('28-11-2018', 'teams_1000.csv'),
		 ('29-11-2018', 'teams_800.csv'),
		 ('29-11-2018', 'teams_1030.csv'),
		 ('01-12-2018', 'teams_800.csv'),
		 ('03-12-2018', 'teams_800.csv'),
		 ('04-12-2018', 'teams_730.csv'),
		 ('04-12-2018', 'teams_900.csv'),
		 ('06-12-2018', 'teams_800.csv'),
		 ('06-12-2018', 'teams_1000.csv'),
		 ('07-12-2018', 'teams_800.csv'),
		 ('07-12-2018', 'teams_900.csv'),
		 ('08-12-2018', 'teams_800.csv'),
		 ('08-12-2018', 'teams_1000.csv'),
		 ('09-12-2018', 'teams_700.csv'),
		 ('10-11-2018', 'teams_800.csv'),
		 ('10-11-2018', 'teams_900.csv'),
		 ('10-11-2018', 'teams_300.csv')]

result_path = 'strats/{}.csv'

tbm = []
for t in tbigs:
	tbm.append(t)
for t in tmeds:
	tbm.append(t)

'''
t_test = []
used = set()
for _ in range(1):
	i = random.randint(0, len(tbm)-1)
	while i in used:
		i = random.randint(0, len(tbm)-1)
	t_test.append(tbm[i])
	used.add(i)
t_train = []
for t in tbm:
	if t not in t_test:
		t_train.append(t)
'''

def test_strat(overlap, to_max, name, tests, fltr=None, ml=False):
	base = 'backtesting_data'

	b = []
	for t in tests:
		b.append((300, overlap, to_max, '{}:{}'.format(t[0], t[1]), 
			      '{}/{}/{}'.format(base, t[0], 'rotogrinders_predictions.csv'),
			      '{}/{}/{}'.format(base, t[0], t[1]),
			      '{}/{}/{}'.format(base, t[0], 'draftkings_actual_scores.csv')))

	df = backtest_fast(b, fltr, ml)
	df.to_csv(result_path.format(name))


def insanity():

	test_strat(7, '4', 'train', t_train, ml=True)

	df = make_one('wa_train')
	df_temp = df[df.columns.difference(['p1_name', 'p2_name', 'p3_name', 'p4_name', 'p5_name', 'p6_name', 'p7_name', 'p8_name', 'meta'])]
	x_train = df_temp.loc[:, df_temp.columns != 'y']
	y_train = df_temp['y']
	y_train = y_train.astype('int') 
	etc = DecisionTreeClassifier(criterion='entropy')
	etc.fit(x_train, y_train)

	test_strat(7, '4', 'test', t_test, fltr=etc, ml=True)
	df = make_one('wa_test')
	#print(df)
	#print(df)
	#print(len([a for a in df['y'].tolist() if a == 1]))
	#print(len(df['y'].tolist()))
	eval_ml()


#eval_ml()


for i in range(len(tbm)):
#for i in range(1):
	t_test = []
	t_test.append(tbm[i])
	t_train = []
	print(tbm[i])
	for j in range(len(tbm)):
		if j != i:
			t_train.append(tbm[j])
	insanity()
	print()


# Live Strats:
#test_strat(6, 'Points', 'testlive', simple)
#test_strat(6, 'Points', 'testlive_nopg', simple, -1)
#test_strat(4, 'Points', 'tmeds_pg', tmeds, 1)
#test_strat(4, 'Points', 'tmeds_nopg', tmeds, -1)
#test_strat(7, 'Ceiling', 'tsmls_pg', tsmls, 1)
#test_strat(7, 'Ceiling', 'tsmls_nopg', tsmls, -1)

#print('doing nousage')
#test_strat(6, 'Points', 'Points_6_tbigs_pg', tbigs)

#test_strat(6, 'Points', 'asdf', tbigs)
#test_strat(6, 'Points', 'asdf_pg', tbigs, 1)
#test_strat(6, 'Points', 'asdf_pf', tbigs, 2)
#test_strat(6, 'Points', 'asdf_dg', tbigs, -3)
#test_strat(6, 'Points', 'asdf_pc', tbigs, 5)
#test_strat(6, 'Points', 'asdf_npc', tbigs, -5)
#test_strat(6, 'Points', 'asdf_pc', tbigs, 5)
#test_strat(6, 'Points', 'asdf_lt2', tbigs, 4)
#test_strat(6, 'Points', 'asdf_nlt2', tbigs, -4)
#test_strat(6, '4', 'asdf_wa', tbigs)
#test_strat(4, 'Ceiling', 'asdf_ceil4', tbigs)
#test_strat(7, 'Ceiling', 'asdf_ceil7', tbigs)
#test_strat(7, 'Ceiling', 'asdf_ceil7o', tbigs, 6)
#test_strat(7, '4', 'asdf_wa7', tbigs)
#test_strat(6, '4', 'asdf_wa6o', tbigs, 6)
#test_strat(7, '4', 'asdf_wa7o', tbigs, 6)

'''
test_strat(7, 'Points', 'meds_p7', tsmls, 6)
test_strat(7, 'Ceiling', 'meds_c7', tsmls, 6)
test_strat(7, '4', 'meds_w7', tsmls, 6)
test_strat(6, 'Points', 'meds_p6', tsmls, 6)
test_strat(6, 'Ceiling', 'meds_c6', tsmls, 6)
test_strat(6, '4', 'meds_w6', tsmls, 6)
test_strat(5, 'Points', 'meds_p5', tsmls, 6)
test_strat(5, 'Ceiling', 'meds_c5', tsmls, 6)
test_strat(5, '4', 'meds_w5', tsmls, 6)
test_strat(4, 'Points', 'meds_p4', tsmls, 6)
test_strat(4, 'Ceiling', 'meds_c4', tsmls, 6)
test_strat(4, '4', 'meds_w4', tsmls, 6)
'''
#test_strat(7, '4', 'wa_fn3', tbm, -3)
#test_strat(7, '4', 'wa_fn5', tbm, -5)
#test_strat(7, '4', 'wa_fn0', tbm, 6)



'''
for i in range(4, 8):
	print(i)
	test_strat(i, 'Ceiling', 'Ceiling_{}_tbigs'.format(i), tbigs)
	test_strat(i, 'Ceiling', 'Ceiling_{}_tmeds'.format(i), tmeds)
	test_strat(i, 'Ceiling', 'Ceiling_{}_tsmls'.format(i), tsmls)
	test_strat(i, 'Points', 'Points_{}_tbigs'.format(i), tbigs)
	test_strat(i, 'Points', 'Points_{}_tmeds'.format(i), tmeds)
	test_strat(i, 'Points', 'Points_{}_tsmls'.format(i), tsmls)
	test_strat(i, 'Floor', 'Floor_{}_tbigs'.format(i), tbigs)
	test_strat(i, 'Floor', 'Floor_{}_tmeds'.format(i), tmeds)
	test_strat(i, 'Floor', 'Floor_{}_tsmls'.format(i), tsmls)

	test_strat(i, 'Ceiling', 'Ceiling_{}_tbigs_pg'.format(i), tbigs, 1)
	test_strat(i, 'Ceiling', 'Ceiling_{}_tmeds_pg'.format(i), tmeds, 1)
	test_strat(i, 'Ceiling', 'Ceiling_{}_tsmls_pg'.format(i), tsmls, 1)
	test_strat(i, 'Points', 'Points_{}_tbigs_pg'.format(i), tbigs, 1)
	test_strat(i, 'Points', 'Points_{}_tmeds_pg'.format(i), tmeds, 1)
	test_strat(i, 'Points', 'Points_{}_tsmls_pg'.format(i), tsmls, 1)
	test_strat(i, 'Floor', 'Floor_{}_tbigs_pg'.format(i), tbigs, 1)
	test_strat(i, 'Floor', 'Floor_{}_tmeds_pg'.format(i), tmeds, 1)
	test_strat(i, 'Floor', 'Floor_{}_tsmls_pg'.format(i), tsmls, 1)
'''
