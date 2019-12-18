import datetime
import json
import os

import pandas as pd

# data is tuple: (points, rebounds, assists, blocks, steals, 3pts, turnovers)
def calc_draftkings_points(data):
	pts = data[0] + 1.25 * data[1] + 1.5 * data[2] + 2 * (data[3] + data[4]) + 0.5 * (data[5] - data[6])

	c = 0
	for i in range(len(data)):
		if 0 <= i <= 4:
			c += 1
	if c == 2:
		return pts + 1.5
	elif c >= 3:
		return pts + 4.5
	return pts

players = pd.read_csv('datasets/games_2018-2019.csv')
#players = pd.read_csv('datasets/games_2017-2018.csv')

gamedir = {} # date -> player, pts

for _, p in players.iterrows():
	date = p['Date'].split('/')
	#print(date)
	#date = 'pseudo_' + date[2] + '-' + date[1] + '-' + date[0]
	
	if len(date[1]) == 1:
		date[1] = '0' + date[1]

	date = 'pseudo_' + date[1] + '-' + date[0] + '-20' + date[2]

	#print(date)
	if date not in gamedir:
		gamedir[date] = {'fpts' : {}}
	gamedir[date]['fpts'][p['Player']] = calc_draftkings_points((p[-1], p[-7], p[-6], p[-4], p[-5], p[16], p[-3]))

for date in gamedir:
	path = 'backtesting_data/{}'.format(date)
	if not os.path.isdir('backtesting_data/{}'.format(date)):
		os.makedirs(path)
	with open(path + '/draftkings_actual_scores.json', 'w') as f:
		f.write(json.dumps(gamedir[date]))

