#
# File: zhaxy187_game.py
# Author: Xin Zhao
# Student Id: 110352998
# Email Id: zhaxy187@mymail.unisa.edu.au
# Date: 21/08/21
# Description: This class manages displaying of messages to the human user
# This is my own work as defined by the University's
# Academic Misconduct policy.
#
class UserInterfaceManager:

    def __init__(self):
        self.reset_input_type()

    # This method takes in a message variable and displays it
    def display_message(self, message):
        print(message)

    # This method displays the game options to the user
    def display_game_options(self):
         self.display_message('What would you like to do? ')
         self.display_message('(r) register a new user ')
         self.display_message('(s) show the score board ')
         self.display_message('(p) play a game ')
         self.display_message('(q) quit')
         game_option = self.get_user_input('')
         return game_option
    
    # This method displays the gameplay options to the user. This is when the game starts
    def display_gameplay_options(self):
        self.display_message('Let’s play the game of Mastermind! ')
        self.display_message('How many players (2-4)? ')
        
        try:
            number_of_players = int(self.get_user_input(''))
            if number_of_players == None:
                raise ValueError('')
            elif(number_of_players < 2 or number_of_players > 4):
                raise ValueError('')
            return number_of_players
        except ValueError:
            self.display_message('Please enter a valid number between 2 and 4')
        except:
            self.display_message('Invalid input')

    # This method helps take in the user input where the font style of the user input is bold and italic
    def get_user_input(self, message):
        value = input(message+'\033[1m\033[3m')
        self.reset_input_type()
        return value

    # This method resets the user input font style to normal
    def reset_input_type(self):
        print('\033[0m\033[0m', end='')
