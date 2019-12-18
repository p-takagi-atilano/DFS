import json
import os
import re
import requests
import sys
import time

import pandas as pd

from datetime import datetime, timedelta

# dates in which there were no nba games
bads = [datetime.strptime('2018-11-22', '%Y-%m-%d'),
		datetime.strptime('02-12-2018', '%Y-%m-%d')]

roto_url = 'https://rotogrinders.com/projected-stats/nba-player?site=draftkings&date={}'
r = re.compile(r'data = .*;\n')

def get_rotogrinders(datestr):
	df = pd.DataFrame(columns=['player_name', 'salary', 'team', 'position', 'opp', 'ceil', 'floor', 'points'])
	a = r.search(requests.get(roto_url.format(datestr)).text)
	s = a.group(0)
	s = s[7:len(s)-2]

	js = json.loads(s)

	for i in range(len(js)):
		row = []
		row.append(js[i]['player_name'])
		row.append(int(float(js[i]['salary'])))
		row.append(js[i]['team'])
		row.append(js[i]['position'])
		row.append(js[i]['opp'])
		row.append(js[i]['ceil'])
		row.append(js[i]['floor'])
		row.append(js[i]['points'])

		df.loc[i] = row
	return df
	
'''
dk_csv = 'datasets/games_2018-2019.csv'
def get_dkscores(datestr):
	df = pd.read_csv(dk_csv)
	js = {'fpts': {}}
	for i,p in df.iterrows():
		if p['Date'] == datestr:
			pts = calc_draftkings_points((p['PTS'], p['TRB'], p['AST'], p['BLK'], p['STL'], p['3P'], p['TOV']))
			js['fpts'][p['Player']] = pts
	return js
'''

#get_dkscores('2018-10-16')

#get_rotogrinders('2018-10-16')

base = 'backtesting_data/{}'
rgp = 'backtesting_data/{}/rotogrinders_predictions.csv'
dks = 'backtesting_data/{}/draftkings_actual_scores.csv'

start_date = '2018-10-16'
end_date = '2018-12-22'

start = datetime.strptime(start_date, '%Y-%m-%d')
end = datetime.strptime(end_date, '%Y-%m-%d')

date = start
while date != end:
	if date not in bads:
		datestr_me = date.strftime('%d-%m-%Y')
		datestr_yu = date.strftime('%Y-%m-%d')

		if not os.path.isdir(base.format(datestr_me)):
			os.mkdir(base.format(datestr_me))

		df = get_rotogrinders(datestr_yu)
		df.to_csv(rgp.format(datestr_me), header=False, index=False)

		time.sleep(1)
		
	print(date)
	date += timedelta(days=1)
