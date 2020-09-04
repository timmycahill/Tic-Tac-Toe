import pygame
from pygame.locals import *
from menucontroller import MenuController
from gamecontroller import GameController

# Set window size
WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = 610, 710

# Set color rgb constants
BLACK = 0,0,0
WHITE = 255,255,255
GREEN = 0,255,0
RED = 255,0,0
GRAY = 105,105,105

pygame.init()


####################################################
##  View Class                                    ##
####################################################

class View:
	def __init__(self):
		# Create controller objects
		self.menuController = MenuController()
		self.gameController = GameController()

		# Create display window
		self.display = pygame.display.set_mode(WINDOW_SIZE)		


	def run(self):
		self.menu()


	def menu(self):
		# Fill screen with a black background
		self.display.fill(BLACK)

		# Draw resources
		self._draw_title()
		self._draw_image()
		self._draw_buttons()

		# Update Screen
		pygame.display.update()

		# Wait for user input
		self._read_in_mouse_click()



	def _draw_title(self):
		# Get title from controller
		title = self.menuController.get_title()

		# Create title font object
		font = pygame.font.SysFont("font", 100)
		text = font.render(title, True, WHITE)

		# Position on screen
		width, height = font.size(title)
		x = (WINDOW_WIDTH - width) // 2
		y = (WINDOW_HEIGHT -height) // 8

		# Blit to screen
		self.display.blit(text, (x, y))

	def _draw_image(self):
		# Get image path from controller
		path = self.menuController.get_image_path()

		# Create image object
		image = pygame.image.load(path)

		# Position on screen
		width, height = image.get_size()
		x = (WINDOW_WIDTH - width) // 2
		y = (WINDOW_HEIGHT -height) // 2

		# Blit to screen
		self.display.blit(image, (x, y))


	def _draw_buttons(self):
		# Create play button
		playButton = Button("Play").get_surface()

		# Position on screen
		width, height = playButton.get_size()
		x = ((WINDOW_WIDTH // 2) - width) // 2
		y = WINDOW_HEIGHT - (WINDOW_HEIGHT // 5) + height

		# Blit to screen
		self.display.blit(playButton, (x, y))


		# Create Quit button
		quitButton = Button("Quit").get_surface()

		# Position on screen
		x = (WINDOW_WIDTH // 2) + ((WINDOW_WIDTH // 2) - width) // 2

		# Blit to screen
		self.display.blit(quitButton, (x, y))


	def _read_in_mouse_click(self):
		while True:
			for event in pygame.event.get():
				# If player exits...
				if event.type == QUIT:
					sys.exit()
				# If mouse is clicked...
				elif event.type == MOUSEBUTTONDOWN:
					return pygame.mouse.get_pos()



####################################################
##  Button Class                                  ##
####################################################

class Button:
	def __init__(self, text, textSize=25, dimensions=(100,50), bgColor=GRAY, textColor=BLACK):
		# Create button surface
		self.button = pygame.Surface(dimensions)
		self.button.fill(bgColor)

		# Create button text
		font = pygame.font.SysFont(None, textSize)
		textObj = font.render(text, True, textColor)

		# Center text in button
		textWidth, textHeight = font.size(text)
		buttonWidth, buttonHeight = self.button.get_size()
		textX = (buttonWidth - textWidth) // 2
		textY = (buttonHeight - textHeight) // 2

		# Print text to surface
		self.button.blit(textObj, (textX, textY))


	def get_surface(self):
		return self.button