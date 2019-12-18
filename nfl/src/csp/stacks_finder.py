import pandas as pd

from config import Config
from copy import deepcopy
from data_parser import DataParser
from itertools import combinations


# Currently  only supports stacks of two positions
class GenericStacksFinder:
	# A stacks list is a list of tuples: [('QB', 1), ('WR', 2), ...]
	def __init__(self, stacks_type, data_parser):
		self.stacks_type = stacks_type
		self.data_parser = data_parser

	def find_stacks(self):
		stacks = []
		stacks_map = {}
		stacks_map_entry = {}
		for s in self.stacks_type:
			stacks_map_entry[s] = []
		stacks_map_entry_keys = set(stacks_map_entry.keys())

		for i,p in self.data_parser.players.iterrows():
			for pos in set(stacks_map_entry.keys()):
				if p[pos] == 1:
					if p['Team'] not in stacks_map:
						stacks_map[p['Team']] = deepcopy(stacks_map_entry)
					stacks_map[p['Team']][pos].append(p)

		for team in stacks_map:
			position_combinations = []
			for position in stacks_map[team]:
				position_combinations.append(list(combinations(stacks_map[team][position], self.stacks_type[position])))
			index_list = []
			for i in range(len(position_combinations)):
				index_list.append(len(position_combinations[i]))
			all_indices = self.get_all_indices(index_list)
			for indices in all_indices:
				df = pd.DataFrame()
				for i in range(len(indices)):
					for player in position_combinations[i][indices[i]]:
						df = df.append(player)
				stacks.append(df)
				
		return stacks

	def get_all_indices(self, index_list):
		all_tup = []

		tup = [0]*len(index_list)
		all_tup.append(deepcopy(tup))

		while sum(tup) < sum(index_list)-len(index_list):
			i = len(tup) - 1
			tup[i] += 1
		
			for j in reversed(range(len(tup))):
				if tup[j] == index_list[j]:
					tup[j] = 0
					tup[j-1] += 1
			all_tup.append(deepcopy(tup))
	
		return all_tup

def QB_WR1_stacks_finder(config):
	stacks_type = {'QB': 1, 'WR': 1}
	return GenericStacksFinder(stacks_type, DataParser(config))
