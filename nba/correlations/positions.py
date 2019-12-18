import numpy as numpy


def stats_to_fpts(pts, m3s, rbs, ats, stl, blk, trn):
	p = pts + 
		(0.5 * m3s) + (1.25 * rbs) + 
		(1.5 * ats) + (2 * stl) + 
		(2 * blk) - (0.5 * trn)

	i = 0
	if pts >= 10:
		i += 1
	if rbs >= 10:
		i += 1
	if ats >= 10:
		i += 1
	if stl >= 10:
		i += 1
	if blk >= 10:
		i += 1

	if i >= 2:
		p += 1.5
	if i >= 3:
		p += 3

	return p



'''

pg vs other pg


'''