import spot, pygame

SIZE = WIDTH, HEIGHT = 610, 610
BORDER_SIZE = 5

class Board:
	def __init__(self):
		# Create board surface
		self.board = Surface(SIZE)

		# Create spots
		self.spots = []
		for i in range(3):
			self.spots.append(spot.Spot())

		# Print the board
		self.print_board()

	def print_board(self):
		for row in range(3):
			for column in range(3):
				spot = spots[row][column].get_spot()
				x = row * (spot.WIDTH + BORDER_SIZE)
				y = column * (spot.HEIGHT + BORDER_SIZE)
				self.board.blit(spot, (x, y))
		pygame.display.update()

	def take_spot(self, row, column, plyr):
		if spots[row][column].is_taken():
			return False
		else:
			spots[row][column].take_spot(plyr)
			self._update_spot(row, column)
			return True

	def _update_spot(self, row, column):
		spot = spots[row][column].get_spot()
		x = row * (spot.WIDTH + BORDER_SIZE)
		y = column * (spot.HEIGHT + BORDER_SIZE)
		self.board.blit(spot, (x, y))
		pygame.display.update()

	def get_winner(self):
		return self.winner

	def is_game_over(self):
		if not self._check_for_winner():
			for row in range(3):
				for column in range(3):
					if self.spots[row][column] == None:
						return False
			self.winner = 2
		return True

	def _check_for_winner(self):
		for row in range(3):
			for column in range(3):
				if self.spots[row][column].is_taken():
					if self._check_spot_for_win(row, column):
						return True
		return False

	def _check_spot_for_win(self, row, column):
		plyr = self.spots[row][column].get_player_symbol()
		return (self._check_for_horizontal_win(row, plyr) or 
			self._check_for_vertical_win(column, plyr) or 
			self._check_for_diagonal_win(row, column, plyr))

	def _check_for_horizontal_win(self, row, plyr):
		win = True
		for column in range(3):
			if self.spots[row][column].get_player_symbol() != plyr:
				win = False
				break
		return win

	def _check_for_vertical_win(self, column, plyr):
		win = True
		for row in range(3):
			if self.spots[row][column].get_player_symbol() != plyr:
				win = False
				break
		return win

	def _check_for_diagonal_win(self, rpw, column, plyr):
		diagonals = [(0, 0), (1, 1), (2, 2), (0, 2), (2, 0)]

		if (row, column) in diagonals:
			win = True
			for row in range(3):
				column = row
				if self.spots[row][column].get_player_symbol() != plyr:
					win = False
					break
			if win:
				return True

			win = True
			column = 2
			for row in range(3):
				if self.spots[row][column].get_player_symbol() != plyr:
					win = False
					break
				column -= 1
			return win
		return False