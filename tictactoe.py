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
			self.emptyRect.move_ip(i * 205, 0)
			for j in range(3):
				self.emptyRect.move_ip(0, j * 205)
				self.screen.blit(self.empty, self.emptyRect)
				pygame.display.update()
				self.emptyRect.move_ip(0, j * (-205))

			self.emptyRect.move_ip(i * (-205), 0)

	def _main_loop(self):
		clock = pygame.time.Clock()
		while True:
			clock.tick(60)

			for event in pygame.event.get():
				if event.type == QUIT:
					return
				elif event.type == MOUSEBUTTONDOWN:
					print(pygame.mouse.get_pos)