import warnings

from pulp import *

from libs.constraints import add_feasibility_constraints, add_usage_constraints, add_overlap_constraints
from libs.data_handling import get_teams, get_players, get_solution_lineup

import numpy as np
import pandas as pd

warnings.filterwarnings("ignore")
#LpSolverDefault.msg = 1

# configs are tuples: (num_lineups, overlap, to_max, name, player_csv, team_csv)
def solve(configs, verbose=False):
	players = get_players(configs[4], get_teams(configs[5]))
	model = pulp.LpProblem('',pulp.LpMaximize)

	solutions = []
	for config in configs:
		lineups = []
		prev = None
		for i in range(config[0]):
			if i == 0:
				add_feasibility_constraints(model, players, config[2])
			else:
				add_overlap_constraints(model, players, prev, config[1])

			if model.solve():
				sol = get_solution_lineup(model, players, verbose)
				lineups.append(sol[0]['Name'].tolist())
				prev = sol[1]

		solutions.append(lineups)
		model._variables.clear()
		print('Completed: {}'.format(config[3]))

	return solutions

# configs are tuples: (num_lineups, overlap, to_max, name, player_csv, team_csv)
def solve_one(config, verbose=False, usage=False):
	players = get_players(config[4], get_teams(config[5]))
	model = pulp.LpProblem('',pulp.LpMaximize)

	lineups = []
	sols = []

	prev = None
	for i in range(config[0]):
		if i == 0:
			add_feasibility_constraints(model, players, config[2])
			if usage:
				add_usage_constraints(model, players)
		else:
			add_overlap_constraints(model, players, prev, config[1])

		if model.solve():
			sol = get_solution_lineup(model, players, verbose)
			lineups.append(sol[0]['Name'].tolist())
			sols.append(sol[0])
			prev = sol[1]
		else:
			return lineups, sols

	return lineups, sols




class Solver:
	def __init__(self, num_lineups, overlap, to_max, player_csv, team_csv, verbose=True):
		self.num_lineups = num_lineups
		self.to_max = to_max
		self.teams = get_teams(team_csv)
		self.players = get_players(player_csv, self.teams)
		self.model = pulp.LpProblem('',pulp.LpMaximize)
		self.overlap = overlap
		self.verbose = verbose
	
	def get_classic_lineups(self):
		#LpSolverDefault.msg = 1
		lineups = []
		prev = None
		for i in range(self.num_lineups):
			#model = pulp.LpProblem('NBA DFS', pulp.LpMaximize)
			if i == 0:
				add_feasibility_constraints(self.model, self.players, self.to_max)
			else:
				add_overlap_constraints(self.model, self.players, prev, self.overlap)

			#print(model)
			if self.model.solve():
				sol = get_solution_lineup(self.model, self.players, self.verbose)
				lineups.append(sol[0]['Name'])
				prev = sol[1]
		#self.model = pulp.LpProblem('NBA DFS', pulp.LpMaximize)
		print(self.model._variables)
		self.model._variables.clear()
		print(self.model._variables)

		return lineups


#s = Solver(5, 7, 'nba-player.csv', 'Ceiling')
#l = s.get_lineups()
#print(l)
