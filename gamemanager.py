#
# File: gamemanager.py
# Author: Xin Zhao
# Student Id: 110352998
# Email Id: zhaxy187@mymail.unisa.edu.au
# Date: 22/08/21
# Description: This class manages the game play for players
# This is my own work as defined by the University's
# Academic Misconduct policy.
#
from player import Player
from userinterfacemanager import UserInterfaceManager
from usermanager import UserManager
import re

class GameManager:

	def __init__(self, userinterface_manager, user_manager, player_manager):
		self.userinterface_manager = userinterface_manager
		self.user_manager = user_manager
		self.player_manager = player_manager
		self.regular_expression=re.compile('^[RGBYWK]+$')

	def set_up_game(self):
		self.player_manager.set_number_of_players(self.userinterface_manager.display_gameplay_options())
		self.player_manager.set_up_players()

	def set_up_codes(self):
		player_index = 0
		number_of_players = self.player_manager.get_number_of_players()

		while player_index < number_of_players:
			is_valid_code_entered = False
			
			if player_index == number_of_players - 1:
				player_code_maker = self.player_manager.players[player_index]
				player_code_breaker = self.player_manager.players[0]
			else:
				player_code_maker = self.player_manager.players[player_index]
				next_index = player_index + 1
				player_code_breaker = self.player_manager.players[next_index]

			self.userinterface_manager.display_message('\n* '+player_code_maker.get_name()+'\'s turn to set the code for '+player_code_breaker.get_name()+' to break')

			while is_valid_code_entered == False:
				try:
					code = input('Please enter the code:\n')
					if len(code) != 4 or self.regular_expression.match(code) == None:
						raise ValueError('')

					player_code_maker.set_code(code)
					self.userinterface_manager.display_message('The code is now set for '+player_code_breaker.get_name()+' to break.')
					is_valid_code_entered = True
				except ValueError:
					self.userinterface_manager.display_message('Invalid code.  \nIt must be exactly four characters, each can be R, G, B, Y, W, or K.  ')
				

			player_index += 1

