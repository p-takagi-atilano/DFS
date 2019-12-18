import pandas as pd

# stacks one team's guard and other team's opposing  center
def g_and_center(df):
	for i,p in df.iterrows():
		if p['PG'] or p['SG']:
			for j,q in df.iterrows():
				if q['C'] and p['Team'] == q['Opponent']:
					return True
	return False

def pg_and_c(df):
	for i,p in df.iterrows():
		if p['PG']:
			for j,q in df.iterrows():
				if q['C'] and p['Team'] == q['Team']:
					return True
	return False

# stacks one team's forward and other team's opposing center
def f_and_center(df):
	for i,p in df.iterrows():
		if p['PF'] or p['SF']:
			for j,q in df.iterrows():
				if q['C'] and p['Team'] == q['Opponent']:
					return True
	return False

# stacks guards on same team
def double_g(df):
	for i,p in df.iterrows():
		if p['PG'] or p['SG']:
			for j,q in df.iterrows():
				if i != j and (q['PG'] or q['SG']) and p['Team'] == q['Team']:
					return True
	return False

def lim_teams(df):
	teams = {}
	for i,p in df.iterrows():
		if p['Team'] not in teams:
			teams[p['Team']] = 0
		teams[p['Team']] += 1

	for t in teams:
		if teams[t] >= 3:
			return True
	return False