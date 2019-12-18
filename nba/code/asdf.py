


INITIAL_SIZE = 10

class DoubleQueue:
	def __init__(self):
		self.queue = [None] * INITIAL_SIZE
		self.length = INITIAL_SIZE
		self.left = 5
		self.right = 5

	def lookup(self, i):
		

