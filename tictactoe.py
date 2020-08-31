import pygame, random, sys
from pygame.locals import *

WINDOW_SIZE = (610, 610)
BLACK = 0, 0, 0
WHITE = 255, 255, 255

class TicTacToe:

	def __init__(self):
		pygame.init()
		random.seed()
		self._load_in_resources()
		self._initialize_window()
		self._initialize_board()
		self._main_loop()



	def _load_in_resources(self):
		self.empty = pygame.image.load("resources/images/empty.png")
		self.emptyRect = self.empty.get_rect()
		self.x = pygame.image.load("resources/images/x.png")
		self.xRect = self.x.get_rect()
		self.o = pygame.image.load("resources/images/o.png")
		self.oRect = self.o.get_rect()



	def _initialize_window(self):
		self.screen = pygame.display.set_mode(WINDOW_SIZE)
		self._reset_board()




	def _initialize_board(self):
		self.board = []
		for i in range(3):
			self.board.append([None] * 3)



	def _reset_board(self):
		# Fill screen with black
		self.screen.fill(BLACK)

		# Print empty squares where they would be on the board
		for i in range(3):
			for j in range(3):
				self._draw_box(self.empty, self.emptyRect, i, j)



	def _reset_game(self):
		self._reset_board()
		self._initialize_board()


	def _main_loop(self):
		while True:
			self._game_loop()
			if not self._play_again():
				break
			self._reset_game()



	def _play_again(self):
		while True:
			playAgain = input("Would you like to play again? (Y/N): ")
			if playAgain.upper() == "Y":
				return True
			elif playAgain.upper() == "N":
				return False
			print("Invalid input. Please try again.")



	def _draw_box(self, image, rect, xloc, yloc):
		xloc *= 205
		yloc *= 205
		rect.move_ip(xloc, yloc)
		self.screen.blit(image, rect)
		rect.move_ip(-xloc, -yloc)
		pygame.display.update()



	def _game_loop(self):
		gameOver = False
		if random.randint(0, 1) == 0:
			self.turn = 'X'
		else:
			self.turn = 'O'

		while not gameOver:
			if self.turn == 'X':
				self._player_turn()
			else:
				self._computer_turn()

			gameOver = self._check_for_game_over()
			if gameOver:
				self._display_winner()
			else:
				if self.turn == 'X':
					self.turn = 'O'
				else:
					self.turn = 'X'




	def _player_turn(self):
		validSelection = False

		while not validSelection:
			selection = self._player_selection()
			validSelection = self._validate_selection(selection)
			if validSelection:
				self._finalize_selection(selection)		



	def _player_selection(self):
		while True:
			for event in pygame.event.get():
				# If player exits...
				if event.type == QUIT:
					sys.exit()
				# If mouse is clicked...
				elif event.type == MOUSEBUTTONDOWN:
					# Read in mouse position
					x, y = pygame.mouse.get_pos()

					# Determine which box was clicked
					for i in range(3):
						finished = False
						for j in range(3):
							if x < (200 + (205 * i)) and y < (200 + (205 * j)):
								return i, j



	def _validate_selection(self, selection):
		i, j = selection

		return self.board[i][j] == None



	def _finalize_selection(self, selection):
		i, j = selection

		self.board[i][j] = self.turn

		if self.turn == 'X':
			image = self.x
			rect = self.xRect
		else:
			image = self.o
			rect = self.oRect

		self._draw_box(image, rect, i, j)



	def _computer_turn(self):
		validSelection = False

		while not validSelection:
			selection = self._randomize_selection()
			validSelection = self._validate_selection(selection)
			if validSelection:
				self._finalize_selection(selection)



	def _randomize_selection(self):
		i = random.randint(0,2)
		j = random.randint(0,2)
		return i, j



	def _check_for_game_over(self):
		if not self._check_for_winner():
			for i in range(3):
				for j in range(3):
					if self.board[i][j] == None:
						return False
		return True



	def _check_for_winner(self):
		for i in range(3):
			for j in range(3):
				if self.board[i][j] == self.turn:
					if self._check_spot_for_win(i, j):
						return True
		return False



	def _check_spot_for_win(self, i, j):
		return self._check_for_horizontal_win(i) or self._check_for_vertical_win(j) or self._check_for_diagonal_win(i, j)



	def _check_for_horizontal_win(self, i):
		win = True
		for j in range(3):
			if self.board[i][j] != self.turn:
				win = False
				break
		if win:
			return True



	def _check_for_vertical_win(self, j):
		win = True
		for i in range(3):
			if self.board[i][j] != self.turn:
				win = False
				break
		if win:
			return True



	def _check_for_diagonal_win(self, i, j):
		diagonals = [(0, 0), (1, 1), (2, 2), (0, 2), (2, 0)]

		if (i, j) in diagonals:
			win = True
			for i in range(3):
				if self.board[i][i] != self.turn:
					win = False
					break
			if win:
				return True

			win = True
			for i in range(3):
				for j in range(2, -1, -1):
					if self.board[i][i] != self.turn:
						win = False
						break
			if win:
				return True

		return False


	def _display_winner(self):
		pass