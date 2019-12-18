import json
import os
import re
import requests
import sys
import time

import pandas as pd

from datetime import datetime, timedelta

bads = [datetime.strptime('2018-11-22', '%Y-%m-%d'),
		datetime.strptime('02-12-2018', '%Y-%m-%d')]

rgp = 'backtesting_data/{}/rotogrinders_predictions.csv'
dks = 'backtesting_data/{}/draftkings_actual_scores.csv'

js = {}
with open('backtesting_data/sa_to_rg.json') as f:
	js = json.loads(f.read())

start_date = '2018-10-16'
end_date = '2018-12-22'

start = datetime.strptime(start_date, '%Y-%m-%d')
end = datetime.strptime(end_date, '%Y-%m-%d')

date = start
while date != end:
	if date not in bads:
		datestr = date.strftime('%d-%m-%Y')
		rg = pd.read_csv(rgp.format(datestr), header=None)
		sa = {}
		with open(dks.format(datestr)) as f:
			sa = json.loads(f.read())

		print(date)
		print(sa)
		for p in rg[0].tolist():
			if p not in sa['fpts']:
				if p in js:
					if js[p] in sa['fpts']:
						sa['fpts'][p] = sa['fpts'][js[p]]
						del sa['fpts'][js[p]]
					else:
						del js[p]
				else:
					a = input('{} >> '.format(p)).split(';')
					if a[0] == '0':		# 0;fpts
						sa['fpts'][p] = float(a[1])
						print('adding')
					elif a[0] == '1':	# 1;sa_name
						try:
							sa['fpts'][p] = sa['fpts'][a[1]]
						except KeyError:
							with open('backtesting_data/sa_to_rg', 'w') as f:
								f.write(json.dumps(js))
						del sa['fpts'][a[1]]
						js[p] = a[1]
						print('switching')
					elif a[0] == '2':	# 2 (player didn't play)
						print('passing')
		
		with open(dks.format(datestr), 'w') as f:
			f.write(json.dumps(sa))

		print()
	date += timedelta(days=1)

with open('backtesting_data/sa_to_rg.json', 'w') as f:
	f.write(json.dumps(js))
