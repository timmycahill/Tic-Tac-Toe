import pygame, random, sys
from pygame.locals import *

WINDOW_SIZE = (610, 610)
BLACK = 0, 0, 0
WHITE = 255, 255, 255

class TicTacToe:
	def __init__(self):
		pygame.init()
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


	def _main_loop(self):
		while True:
			self._game_loop()
			if not self._play_again():
				break

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
			self.turn = 'x'
		else:
			self.turn = 'o'

		while not gameOver:
			if self.turn == 'x':
				self._player_turn()
				self.turn = 'o'
			else:
				self._computer_turn()
				self.turn = 'x'
			self._check_for_winner()

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
		x, y = selection

		return self.board[x][y] == None

	def _finalize_selection(self, selection):
		x, y = selection

		self.board[x][y] = self.turn

		if self.turn == 'x':
			image = self.x
			rect = self.xRect
		else:
			image = self.o
			rect = self.oRect

		self._draw_box(image, rect, x, y)

	def _computer_turn(self):
		validSelection = False

		while not validSelection:
			selection = self._randomize_selection()
			validSelection = self._validate_selection(selection)
			if validSelection:
				self._finalize_selection(selection)

	def _randomize_selection(self):
		x = random.randint(0,2)
		y = random.randint(0,2)
		return x, y

	def _check_for_winner(self):
		pass