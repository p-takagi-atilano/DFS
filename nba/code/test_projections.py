import json
import os
import re
import requests
import sys
import time

import numpy as np
import pandas as pd

from datetime import datetime, timedelta

bads = [datetime.strptime('2018-11-22', '%Y-%m-%d'),
		datetime.strptime('2018-12-02', '%Y-%m-%d')]

rgp = 'backtesting_data/{}/rotogrinders_predictions.csv'
dks = 'backtesting_data/{}/draftkings_actual_scores.csv'

diffs = []


start_date = '2018-10-16'
end_date = '2018-12-22'

start_date = '2018-11-03'
end_date = '2018-11-04'

start = datetime.strptime(start_date, '%Y-%m-%d')
end = datetime.strptime(end_date, '%Y-%m-%d')

date = start
while date != end:
	if date not in bads:
		subdiff = 0
		datestr = date.strftime('%d-%m-%Y')
		rg = pd.read_csv(rgp.format(datestr), header=None)
		with open(dks.format(datestr)) as f:
			dk = json.loads(f.read())
			
			for i,p in rg.iterrows():
				#print(p)
				diffs.append(p[7] - dk['fpts'][p[0]])
				subdiff += p[7] - dk['fpts'][p[0]]

		#diffs.append(subdiff)
	date += timedelta(days=1)

print(np.mean(diffs))
print(np.std(diffs))
