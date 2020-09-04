import pygame, sys, board, player, displaybox, random
from pygame.locals import *
from displaybox import *

SIZE = WIDTH, HEIGHT = board.WIDTH, (board.HEIGHT + displaybox.HEIGHT)

import menu

pygame.init()
random.seed()

class Game:

	def __init__(self):
		self.screen = pygame.display.set_mode(SIZE)
		self._initialize_music()

	def _initialize_music(self):
		pygame.mixer.music.load("resources/music/music.mp3")
		pygame.mixer.music.play(loops=-1)

	def run(self):



		while True:
			mainMenu = menu.MainMenu()
			self.screen.blit(mainMenu.get_menu(), (0, 0))
			pygame.display.update()

			

			selection = mainMenu.get_selection()


			if selection == "Play":
				# Create players
				self._game_loop()
			else:
				sys.exit()

	def _game_loop(self):
		# Create players
		players = [player.User(), player.Bot()]

		# Initialize game board
		gameBoard = board.Board()
		scoreDisplay = DisplayBox(Presets.SCORE, players=players)
		
		# Randomize who goes first
		turn = random.randrange(0,2)

		while True:
			# Mod turn so it is always one of the players
			turn %= 2

			# Read in player selection
			row, column = players[turn].get_selection()

			# Validate selection
			while not board.take_spot(row, column, player[turn]):
				# Read in player selection
				row, column = players[turn].get_selection()

			# Check for game over
			if gameBoard.is_game_over():
				winner = gameBoard.get_winner()

				# Display winner
				winnerDisplay = DisplayBox(Presets.WINNER, winner=players[winner])


				# Update score
				for plyr in players:
					if plyr.get_symbol() == winner:
						plyr.win()
						break

				# Play again?

			# Next turn
			else:
				turn += 1