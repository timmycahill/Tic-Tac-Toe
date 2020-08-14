#ifndef GAME_H
#define GAME_H

#include <string>

using namespace std;

class Game {
	public:
		/// <summary>
		/// Creates a game object which automatically starts and simulates one game of tic-tac-toe.
		/// </summary>
		Game();

	private:
		bool gameOver;
		short turn;
		string rows[11];
		int boxes[9];
		bool availableBoxes[9];
		int winner;

		/// <summary>
		/// Creates an empty playing field and displays it to the screen.
		/// </summary>
		void initialize_board();

		/// <summary>
		/// Simulates the player's turn and prints the updated playing field to the screen.
		/// </summary>
		void player_turn();

		/// <summary>
		/// Simulates the computer's turn and prints the updated playing field to the screen.
		/// </summary>
		void computer_turn();

		/// <summary>
		/// Updates the playing field with the most recent move by the most recent player.
		/// </summary>
		/// <param name="selection"></param>
		/// <param name="player"></param>
		void update_board(int selection, int player);

		/// <summary>
		/// Checks field against most recent move to see if the game is over.
		/// </summary>
		/// <param name="selection"></param>
		/// <param name="player"></param>
		void print_board();

		/// <summary>
		/// Prints the playing field to the screen.
		/// </summary>
		void check_for_winner(int selection, int player);

		/// <summary>
		/// Displays the results of the game to the screen.
		/// </summary>
		void display_winner();
};

#endif