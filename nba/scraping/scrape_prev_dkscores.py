import datetime
import json
import re
import urllib.request

import pandas as pd

url = 'https://rotogrinders.com/game-stats?site=draftkings&sport=nba&range=yesterday'

source = urllib.request.urlopen(url).read().decode('utf-8')

r = re.compile(r'var data = .*;\n')
a = r.search(source)
try:
	s = a.group(0)
	s = s[11:len(s)-2]

	df = pd.read_json(s)
	df = df[['player','fpts']]
	df = df.set_index('player')

	date = (datetime.datetime.today() - datetime.timedelta(1)).strftime('%d-%m-%Y')

	df.to_json('backtesting_data/{}/draftkings_actual_scores.csv'.format(date))
except:
	print('Could not scrape, check to see if games yesterday')
