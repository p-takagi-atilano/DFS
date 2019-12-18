from pulp import *

from libs.constants import BUDGET#, MAX_OVERLAP

decision_vars = []

def add_feasibility_constraints(model, players, to_max, b=True):
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
		decision_vars.append(decision_var)
		
		if to_max == '1':
			total_points[decision_var] = p['Ceiling'] + p['Points']
		elif to_max == '2':
			total_points[decision_var] = p['Ceiling'] + p['Floor']
		elif to_max == '3':
			total_points[decision_var] = p['Points'] + p['Floor']
		elif to_max == '4':
			total_points[decision_var] = (p['Ceiling']-p['Points'])*p['Points']
		else:
			total_points[decision_var] = p[to_max]
			

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

	if b:
		model += (total_cost <= BUDGET)

	model += (total_players == 8)

	model += (1 <= pg_constraint <= 3)
	model += (1 <= sg_constraint <= 3)
	model += (1 <= sf_constraint <= 3)
	model += (1 <= pf_constraint <= 3)
	model += (1 <= c_constraint <= 2)

	#model += (2 <= g_constraint <= 4)
	#model += (2 <= f_constraint <= 4)


# pg on one team, c on other team, doesnt work very well
def add_usage_constraints(model, players):
	tms = []
	dvars = []

	for i in range(len(decision_vars)):
		itup = _get_info_from_decision_var(decision_vars[i], players)
		if itup[2] == 'g':
			tm = {}
			tm[decision_vars[i]] = 0.9
			for j in range(len(decision_vars)):
				if i != j:
					jtup = _get_info_from_decision_var(decision_vars[j], players)
					if itup[0] == jtup[1] and jtup[2] == 'c':
						tm[decision_vars[j]] = .1
					else:
						tm[decision_vars[j]] = 0

			x = pulp.LpAffineExpression(tm)
			tms.append(x)

	for i in range(len(tms)):
		y = pulp.LpVariable('y' + str(i), cat='Binary')
		dvars.append(y)
		model += (tms[i] >= y)

	for i in range(len(tms)):
		model += ((1 - 0) * (1-dvars[i])<= tms[i] <= (1 + 2) * (1-dvars[i]))

	# 1 - M * (1-δ(i)) <= L(i) <= 1 + M * (1-δ(i)) 

	model += (sum(dvars) >= 1)
	



	# TODO: Add different team constraints

def _get_info_from_decision_var(decision_var, players):
	i = int(decision_var.name[1:])
	team = players.at[i, 'Team']
	opp = players.at[i, 'Opponent']
	if players.at[i, 'PG'] or players.at[i, 'SG']:
		pos = 'g'
	elif players.at[i, 'C']:
		pos = 'c'
	else:
		pos = None

	return team, opp, pos

def add_overlap_constraints(model, players, prev, max_overlap):
	# adds previous overlap constraint
	overlap = {}
	for d in decision_vars:
		overlap[d] = 0
	for d in prev:
		overlap[d] = 1

	overlap_constraint = pulp.LpAffineExpression(overlap)

	model += (overlap_constraint <= max_overlap)
