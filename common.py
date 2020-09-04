import pygame

BLACK = 0, 0, 0
WHITE = 255, 255, 255
GREEN = 0, 255, 0
RED = 255, 0, 0
GRAY = 169, 169, 169

def read_in_mouse_click():
		while True:
			for event in pygame.event.get():
				# If player exits...
				if event.type == pygame.QUIT:
					sys.exit()
				# If mouse is clicked...
				elif event.type == pygame.MOUSEBUTTONDOWN:
					return pygame.mouse.get_pos()