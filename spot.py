import pygame, player

SPOT_DIMENSIONS = SPOT_WIDTH, SPOT_HEIGHT = 200, 200
TEXT_COLOR = (0,0,0)
TEXT_SIZE = int(SPOT_HEIGHT * 0.8)

class Spot:
	def __init__(self, color=(255,255,255)):
		# Create surface for spot
		self.spot = pygame.Surface(SPOT_DIMENSIONS)
		self.spot.fill(color)

		# Mark spot as not taken
		self.isTaken = False

	def is_taken(self):
		return self.isTaken

	def take_spot(self, plyr):
		# Check if spot is already taken
		if self.isTaken():
			return False
		else:	
			# Create spot text
			font = pygame.font.SysFont(None, TEXT_SIZE)
			self.symbol = font.render(plyr.get_symbol(), True, TEXT_COLOR)

			# Center text in spot
			textWidth, textHeight = font.size(playerSymbol)
			self.textX = (SPOT_WIDTH - textWidth) // 2
			self.textY = (SPOT_HEIGHT - textHeight) // 2

			# Blit text to button
			self.spot.blit(self.symbol, (self.textX, self.textY))

			# Mark spot as taken
			self.isTaken = True
			return True

	def change_color(self, color):
		# Fill spot with new color
		self.spot.fill(color)

		# If spot is taken, reprint symbol in spot
		self._reprint_symbol()

	def _reprint_symbol(self):
		self.spot.blit(self.symbol, (self.textX, self.textY))

	def get_spot(self):
		return self.spot

	def get_player_symbol(self):
		return self.symbol