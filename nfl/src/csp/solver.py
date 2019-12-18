import warnings

from config import Config
from constrained_model import ConstrainedModel
from backtester import Backtester
from data_parser import DataParser
from draftkings_csv_generator import DraftKingsCsvGenerator
from filters import QB_WR1_Stack

warnings.filterwarnings('ignore')

# Solver class provides all final functionality, by connecting other classes properly
class Solver:
	def __init__(self, config, stack_players=None):
		self.config = config
		self.dataParser = DataParser(config)
		self.constrainedModel = ConstrainedModel(self.config, self.dataParser, stack_players)
		self.backtester = Backtester(self.config, self.dataParser, self.constrainedModel)

	def generate_lineups(self):
		self.constrainedModel.get_lineups()
		return self.constrainedModel.lineups

	def get_lineup_data(self):
		self.backtester.generate_lineup_scores()
		return self.backtester.lineup_report()




