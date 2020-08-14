#include <iostream>
#include <stdlib.h>
#include <time.h>
#include "game.h"

using namespace std;

Game::Game() {
	gameOver = false;
	turn = 0;
	winner = 0;

	// Initialize random seed
	srand(time(NULL));

	for (int i = 0; i < 9; i++) {
		availableBoxes[i] = true;
		boxes[i] = 0;
	}

	initialize_board();
	while (!gameOver) {
		switch (turn % 2) {
			case 0:
				player_turn();
				break;
			case 1:
				computer_turn();
				break;
		}
		turn++;
	}
	display_winner();
}

void Game::initialize_board() {
	for (int i = 0; i < 11; i++) {
		if (i == 3 || i == 7) {
			rows[i] = "-----------";
		}
		else if (i == 1) {
			rows[i] = " 1 | 2 | 3 ";
		}
		else if (i == 5) {
			rows[i] = " 4 | 5 | 6 ";
		}
		else if (i == 9) {
			rows[i] = " 7 | 8 | 9 ";
		}
		else {
			rows[i] = "   |   |   ";
		}
	}

	print_board();
}

void Game::player_turn() {
	const int PLAYER_NUMBER = 1;

	// Read in player selection
	cout << "Select a box: ";
	int selection;
	cin >> selection;

	// Validate input
	while (!cin || selection > 9 || selection < 1 || !availableBoxes[selection - 1]) {
		// Reset stream
		cin.clear();
		cin.ignore(1000, '\n');

		// Output error message
		cout << "Invalid Selection" << endl;

		// Prompt user to re-enter selection
		cout << "Select a box: ";
		cin >> selection;
	}

	// Update board and print to screen
	update_board(selection, PLAYER_NUMBER);
	cout << "\n\n\n";
	print_board();
	check_for_winner(selection, PLAYER_NUMBER);
}

void Game::computer_turn() {
	const int PLAYER_NUMBER = 2;

	// Randomize Selection
	int selection = (rand() % 9) + 1;

	while (!availableBoxes[selection - 1]) {
		// Randomize Selection
		selection = (rand() % 9) + 1;
	}

	// Update board and print to screen
	update_board(selection, PLAYER_NUMBER);
	cout << "\n\n\n";
	print_board();
	check_for_winner(selection, PLAYER_NUMBER);
}

void Game::update_board(int selection, int player) {
	// Set X or O depending on player
	string lines[3];

	switch (player) {
		case 1:
			lines[0] = "\\ /";
			lines[1] = " X ";
			lines[2] = "/ \\";
			break;
		case 2:
			lines[0] = "+-+";
			lines[1] = "| |";
			lines[2] = "+-+";
			break;
	}

	// Adjust selection to appropriate box
	int box = selection - 1;
	
	// Find row of selection
	int startingRow = 0;
	if (box / 3 == 1) {
		startingRow = 4;
	}
	else if (box / 3 == 2) {
		startingRow = 8;
	}

	// Find column of selection
	int columnStart = 0;
	if (box % 3 == 1) {
		columnStart = 4;
	}
	else if (box % 3 == 2) {
		columnStart = 8;
	}
	
	// Update selection on board
	for (int i = 0; i < 3; i++) {
		rows[startingRow + i] = rows[startingRow + i].substr(0, columnStart) + lines[i] + rows[startingRow + i].substr(columnStart + 3);
	}

	// Set selection as unavailable
	boxes[selection - 1] = player;
	availableBoxes[selection - 1] = false;
}

void Game::check_for_winner(int selection, const int PLAYER) {
	switch (selection - 1) {
		case 0:
			if ( (boxes[1] == PLAYER && boxes[2] == PLAYER) ||
				(boxes[4] == PLAYER && boxes[8] == PLAYER) ||
				(boxes[3] == PLAYER && boxes[6] == PLAYER) ) {
				gameOver = true;
				winner = PLAYER;
			}
			break;
		case 1:
			if ((boxes[0] == PLAYER && boxes[2] == PLAYER) ||
				(boxes[4] == PLAYER && boxes[7] == PLAYER)) {
				gameOver = true;
				winner = PLAYER;
			}
			break;
		case 2:
			if ((boxes[0] == PLAYER && boxes[1] == PLAYER) ||
				(boxes[6] == PLAYER && boxes[4] == PLAYER) ||
				(boxes[5] == PLAYER && boxes[8] == PLAYER)) {
				gameOver = true;
				winner = PLAYER;
			}
			break;
		case 3:
			if ((boxes[0] == PLAYER && boxes[6] == PLAYER) ||
				(boxes[4] == PLAYER && boxes[5] == PLAYER)) {
				gameOver = true;
				winner = PLAYER;
			}
			break;
		case 4:
			if ((boxes[0] == PLAYER && boxes[8] == PLAYER) ||
				(boxes[3] == PLAYER && boxes[5] == PLAYER) ||
				(boxes[6] == PLAYER && boxes[2] == PLAYER) ||
				(boxes[1] == PLAYER && boxes[7] == PLAYER)) {
				gameOver = true;
				winner = PLAYER;
			}
			break;
		case 5:
			if ((boxes[2] == PLAYER && boxes[8] == PLAYER) ||
				(boxes[3] == PLAYER && boxes[4] == PLAYER)) {
				gameOver = true;
				winner = PLAYER;
			}
			break;
		case 6:
			if ((boxes[0] == PLAYER && boxes[3] == PLAYER) ||
				(boxes[4] == PLAYER && boxes[2] == PLAYER) ||
				(boxes[7] == PLAYER && boxes[8] == PLAYER)) {
				gameOver = true;
				winner = PLAYER;
			}
			break;
		case 7:
			if ((boxes[1] == PLAYER && boxes[4] == PLAYER) ||
				(boxes[6] == PLAYER && boxes[8] == PLAYER)) {
				gameOver = true;
				winner = PLAYER;
			}
			break;
		case 8:
			if ((boxes[0] == PLAYER && boxes[4] == PLAYER) ||
				(boxes[2] == PLAYER && boxes[5] == PLAYER) ||
				(boxes[6] == PLAYER && boxes[7] == PLAYER)) {
				gameOver = true;
				winner = PLAYER;
			}
			break;
	}

	// Check for full board
	if (!gameOver) {
		gameOver = true;
		for (int i = 0; i < 9; i++) {
			if (boxes[i] == 0) {
				gameOver = false;
				break;
			}
		}
	}
}

void Game::print_board() {
	for (int i = 0; i < 11; i++) {
		cout << rows[i] << endl;
	}
	cout << "\n\n\n";
}

void Game::display_winner() {
	if (winner == 1) {
		cout << "YOU WIN!!!!" << endl;
	}
	else if (winner == 2) {
		cout << "YOU LOSE!!!" << endl;
	}
	else {
		cout << "ITS A DRAW!!!" << endl;
	}
}