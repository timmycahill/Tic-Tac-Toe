import pygame, game, common, board
from displaybox import *

SIZE = WIDTH, HEIGHT = game.SIZE
DISPLAY_BOX_POS = (0, board.HEIGHT)

class MainMenu:
	def __init__(self):
		self.screen = pygame.Surface(SIZE)
		self._create_menu()


	def _create_menu(self):
		# Clear screen
		self.screen.fill(common.BLACK)

		# Print menu to screen
		self._print_menu_title()
		self._print_menu_image()

		# Print display box with buttons
		self.displayBox = DisplayBox(Presets.MAIN_MENU)
		self.screen.blit(displayBox.get_box(), DISPLAY_BOX_POS)



	def _print_menu_title(self):
		# Display game title
		font = pygame.font.SysFont(None, 100)
		text = font.render("TicTacToe", True, common.WHITE)
		textWidth, textHeight = font.size("TicTacToe")

		# Get x,y coordinates
		textX = (WIDTH - textWidth) // 2
		textY = (HEIGHT - textHeight) // 7

		# Print to screen
		self.screen.blit(text, (textX, textY))


	def _print_menu_image(self):
		# Load in menu image
		menuImage = pygame.image.load("resources/images/menuImage.png")
		menuImageRect = menuImage.get_rect()

		# Move menu image to desired location
		x = (WIDTH - menuImageRect.width) // 2
		y = (HEIGHT - menuImageRect.height) // 2
		menuImageRect.move_ip(x, y)

		# Blit and print menu image to screen
		self.screen.blit(menuImage, menuImageRect)


	def get_selection(self):
		buttons = self.displaybox.get_buttons()
		common.read_in_mouse_click()
		

	def get_menu(self):
		return self.screen