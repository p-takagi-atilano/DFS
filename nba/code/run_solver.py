import sys

from solver import Solver


def run_solver(num_lineups, overlap, to_max, player_csv, team_csv, verbose=False):
	s = Solver(num_lineups, overlap, to_max, player_csv, team_csv, verbose)
	return s.get_classic_lineups()


if __name__ == '__main__':
	if len(sys.argv) == 6:
		#try:
		run_solver(int(sys.argv[1]), int(sys.argv[2]), sys.argv[3], sys.argv[4], sys.argv[5], True)
		#except Exception as ex:
			#print(ex)
			#print('num_lineups and overlap must be ints')
	else:
		print('Usage: python code/run_solver num_lineups overlap to_max player_csv team_csv verbose=False')

