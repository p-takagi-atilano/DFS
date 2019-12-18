
#FILTER_MAP = {'QB_WR1_Stack': QB_WR1_Stack()}

class QB_WR1_Stack:
	def __init__(self):
		pass

	def isValid(self, lineup):
		#print(lineup)
		valid_map = {}

		for i,p in lineup.iterrows():
			if p['Team'] not in valid_map:
				valid_map[p['Team']] = {'QB': 0, 'WR': 0}
			if p['QB'] == 1:
				valid_map[p['Team']]['QB'] += 1
			elif p['WR'] == 1:
				valid_map[p['Team']]['WR'] += 1

			if valid_map[p['Team']]['QB'] >= 1 and valid_map[p['Team']]['WR'] >= 1:
				return True

		return False
