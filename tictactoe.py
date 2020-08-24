import random

class TicTacToe:
	def __init__(self):
		self.start_new_game()


	def start_new_game(self):
		while True:
			self.gameOver = False
			self.winner = 0
			self.boxes = []
			self.availableBoxes = []
			self.rows = []
			turn = 0

			# Initialize random seed
			random.seed()

			for i in range(9):
				self.availableBoxes.append(True)
				self.boxes.append(0)

			self.initialize_board()
			while not self.gameOver:
				if turn % 2 == 0:
					self.player_turn()
				else:
					self.computer_turn()
				turn += 1
			self.display_winner()

			# Prompt user to play again
			playAgain = input("Would you like to play again? (Y/N): ")

			while playAgain.upper() != 'Y' and playAgain.upper() != 'N':
				print("Invalid input.")
				playAgain = input("Would you like to play again? (Y/N): ")

			if playAgain.upper() == 'N':
				break


	def initialize_board(self):
		for i in range(0, 11):
			if i == 3 or i == 7:
				self.rows.append("-----------")
			elif i == 1:
				self.rows.append(" 1 | 2 | 3 ")
			elif i == 5:
				self.rows.append(" 4 | 5 | 6 ")
			elif i == 9:
				self.rows.append(" 7 | 8 | 9 ")
			else:
				self.rows.append("   |   |   ")

		self.print_board()


	def player_turn(self):
		PLAYER_NUMBER = 1

		hasSucceeded = False
		while not hasSucceeded:
			try:
				# Read in player selection
				selection = eval(input("Select a box: "))

				# Validate input
				while not self.availableBoxes[selection- 1]:
					print ("Invalid selection.")
					selection = eval(input("Select a box: "))

				# Set hasSucceeded boolean to true so we can exit loop
				hasSucceeded = True
			except:
				print ("Error: Invalid input.")

		# Adjust selection to appropriate box
		selection -= 1

		self.update_board(selection, PLAYER_NUMBER)
		self.print_board()
		self.check_for_winner(selection, PLAYER_NUMBER)


	def computer_turn(self):
		PLAYER_NUMBER = 2

		# Randomize selection
		selection = random.randint(0, 8)

		while not self.availableBoxes[selection]:
			selection = random.randint(0, 8)

		self.update_board(selection, PLAYER_NUMBER)
		self.print_board()
		self.check_for_winner(selection, PLAYER_NUMBER)


	def update_board(self, selection, player):
		lines = []
		if player == 1:
			lines.append("\\ /")
			lines.append(" X ")
			lines.append("/ \\")
		else:
			lines.append("+-+")
			lines.append("| |")
			lines.append("+-+")

		# Find starting row of selection
		startingRow = 0
		if selection // 3 == 1:
			startingRow = 4
		elif selection // 3 == 2:
			startingRow = 8

		# Find starting column of selection
		startingColumn = 0
		if selection % 3 == 1:
			startingColumn = 4
		elif selection % 3 == 2:
			startingColumn = 8

		# Update selection on board
		for i in range(3):
			self.rows[startingRow + i] = self.rows[startingRow + i][0:startingColumn] + lines[i] + self.rows[startingRow + i][startingColumn + 3:]

		# Set selection as unavailable
		self.boxes[selection] = player
		self.availableBoxes[selection] = False



	def print_board(self):
		print()
		for row in self.rows:
			print(row)
		print()


	def check_for_winner(self, selection, player):
		if selection == 0:
			if (self.boxes[1] == player and self.boxes[2] == player) or (self.boxes[4] == player and self.boxes[8] == player) or (self.boxes[3] == player and self.boxes[6] == player):
				self.gameOver = True
		elif selection == 1:
			if (self.boxes[0] == player and self.boxes[2] == player) or (self.boxes[4] == player and self.boxes[7] == player):
				self.gameOver = True
		elif selection == 2:
			if (self.boxes[0] == player and self.boxes[1] == player) or (self.boxes[4] == player and self.boxes[6] == player) or (self.boxes[5] == player and self.boxes[8] == player):
				self.gameOver = True
		elif selection == 3:
			if (self.boxes[0] == player and self.boxes[6] == player) or (self.boxes[4] == player and self.boxes[5] == player):
				self.gameOver = True
		elif selection == 4:
			if (self.boxes[0] == player and self.boxes[8] == player) or (self.boxes[3] == player and self.boxes[5] == player) or (self.boxes[6] == player and self.boxes[2] == player) or (self.boxes[1] == player and self.boxes[7] == player):
				self.gameOver = True
		elif selection == 5:
			if (self.boxes[2] == player and self.boxes[8] == player) or (self.boxes[3] == player and self.boxes[4] == player):
				self.gameOver = True
		elif selection == 6:
			if (self.boxes[0] == player and self.boxes[3] == player) or (self.boxes[4] == player and self.boxes[2] == player) or (self.boxes[7] == player and self.boxes[8] == player):
				self.gameOver = True
		elif selection == 7:
			if (self.boxes[1] == player and self.boxes[4] == player) or (self.boxes[6] == player and self.boxes[8] == player):
				self.gameOver = True
		elif selection == 8:
			if (self.boxes[0] == player and self.boxes[4] == player) or (self.boxes[2] == player and self.boxes[5] == player) or (self.boxes[6] == player and self.boxes[7] == player):
				self.gameOver = True

		if self.gameOver:
			self.winner = player
		else:
			# Check for full board
			self.gameOver = True
			for box in self.boxes:
				if box == 0:
					self.gameOver = False
					break


	def display_winner(self):
		if self.winner == 1:
			print("YOU WON!")
		elif self.winner == 2:
			print("YOU LOST!")
		else:
			print("It's a draw.")