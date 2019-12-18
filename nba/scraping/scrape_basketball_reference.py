import sys
import requests

import time

import numpy as np
import pandas as pd

from bs4 import BeautifulSoup

base = 'https://www.basketball-reference.com'
normal_url = base + '/play-index/psl_finder.cgi?request=1&match=single&type=totals&per_minute_base=36&per_poss_base=100&season_start=1&season_end=-1&lg_id=NBA&age_min=0&age_max=99&is_playoffs=N&height_min=0&height_max=99&year_min=2019&year_max=2019&birth_country_is=Y&as_comp=gt&as_val=0&pos_is_g=Y&pos_is_gf=Y&pos_is_f=Y&pos_is_fg=Y&pos_is_fc=Y&pos_is_c=Y&pos_is_cf=Y&order_by=ws'
advanced_url = base + '/play-index/psl_finder.cgi?request=1&match=single&per_minute_base=36&per_poss_base=100&type=advanced&season_start=1&season_end=-1&lg_id=NBA&age_min=0&age_max=99&is_playoffs=N&height_min=0&height_max=99&year_min=2019&year_max=2019&birth_country_is=Y&as_comp=gt&as_val=0&pos_is_g=Y&pos_is_gf=Y&pos_is_f=Y&pos_is_fg=Y&pos_is_fc=Y&pos_is_c=Y&pos_is_cf=Y&order_by=ws'
game_url = base + '/play-index/pgl_finder.cgi?request=1&match=game&year_min=2019&year_max=2019&is_playoffs=N&age_min=0&age_max=99&season_start=1&season_end=-1&pos_is_g=Y&pos_is_gf=Y&pos_is_f=Y&pos_is_fg=Y&pos_is_fc=Y&pos_is_c=Y&pos_is_cf=Y&order_by=pts'
#game_url = base + '/play-index/pgl_finder.cgi?request=1&match=game&year_min=2018&year_max=2018&is_playoffs=N&age_min=0&age_max=99&season_start=1&season_end=-1&pos_is_g=Y&pos_is_gf=Y&pos_is_f=Y&pos_is_fg=Y&pos_is_fc=Y&pos_is_c=Y&pos_is_cf=Y&order_by=pts'

def get_normal_stats():
	cols = ['Player', 'Season', 'Age', 'TM', 'WS', 'G', 'GS', 'MP', 'FG', 'FGA', '2P', '2PA', '3P', '3PA', 
			'FT', 'FTA', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'DLK', 'TOB', 'PF', 'PTS', 'FG%', '2P%', '3P%', 
			'eFG%', 'FT%', 'TS%']
	return get_stats(cols, normal_url, 0)

def get_advanced_stats():
	cols = ['Player', 'Season', 'Age', 'TM', 'WS', 'G', 'GS', 'MP', 'PER', '3PAr', 'FTr', 'ORB%', 'DRB%', 
			'TRB%', 'AST%', 'STL%', 'BLK%', 'TOV%', 'USG%', 'ORtg', 'DRtg', 'OWS', 'DWS', 'WS/48', 'OBPM',
			'DBPM', 'BPM', 'VORP']
	return get_stats(cols, advanced_url, 1)

def get_game_stats():
	cols = ['Player', 'Pos', 'Date', 'TM', 'OPP', 'H/A', 'W/L', 'GS', 'MP', 'FG', 'FGA', 'FG%', '2P', '2PA', '2P%', '3P',
			'3PA', '3P%', 'FT', 'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS']
	return get_stats(cols, game_url, 2)

def get_stats(cols, url, kind):
	df = pd.DataFrame(columns=cols)

	while url is not None:
		soup = BeautifulSoup(requests.get(url).text, 'lxml')
		table = soup.find('table')
		if table:
			df = df.append(get_stats_helper(table, cols, kind))
	
		url = None
		for a in soup.findAll('a'):
			if a.text == 'Next page':
				url = base + a['href']
		time.sleep(1)

	df.index = [i for i in range(df.count()[0])]
	return df

def get_stats_helper(table, cols, kind):
	df = pd.DataFrame(columns=cols)

	table_body = table.find('tbody')
	for row in table_body.findAll('tr'):
		cells = [p.text for p in row.findAll('td')]
		if cells != [] and cells[4] == 'NBA':
			if kind == 0:
				cells = process_normal(cells)
			elif kind == 1:
				cells = process_advanced(cells)

			df = df.append(pd.DataFrame([cells], columns=cols))

		elif cells != [] and kind == 2:
			cells = process_games(cells)
			df = df.append(pd.DataFrame([cells], columns=cols))			

	return df

def process_normal(cells):
	del cells[4]
	for i in range(len(cells)):
		if i == 2 or 5 <= i <= 24:
			if cells[i] == '':
				cells[i] == np.nan
			else:
				cells[i] = int(cells[i])
		elif i == 4 or i > 24:
			if cells[i] == '':
				cells[i] = np.nan
			else:
				cells[i] = float(cells[i])
	return cells

def process_advanced(cells):
	del cells[4]
	for i in range(len(cells)):
		if i == 2 or 5 <= i <= 7 or 19 <= i <= 20:
			if cells[i] == '':
				cells[i] = np.nan
			else:
				cells[i] = int(cells[i])
		elif i == 4 or 8 <= i <= 18 or i > 20:
			if cells[i] == '':
				cells[i] = np.nan
			else:
				cells[i] = float(cells[i])
	return cells

def process_games(cells):
	del cells[1]
	del cells[-1]
	if cells[4] == '':
		cells.insert(6, 'H')
	else:
		cells.insert(6, 'A')
	del cells[4]

	for i in range(len(cells)):
		if 7 <= i <= 10 or 12 <= i <= 13 or 15 <= i <= 16 or 18 <= i <= 19 or i > 20:
			if cells[i] == '':
				cells[i] = np.nan
			else:
				cells[i] = int(cells[i])
		elif i == 11 or i == 14 or i == 17 or i == 20:
			if cells[i] == '':
				cells[i] = np.nan
			else:
				cells[i] = float(cells[i])

	return cells

#print('getting normal season stats')
#get_normal_stats().to_csv('datasets/season_normal.csv')
#print('getting advanced season stats')
#get_advanced_stats().to_csv('datasets/season_advanced.csv')
print('getting game stats')
get_game_stats().to_csv('datasets/games_2018-2019.csv')
