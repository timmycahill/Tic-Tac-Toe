import pygame, common

class Button:
	def __init__(self, text, textSize=25, dimensions=(100,50), bgColor=common.GRAY, textColor=common.BLACK):
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

		# Blit text to button
		self.button.blit(textObj, (textX, textY))

	def get_button(self):
		return self.button

	def get_width(self):
		return self.button.get_width()

	def get_height(self):
		return self.button.get_height()