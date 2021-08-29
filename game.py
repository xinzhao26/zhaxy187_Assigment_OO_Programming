#
# File: feedback.py
# Author: Xin Zhao
# Student Id: 110352998
# Email Id: zhaxy187@mymail.unisa.edu.au
# Date: 27/08/21
# Description: This class represents the Game which handles user options for different paths in the game 
# This is my own work as defined by the University's
# Academic Misconduct policy.
#

from userinterfacemanager import UserInterfaceManager
from usermanager import UserManager
from playermanager import PlayerManager
from gamemanager import GameManager
from scoreboard import ScoreBoard

# This class represents a Game which handles user options for different paths in the game 
class Game():
    
    def __init__(self):
        # User option for game r, p, s or q
        self.__game_option = ''

        # User interface manager to handle user interface functions
        self.__user_interface_manager = UserInterfaceManager()

        # User manager to handle user related operations
        self.__user_manager = UserManager()

        # Player manager to handle player related operations
        self.__player_manager = PlayerManager(self.__user_manager)

        # Denotes the score board
        self.__score_board = ScoreBoard(self.__user_interface_manager, self.__user_manager, self.__player_manager)

        # The main manager that handles game play
        self.__game_manager = GameManager(self.__user_interface_manager, self.__user_manager, self.__player_manager, self.__score_board)

    # This method when called displays a set of options for the user to choose a path in the game
    def play_game(self):
        try:
            # Show options until user enters q or quit
            while self.__game_option != 'q':

                # Call on the display game options method of the user interface class to read the user option
                self.__game_option = self.__user_interface_manager.display_game_options()

                # User has selected r - register a new user into the system
                if self.__game_option == 'r':
                    user_name = self.__user_interface_manager.get_user_input('What is the name of the new user?\n')
                    self.__user_manager.register_user(user_name)

                # User has selected p - to play the game
                elif self.__game_option == 'p':
                    # Initiaite game config
                    self.__game_manager.set_up_game()

                    # Setup codes for code breakers to break
                    self.__game_manager.set_up_codes()

                    # Commence the operations where code breakers enter codes, which is then verified by the codemaker and feedback provided if necessary
                    self.__game_manager.guess_and_compute_codes()

                # User has selected s - show scoreboard
                elif self.__game_option == 's':
                    self.__score_board.show_score_board()
            else:
                # Call the gracefully exit method that exits the game when user enters q - quit
                self.gracefully_exit_game()
        except KeyboardInterrupt:
            # Call the gracefully exit method that exits the game when user enters  a Command C (Ctrl C for windows)
            self.gracefully_exit_game()

    # This method resets the input type style to normal and displays the exit message
    def gracefully_exit_game(self):
        self.__user_interface_manager.reset_input_type()
        self.__user_interface_manager.display_message('\nThank you for playing the World of Mastermind!')
