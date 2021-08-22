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

    def display_message(self, message):
        print(message)

    def display_game_options(self):
         print('What would you like to do? ')
         print('(r) register a new user ')
         print('(s) show the score board ')
         print('(p) play a game ')
         print('(q) quit')
         game_option = input('')
         return game_option
    
    def display_gameplay_options(self):
        print('Let’s play the game of Mastermind! ')
        print('How many players (2-4)? ')
        
        try:
            number_of_players = int(input(''))
            if(number_of_players < 2 or number_of_players > 4):
                raise ValueError('')
            return number_of_players
        except ValueError:
            display_message('Please enter a valid number between 2 and 4')
        except:
            display_message('Invalid input')
