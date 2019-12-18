import sys

filename = 'backtesting_data/{}/rotogrinders_predictions.csv'.format(sys.argv[1])

s = ''
with open(filename, 'r') as f:
	a = f.readline()
	while a:
		l = a.split(',')
		stemp = ''
		for i in range(len(l)):
			if i == 0:
				stemp += '"'
				stemp += l[i]
				stemp += '"'
			elif i == 1:
				stemp += str(int(float(l[i].replace('$', '').replace('K', ''))*1000))
			elif i == 4:
				stemp += l[i].replace('@ ', '')
			else:
				stemp += l[i]

			if i != len(l)-1:
				stemp += ','
		s += stemp
		a = f.readline()


with open(filename, 'w') as f:
	f.write(s)

