import json
import os
import random
import re
import requests
import sys
import time

import pandas as pd

from datetime import datetime, timedelta

#'defense'
#qb, flex, defense
roto_url = 'https://rotogrinders.com/projected-stats/nfl-{}?site=draftkings&date={}'
r_roto = re.compile(r'data = .*;\n')

def get_rotogrinders(datestr):
	df = pd.DataFrame(columns=['player_name', 'salary', 'team', 'position', 'opp', 'ceil', 'floor', 'points'])

	df = df.append(get_rotogrinders_helper(datestr, 'qb'), ignore_index=True)
	time.sleep(1)
	df = df.append(get_rotogrinders_helper(datestr, 'flex'), ignore_index=True)
	time.sleep(1)
	df = df.append(get_rotogrinders_helper(datestr, 'defense'), ignore_index=True)

	return df

def get_rotogrinders_helper(datestr, pos):
	df = pd.DataFrame(columns=['player_name', 'salary', 'team', 'position', 'opp', 'ceil', 'floor', 'points'])
	
	a = r_roto.search(requests.get(roto_url.format(pos, datestr)).text)
	s = a.group(0)
	s = s[7:len(s)-2]
	js = json.loads(s)
	
	for i in range(len(js)):
		row = []
		row.append(js[i]['player_name'])
		row.append(js[i]['salary'])
		row.append(js[i]['team'])
		row.append(js[i]['position'])
		row.append(js[i]['opp'])
		row.append(js[i]['ceil'])
		row.append(js[i]['floor'])
		row.append(js[i]['points'])

		df.loc[i] = row

	return df



dks_url = 'https://swishanalytics.com/optimus/nfl/fanduel-draftkings-live-scoring?date={}'
r_swish = re.compile(r'this\.players = .*;\n')

def get_dks(datestr):
	dks = {}
	a = r_swish.search(requests.get(dks_url.format(datestr)).text)
	s = a.group(0)
	s = s[15:len(s)-2]
	
	js = json.loads(s)

	for j in js:
		dks[j['name']] = float(j['fpts_act'])

	return dks



base = 'backtesting_data/2018/week_{}'

start_date = '2018-09-08'
end_date = '2018-12-29'

start = datetime.strptime(start_date, '%Y-%m-%d')
end = datetime.strptime(end_date, '%Y-%m-%d')

errors = {}
i = 1
date = start
while date != end:
	datestr = date.strftime('%Y-%m-%d')
	rgp = get_rotogrinders(datestr)
	dks = get_dks((date + timedelta(days=1)).strftime('%Y-%m-%d'))

	print(i)
	for _,p in rgp.iterrows():
		if p['player_name'] not in dks:
			if p['player_name'] not in errors:
				errors[p['player_name']] = []
			errors[p['player_name']].append(i)

	rgp.to_csv(base.format(i) + '/rotogrinders_predictions.csv')
	with open(base.format(i) + '/draftkings_actual_scores.json', 'w') as f:
		f.write(json.dumps(dks))

	time.sleep(5)
	i += 1
	date += timedelta(days=7)

with open('errors.json', 'w') as f:
	f.write(json.dumps(errors))
