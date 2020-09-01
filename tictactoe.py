import pygame, random, sys
from pygame.locals import *

WINDOW_SIZE = WINDOW_X, WINDOW_Y = 610, 710
TEXTBOX_LOCATION = TEXTBOX_X, TEXTBOX_Y = 0, 610
TEXTBOX_DIMENSIONS = TEXTBOX_WIDTH, TEXTBOX_HEIGHT = 610, 100
BLACK = 0, 0, 0
WHITE = 255, 255, 255

class TicTacToe:

	def __init__(self):
		pygame.init()
		self.font = pygame.font.SysFont(None, 50)
		random.seed()
		self.playerWins = 0
		self.computerWins = 0
		self._load_in_resources()
		self._initialize_window()
		self._initialize_board()
		self._initialize_music()
		self._main_loop()



	def _initialize_music(self):
		pygame.mixer.music.load("resources/music/music.mp3")
		pygame.mixer.music.play(loops=-1)



	def _load_in_resources(self):
		self.empty = pygame.image.load("resources/images/empty.png")
		self.emptyRect = self.empty.get_rect()
		self.x = pygame.image.load("resources/images/x.png")
		self.xRect = self.x.get_rect()
		self.o = pygame.image.load("resources/images/o.png")
		self.oRect = self.o.get_rect()



	def _initialize_window(self):
		self.screen = pygame.display.set_mode(WINDOW_SIZE)
		self.textbox = self.screen.subsurface(Rect(TEXTBOX_LOCATION, TEXTBOX_DIMENSIONS))
		self._reset_board()




	def _initialize_board(self):
		self.board = []
		self.tie = False
		for i in range(3):
			self.board.append([None] * 3)



	def _increment_win_count(self):
		if not self.tie:
			if self.turn == 'X':
				self.playerWins += 1
			else:
				self.computerWins += 1



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
			self._wait_for_click()
			if not self._play_again():
				break
			self._reset_game()



	def _play_again(self):
		self._clear_text_box()
		self._display_play_again_text()
		return self._read_in_play_again()



	def _read_in_play_again(self):
		while True:
			x, y = self._read_in_mouse_click_loc()

			if x < TEXTBOX_WIDTH // 2 and y > TEXTBOX_Y + (TEXTBOX_HEIGHT // 2):
				return True
			elif x > TEXTBOX_WIDTH // 2 and y > TEXTBOX_Y + (TEXTBOX_HEIGHT // 2):
				return False



	def _read_in_mouse_click_loc(self):
		while True:
			for event in pygame.event.get():
				# If player exits...
				if event.type == QUIT:
					sys.exit()
				# If mouse is clicked...
				elif event.type == MOUSEBUTTONDOWN:
					return pygame.mouse.get_pos()



	def _clear_text_box(self):
		self.textbox.fill(BLACK)
		pygame.display.update()



	def _display_play_again_text(self):
		self._draw_play_again_text()
		self._draw_yes_text()
		self._draw_no_text()



	def _draw_play_again_text(self):
		text = self.font.render("Play again?", True, WHITE)
		x, y = self.font.size("Play again?")

		textX = (WINDOW_X - x) // 2
		textY = TEXTBOX_Y + (((TEXTBOX_HEIGHT // 2) - y) // 2)

		self.screen.blit(text, (textX, textY))
		pygame.display.update()



	def _draw_yes_text(self):
		text = self.font.render("Yes", True, WHITE)
		x, y = self.font.size("Yes")

		textX = ((WINDOW_X // 2) - x) // 2
		textY = TEXTBOX_Y + (TEXTBOX_HEIGHT // 2) + (((TEXTBOX_HEIGHT // 2) - y) // 2)

		self.screen.blit(text, (textX, textY))
		pygame.display.update()



	def _draw_no_text(self):
		text = self.font.render("No", True, WHITE)
		x, y = self.font.size("No")

		textX = (WINDOW_X // 2) + (((WINDOW_X // 2) - x) // 2)
		textY = TEXTBOX_Y + (TEXTBOX_HEIGHT // 2) + (((TEXTBOX_HEIGHT // 2) - y) // 2)

		self.screen.blit(text, (textX, textY))
		pygame.display.update()



	def _wait_for_click(self):
		self._read_in_mouse_click_loc()



	def _draw_box(self, image, rect, xloc, yloc):
		xloc *= 205
		yloc *= 205
		rect.move_ip(xloc, yloc)
		self.screen.blit(image, rect)
		rect.move_ip(-xloc, -yloc)
		pygame.display.update()



	def _game_loop(self):
		# Display win count to screen
		self._display_wins()

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
				self._increment_win_count()
			else:
				if self.turn == 'X':
					self.turn = 'O'
				else:
					self.turn = 'X'



	def _display_wins(self):
		self._clear_text_box()
		self._draw_player_wins()
		self._draw_computer_wins()


	def _draw_player_wins(self):
		# Draw player text
		text = self.font.render("Player: ", True, WHITE)
		x, y = self.font.size("Player: ")

		textX = (WINDOW_X // 2) - x
		textY = TEXTBOX_Y + (((TEXTBOX_HEIGHT // 2) - y) // 2)

		self.screen.blit(text, (textX, textY))

		# Draw win count text
		text = self.font.render(str(self.playerWins), True, WHITE)
		x, y = self.font.size(str(self.playerWins))

		textX = WINDOW_X // 2
		textY = TEXTBOX_Y + (((TEXTBOX_HEIGHT // 2) - y) // 2)

		self.screen.blit(text, (textX, textY))

		# Update screen
		pygame.display.update()


	def _draw_computer_wins(self):
		# Draw computer text
		text = self.font.render("Computer: ", True, WHITE)
		x, y = self.font.size("Computer: ")

		textX = (WINDOW_X // 2) - x
		textY = TEXTBOX_Y + (TEXTBOX_HEIGHT // 2) + (((TEXTBOX_HEIGHT // 2) - y) // 2)

		self.screen.blit(text, (textX, textY))

		# Draw win count text
		text = self.font.render(str(self.computerWins), True, WHITE)
		x, y = self.font.size(str(self.computerWins))

		textX = WINDOW_X // 2
		textY = TEXTBOX_Y + (TEXTBOX_HEIGHT // 2) + (((TEXTBOX_HEIGHT // 2) - y) // 2)

		self.screen.blit(text, (textX, textY))

		# Update screen
		pygame.display.update()





	def _player_turn(self):
		validSelection = False

		while not validSelection:
			selection = self._player_selection()
			validSelection = self._validate_selection(selection)
			if validSelection:
				self._finalize_selection(selection)		



	def _player_selection(self):
		while True:
			x, y = self._read_in_mouse_click_loc()
			
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
		# Add delay to make move more natural
		pygame.time.delay(333)

		# Make move
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
			self.tie = True
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
			j = 2
			for i in range(3):
				if self.board[i][j] != self.turn:
					win = False
					break
				j -= 1
			return win
		return False


	def _display_winner(self):
		self._clear_text_box()
		message = self._generate_winner_message()
		self._display_winner_message(message)



	def _generate_winner_message(self):
		if self.tie:
			message = "It's a Tie!"
		else:
			message = self.turn + " WINS!"

		return message



	def _display_winner_message(self, message):
		text = self.font.render(message, True, WHITE)
		x, y = self.font.size(message)

		textX = (WINDOW_X - x) // 2
		textY = TEXTBOX_Y + ((TEXTBOX_HEIGHT - y) // 2)

		self.screen.blit(text, (textX, textY))
		pygame.display.update()