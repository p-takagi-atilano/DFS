
from copy import deepcopy

def get_all_indices(l):
	all_tup = []

	tup = [0]*len(l)
	all_tup.append(deepcopy(tup))

	while sum(tup) < sum(l)-len(l):
		i = len(tup) - 1
		tup[i] += 1
		
		for j in reversed(range(len(tup))):
			if tup[j] == l[j]:
				tup[j] = 0
				tup[j-1] += 1
		all_tup.append(deepcopy(tup))
	
	return all_tup





l = [2, 10, 6]

# [1, 9, 5]

p = [5,7]

a = get_all_indices(l)
for b in a:
	print(b)