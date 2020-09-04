import pygame, spot, board, common, random

random.seed()

class Player:
	def __init__(self):
		self.wins = 0
		self.name = ""
		self.symbol = ""

	def get_wins(self):
		return self.wins

	def get_name(self):
		return self.name

	def get_symbol(self):
		return self.symbol

	def get_selection(self):
		pass

	def win(self):
		self.win += 1



class User(Player):
	def __init__(self):
		super().__init__()
		self.name = "Player"
		self.symbol = "X"

	def get_selection(self):
		while True:
			# Read in mouse click coordinates
			x, y = common.read_in_mouse_click()
			
			# Determine which box was clicked
			for row in range(3):
				finished = False
				for column in range(3):
					# Return row and column numbers if click was in a spot
					if (x < (spot.SPOT_WIDTH + ((spot.SPOT_WIDTH + board.BOARDER_SIZE) * row)) 
						and y < (spot.SPOT_HEIGHT + ((SPOT_HEIGHT + BOARDER_SIZE) * column))):
						return row, column



class Bot(Player):
	def __init__(self):
		super().__init__()
		self.name = "Computer"
		self.symbol = "O"

	def get_selection(self):
		# Delay for realism
		pygame.time.delay(333)

		row = random.randrange(0, 3)
		column = random.randrange(0, 3)
		return row, column