from pulp import *

from data_handling import format_data

import numpy as np
import pandas as pd

num_lineups = 100
max_overlap = 7

budget = 50000



def add_feasibility_constraints(model, players):
	total_points = {}
	cost = {}
	number_of_players = {}

	pg = {}
	sg = {}
	sf = {}
	pf = {}
	c = {}

	for i, p in players.iterrows():
		decision_var = pulp.LpVariable('x' + str(i), cat='Binary')

		total_points[decision_var] = p['Points']
		cost[decision_var] = p['Salary']
		number_of_players[decision_var] = 1

		pg[decision_var] = p['PG']
		sg[decision_var] = p['SG']
		sf[decision_var] = p['SF']
		pf[decision_var] = p['PF']
		c[decision_var] = p['C']
	

	g = {**pg, **sg}
	f = {**sf, **pf}

	objective_function = pulp.LpAffineExpression(total_points)
	total_cost = pulp.LpAffineExpression(cost)
	total_players = pulp.LpAffineExpression(number_of_players)

	pg_constraint = pulp.LpAffineExpression(pg)
	sg_constraint = pulp.LpAffineExpression(sg)
	sf_constraint = pulp.LpAffineExpression(sf)
	pf_constraint = pulp.LpAffineExpression(pf)
	c_constraint = pulp.LpAffineExpression(c)

	g_constraint = pulp.LpAffineExpression(g)
	f_constraint = pulp.LpAffineExpression(f)


	model += objective_function
	model += (total_cost <= budget)
	model += (total_players == 8)

	model += (1 <= pg_constraint <= 3)
	model += (1 <= sg_constraint <= 3)
	model += (1 <= sf_constraint <= 3)
	model += (1 <= pf_constraint <= 3)
	model += (1 <= c_constraint <= 2)

	model += (2 <= g_constraint <= 4)
	model += (2 <= f_constraint <= 4)
	#model += (False)

	# TODO: Add different team constraints

def add_overlap_constraints(model, players, lineups):
	pass

def get_solution_lineup(model, players):
	used = set()
	players['is_drafted'] = 0
	#print(players)
	for var in model.variables():
		if var.varValue==1:
			used.add(var)
		players.iloc[int(var.name[1:]),12] = var.varValue

	my_team = players[players["is_drafted"] == 1.0]
	print(my_team)
	print("Total Salary: {}".format(my_team["Salary"].sum()))
	print("Projected points: {}".format(my_team["Points"].sum().round(1)))
	return my_team, used


players = format_data()
print(players)

model = pulp.LpProblem('NBA DFS', pulp.LpMaximize)

add_feasibility_constraints(model, players)
model.solve()
#print(model.solve())

get_solution_lineup(model, players)

'''
def get_lineups():
	lineups = []
	for i in range(len(num_lineups)):
		add_feasibility_constraints(model, players)
		if i != 0:
			add_overlap_constraints(model, players)
	
		if model.solve():
			lineups.append(get_solution_lineup(model, players))
		else:
			return None
	return lineups
'''


