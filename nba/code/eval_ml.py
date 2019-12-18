import json

import pandas as pd

filename = 'train_ml/wa_test.csv'

cs = 'backtesting_data/{}/cash_stats.json'

def eval_ml():
	df = pd.read_csv(filename)
	tot = 0
	gpp = 0
	gpp_11 = 0
	gpp_12 = 0
	gpp_13 = 0
	itm = 0
	for i,p in df.iterrows():
		a = p['meta'].split(':')

		with open(cs.format(a[0])) as f:
			js = json.loads(f.read())

		line = js[a[1].replace('teams_','').replace('.csv', '')]['gpp']

		with open('backtesting_data/{}/draftkings_actual_scores.csv'.format(a[0])) as f:
			actuals = json.loads(f.read())

		score = 0
		score += actuals['fpts'][p['p1_name']]
		score += actuals['fpts'][p['p2_name']]
		score += actuals['fpts'][p['p3_name']]
		score += actuals['fpts'][p['p4_name']]
		score += actuals['fpts'][p['p5_name']]
		score += actuals['fpts'][p['p6_name']]
		score += actuals['fpts'][p['p7_name']]
		score += actuals['fpts'][p['p8_name']]

		if score > line:
			itm += 1

		if p['y'] == 1:
			tot += 1
			if score > line:
				gpp += 1
			if score > line*1.1:
				gpp_11 += 1
			if score > line*1.2:
				gpp_12 += 1
			if score > line*1.3:
				gpp_13 += 1
		#actuals = 
		#line = a[1].replace('teams_','').replace('.csv', '')['gpp']

		#print(line)

	print('{} ITM'.format(itm))
	if tot != 0:
		print('{} Chosen'.format(tot))
		print('Gpp:     {}'.format(gpp/tot))
		print('Gpp 1.1: {}'.format(gpp_11/tot))
		print('Gpp 1.2: {}'.format(gpp_12/tot))
		print('Gpp 1.3: {}'.format(gpp_13/tot))
	else:
		print('None chosen')

if __name__ == "__main__":
	eval_ml()
