import datetime
import time
import os

from urllib.request import urlretrieve


date = datetime.datetime.today().strftime('%d-%m-%Y')

url = 'https://rotogrinders.com/projected-stats/nba-player.csv?site=draftkings'
destination = 'backtesting_data/{}/rotogrinders_predictions.csv'.format(date)

urlretrieve(url, destination)


# https://rotogrinders.com/projected-stats/nba-player?site=draftkings&date=2018-02-13
# year-month-day
'''
url = 'https://rotogrinders.com/projected-stats/nba-player?site=draftkings&date={}-{}-{}'
def scrape_all_pseudos():
	base = 'backtesting_data'
	for x in os.walk(base):
		if 'pseudo' in x[0]:
			a = 'backtesting_data/pseudo_'
			b = x[0].replace(a, '').split('-')

			urlf = url.format(b[2], b[1], b[0])
			destination = x[0] + '/rotogrinders_predictions.csv'

			print(x[0])
			urlretrieve(urlf, destination)
			time.sleep(0.5)



scrape_all_pseudos()
'''