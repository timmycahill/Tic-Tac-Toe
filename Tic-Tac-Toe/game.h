#ifndef GAME_H
#define GAME_H

#include <string>

using namespace std;

class Game {
	public:
		Game();

	private:
		bool gameOver;
		short turn;
		string rows[11];
		int boxes[9];
		bool availableBoxes[9];
		int winner;

		void initialize_board();
		void player_turn();
		void computer_turn();
		void update_board(int selection, int player);
		void print_board();
		void check_for_winner(int selection, int player);
		void display_winner();
};

#endif