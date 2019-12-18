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

dks_url = 'https://swishanalytics.com/optimus/nba/fanduel-draftkings-live-scoring?date={}'
r = re.compile(r'this\.players = .*;\n')

def get_dks(datestr):
	dks = {'fpts': {}}
	a = r.search(requests.get(dks_url.format(datestr)).text)
	s = a.group(0)
	s = s[15:len(s)-2]
	
	js = json.loads(s)

	for j in js:
		dks['fpts'][j['name']] = float(j['fpts'])

	return dks

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

		dk = get_dks(datestr_yu)
		with open(dks.format(datestr_me), 'w') as f:
			f.write(json.dumps(dk))

		time.sleep(1)
		
		print(date)
	date += timedelta(days=1)

# https://swishanalytics.com/optimus/nba/fanduel-draftkings-live-scoring?date=2018-10-16
# https://swishanalytics.com/optimus/nba/fanduel-draftkings-live-scoring?date={}