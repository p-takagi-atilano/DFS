#import multithreading
#import multiprocessing

import multiprocessing as mp

from backtester import Backtester
from config import Config
from constrained_model import ConstrainedModel
from data_parser import DataParser
from solver import Solver
from stacks_finder import QB_WR1_stacks_finder

# generates stacks of players, and runs each one on a constrained model on a different thread
class Stacker:
	def __init__(self, config, stacks_finder):
		self.config = config
		self.data_parser = DataParser(self.config)
		self.stacks = stacks_finder.find_stacks()
		self.solution_queue = mp.Queue()
		self.num_lineups = self.modify_num_lineups(config)
		self.lineups = []

	def solve_one(self, i):
		solver = Solver(self.config, stack_players = self.stacks[i])
		solver.generate_lineups()
		self.solution_queue.put(solver)
		return

	def solve_some(self):
		processes = [mp.Process(target=self.solve_one, args=(x,)) for x in range(len(self.stacks))]
		
		for p in processes:
			p.start()

		#for p in processes:
		#	p.join()

		results = [self.solution_queue.get() for p in processes]
		for i in range(self.num_lineups):
			self.lineups.append(results[i%len(results)].constrainedModel.lineups[int(i/len(results))])
		
	def modify_overlap(self):
		pass

	def generate_backtest_report(self):
		backtester = Backtester(self.config, self.data_parser, None, self.lineups)
		backtester.generate_lineup_scores()
		return backtester.lineup_report()

	def modify_num_lineups(self, config):
		num_lineups = self.config.num_lineups
		self.config.num_lineups = int(self.config.num_lineups / len(self.stacks)) + 1
		return num_lineups

'''
config = Config(150, 5, 'Points', '2018', 'week_2', False, None)
s = Stacker(config, QB_WR1_stacks_finder(config))
s.solve_some()
print(len(s.lineups))
print(s.generate_backtest_report())

config = Config(150, 5, 'Points', '2018', 'week_3', False, None)
s = Stacker(config, QB_WR1_stacks_finder(config))
s.solve_some()
print(len(s.lineups))
print(s.generate_backtest_report())


config = Config(150, 5, 'Points', '2018', 'week_4', False, None)
s = Stacker(config, QB_WR1_stacks_finder(config))
s.solve_some()
print(len(s.lineups))
print(s.generate_backtest_report())
'''

config = Config(150, 5, 'Points', '2018', 'week_5', False, None)
s = Stacker(config, QB_WR1_stacks_finder(config))
s.solve_some()
print(len(s.lineups))
print(s.generate_backtest_report())

config = Config(150, 5, 'Points', '2018', 'week_6', False, None)
s = Stacker(config, QB_WR1_stacks_finder(config))
s.solve_some()
print(len(s.lineups))
print(s.generate_backtest_report())

config = Config(150, 5, 'Points', '2018', 'week_7', False, None)
s = Stacker(config, QB_WR1_stacks_finder(config))
s.solve_some()
print(len(s.lineups))
print(s.generate_backtest_report())

config = Config(150, 5, 'Points', '2018', 'week_8', False, None)
s = Stacker(config, QB_WR1_stacks_finder(config))
s.solve_some()
print(len(s.lineups))
print(s.generate_backtest_report())

config = Config(150, 5, 'Points', '2018', 'week_9', False, None)
s = Stacker(config, QB_WR1_stacks_finder(config))
s.solve_some()
print(len(s.lineups))
print(s.generate_backtest_report())

config = Config(150, 5, 'Points', '2018', 'week_10', False, None)
s = Stacker(config, QB_WR1_stacks_finder(config))
s.solve_some()
print(len(s.lineups))
print(s.generate_backtest_report())

config = Config(150, 5, 'Points', '2018', 'week_11', False, None)
s = Stacker(config, QB_WR1_stacks_finder(config))
s.solve_some()
print(len(s.lineups))
print(s.generate_backtest_report())

config = Config(150, 5, 'Points', '2018', 'week_13', False, None)
s = Stacker(config, QB_WR1_stacks_finder(config))
s.solve_some()
print(len(s.lineups))
print(s.generate_backtest_report())

config = Config(150, 5, 'Points', '2018', 'week_14', False, None)
s = Stacker(config, QB_WR1_stacks_finder(config))
s.solve_some()
print(len(s.lineups))
print(s.generate_backtest_report())

config = Config(150, 5, 'Points', '2018', 'week_15', False, None)
s = Stacker(config, QB_WR1_stacks_finder(config))
s.solve_some()
print(len(s.lineups))
print(s.generate_backtest_report())

