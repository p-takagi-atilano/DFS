from pulp import *

import numpy as np
import pandas as pd

#LpSolverDefault.msg = 2

class ConstrainedModel:
	def __init__(self, config, dataParser, stack_players, budget=50000, verbose=False):

		self.config = config
		self.dataParser = dataParser
		
		self.verbose = verbose

		self.model = pulp.LpProblem('', pulp.LpMaximize)
		self.decision_vars = []
		self.lineups = []

		self.budget = budget
		self.total_players_constraint = 9
		self.dst_constraint = 1
		self.qb_constraint = 1
		self.rb_constraint_min = 2
		self.rb_constraint_max = 3
		self.wr_constraint_min = 3
		self.wr_constraint_max = 4
		self.te_constraint_min = 1
		self.te_constraint_max = 2

		self.stack_players = stack_players

	### Constraints Functions ###
	def add_feasibility_constraints(self):
		total_points = {}
		cost = {}
		number_of_players = {}

		qb = {}
		rb = {}
		wr = {}
		te = {}
		dst = {}

		for i,p in self.dataParser.players.iterrows():
			if pd.isna(p['Salary']):
				continue
			if self.stack_players is not None and p['Name'] in self.stack_players['Name'].unique():
				continue


			decision_var = pulp.LpVariable('x' + str(i), cat='Binary')
			self.decision_vars.append(decision_var)
			
			total_points[decision_var] = p[self.config.to_max]
			cost[decision_var] = p['Salary']

			number_of_players[decision_var] = 1

			qb[decision_var] = p['QB']
			rb[decision_var] = p['RB']
			wr[decision_var] = p['WR']
			te[decision_var] = p['TE']
			dst[decision_var] = p['DST']

		objective_function = pulp.LpAffineExpression(total_points)
		
		total_cost = pulp.LpAffineExpression(cost)
		total_players = pulp.LpAffineExpression(number_of_players)

		qb_constraint = pulp.LpAffineExpression(qb)
		rb_constraint = pulp.LpAffineExpression(rb)
		wr_constraint = pulp.LpAffineExpression(wr)
		te_constraint = pulp.LpAffineExpression(te)
		dst_constraint = pulp.LpAffineExpression(dst)

		self.model += objective_function

		self.model += (total_cost <= self.budget)
		self.model += (total_players == self.total_players_constraint)

		self.model += (dst_constraint == self.dst_constraint)
		self.model += (qb_constraint == self.qb_constraint)

		self.model += (self.rb_constraint_min <= rb_constraint)
		self.model += (rb_constraint <= self.rb_constraint_max)

		self.model += (self.wr_constraint_min <= wr_constraint)
		self.model += (wr_constraint <= self.wr_constraint_max)

		self.model += (self.te_constraint_min <= te_constraint)
		self.model += (te_constraint <= self.te_constraint_max)

	# stack_players is a pandas dataframe of the players that are forced onto the lineups
	def add_player_stack(self):
		if self.stack_players is None:
			return

		for i,p in self.stack_players.iterrows():
			self.budget -= p['Salary']
			self.total_players_constraint -= 1

			if p['DST'] == 1:
				self.dst_constraint -= 1
			if p['QB'] == 1:
				self.qb_constraint -= 1
			if p['RB'] == 1:
				self.rb_constraint_min -= 1
				self.rb_constraint_max -= 1
			if p['WR'] == 1:
				self.wr_constraint_min -= 1
				self.wr_constraint_max -= 1
			if p['TE'] == 1:
				self.te_constraint_min -= 1
				self.te_constraint_max -= 1

	def add_stack_players_to_final_lineup(self, lineup):
		if self.stack_players is None:
			return lineup

		return lineup.append(self.stack_players)

	# adds previous overlap constraint
	def add_overlap_constraints(self, prev):
		overlap = {}
		for d in self.decision_vars:
			overlap[d] = 0
		for d in prev:
			overlap[d] = 1
		overlap_constraint = pulp.LpAffineExpression(overlap)

		self.model += (overlap_constraint <= self.config.overlap)


	### CSP Solving Functions ###
	def get_lineups(self):
		prev = None
		feas = True
		while len(self.lineups) < self.config.num_lineups:
			if feas:
				self.add_player_stack()
				self.add_feasibility_constraints()
				feas = False
			else:
				if prev is not None:
					self.add_overlap_constraints(prev)
				prev = None
			
			if self.model.solve() == 1:
				sol = self.get_solution()
				self.lineups.append(self.add_stack_players_to_final_lineup(sol[0]))
				prev = sol[1]

	def get_solution(self):
		sol = []
		self.dataParser.players['is_drafted'] = 0 

		for var in self.model.variables():
			if var.varValue == 1:
				sol.append(var)
			self.dataParser.players.iloc[int(var.name[1:]),12] = var.varValue

		my_team = self.dataParser.players[self.dataParser.players["is_drafted"] == 1.0]	

		if self.verbose:
			print(my_team)
			print("Salary: {}".format(my_team["Salary"].sum()))
			print("Floor: {}, Points: {}, Ceiling: {}".format(my_team["Floor"].sum().round(1), my_team["Points"].sum().round(1), my_team["Ceiling"].sum().round(1)))

		return my_team, sol
