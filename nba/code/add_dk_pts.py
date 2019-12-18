import json

import pandas as pd

datestrs = ['27-11-2018', '28-11-2018']

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
datestrs_formatted = []
dkscores = []

for datestr in datestrs:
	date = datestr.split('-')

	sanity = date[2]
	sanity += '-'
	sanity += date[1]
	sanity += '-'
	sanity += date[0]

	datestrs_formatted.append(sanity)

for _ in datestrs_formatted:
	dkscores.append({})
	dkscores[len(dkscores)-1]['fpts'] = {}

for i in range(len(datestrs_formatted)):
	for _, p in players.iterrows():
		if p['Date'] == datestrs_formatted[i]:
			pts_tup = (p['PTS'], p['TRB'], p['AST'], p['BLK'], p['STL'], p['3P'], p['TOV'])
			dkscores[i]['fpts'][p['Player']] = calc_draftkings_points(pts_tup)

for i in range(len(datestrs)):
	with open('backtesting_data/{}/draftkings_actual_scores.csv'.format(datestrs[i]), 'w') as f:
		f.write(json.dumps(dkscores[i]))


# gapminder_2002 = gapminder[gapminder.year == 2002]
