import pygame, board, player, button, common
from enum import Enum

SIZE = WIDTH, HEIGHT = board.WIDTH, 100
TEXT_SIZE = 50

Presets = Enum('Presets', 'MAIN_MENU SCORE WINNER PLAY_AGAIN')

class DisplayBox:
	def __init__(self, preset, players=None, winner=None):
		# Create surface
		self.display = pygame.Surface(SIZE)

		# Initialize variables
		self.buttons = []
		self.players = players
		self.winner = winner
	
		# Load in preset
		# MAIN_MENU
		if preset == Presets.MAIN_MENU:
			self._main_menu()
		# SCORE
		elif preset == Presets.SCORE:
			self._score()
		# WINNER
		elif preset == Presets.WINNER:
			self._winner()
		# PLAY_AGAIN
		elif preset == Presets.PLAY_AGAIN:
			self._play_again()
		# Default
		else:
			self.display.fill(game.BLACK)


	def get_box(self):
		return self.display


	def _main_menu(self):
		# Clear surface
		self.display.fill(common.BLACK)

		# Create buttons
		buttonList = ["Play", "Quit"]
		for buttonName in buttonList:
			self.buttons.append(button.Button(buttonName))

		# Print buttons
		for i in range(len(self.buttons)):
			# Get button position
			sectionWidth = WIDTH // len(self.buttons)
			x = (i * sectionWidth) + ((sectionWidth - self.buttons[i].get_width()) // 2)
			y = (HEIGHT - self.buttons[i].get_height()) // 2

			# Blit button to surface
			self.display.blit(self.buttons[i].get_button(), (x, y))

		# Update screen
		pygame.display.update()


	def _score(self):
		# Clear surface
		self.display.fill(common.BLACK)

		# Print score rows
		for i in len(players):
			self._print_score_row(i, players[i])
		
		# Update screen
		pygame.display.update()


	def _print_score_row(self, row, plyr):
		# Print name
		font = pygame.font.SysFont(None, TEXT_SIZE)
		text = font.render(plyr.get_name() + ': ', True, common.WHITE)

		textWidth, textHeight = font.size(plyr.get_name() + ': ')
		rowHeight = HEIGHT // 2
		x = (WIDTH // 2) - textWidth
		y = (rowHeight * row) + ((rowHeight - textHeight) // 2)

		self.display.blit(text, (x, y))

		# Print win count
		text = font.render(str(plyr.get_wins()), True, common.WHITE)
		textWidth, textHeight = font.size(str(plyr.get_wins()))

		x = WIDTH // 2
		y = (rowHeight * row) + ((rowHeight - textHeight) // 2)

		self.display.blit(text, (x, y))


	def _winner(self):
		# Clear surface
		self.display.fill(common.BLACK)

		# Create winner message
		if self.winner == None:
			message = "It's a tie!"
		else:
			message = self.winner.get_symbol() + ' WINS!'

		# Print winner message
		font = pygame.font.SysFont(None, TEXT_SIZE)
		text = font.render(message, True, common.WHITE)

		textWidth, textHeight = font.size(message)
		x = (WIDTH - textWidth) // 2
		y = (HEIGHT - textHeight) // 2

		self.display.blit(text, (x, y))

		# Update screen
		pygame.display.update()


	def _play_again(self):
		# Clear surface
		self.display.fill(common.BLACK)

		# Print assets
		self._print_play_again_text()
		self._create_play_again_buttons()

		# Update screen
		pygame.display.update()


	def _print_play_again_text(self):
		message = "Play again?"
		font = pygame.font.SysFont(None, TEXT_SIZE)
		text = font.render(message, True, common.WHITE)

		textWidth, textHeight = font.size(message)
		x = (WIDTH - textWidth) // 2
		y = ((HEIGHT // 2) - textHeight) // 2

		self.display.blit(text, (x, y))



	def _create_play_again_buttons(self):
		# Create buttons
		buttonList = ["Yes", "No"]
		for buttonName in buttonList:
			self.buttons.append(button.Button(buttonName))

		# Print buttons
		for i in range(len(buttons)):
			# Get button position
			sectionWidth = WIDTH // len(buttons)
			sectionHeight = HEIGHT // 2
			x = (i * sectionWidth) + ((sectionWidth - buttons[i].get_length) // 2)
			y = sectionHeight + (sectionHeight - buttons[i].get_height()) // 2

			# Blit button to surface
			self.display.blit(buttons[i].get_button(), (x, y))

	def get_buttons(self):
		return self.buttons