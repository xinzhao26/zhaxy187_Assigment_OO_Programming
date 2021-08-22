#
# File: playermanager.py
# Author: Xin Zhao
# Student Id: 110352998
# Email Id: zhaxy187@mymail.unisa.edu.au
# Date: 22/08/21
# Description: This class manages the users, and their registration
# This is my own work as defined by the University's
# Academic Misconduct policy.
#

from user import User
from player import Player
from userinterfacemanager import UserInterfaceManager
from usermanager import UserManager

class PlayerManager:

	players = []

	def __init__(self, user_manager):
		self.userinterfacemanager = UserInterfaceManager()
		self.number_of_players = 0
		self.user_manager = user_manager

	def set_number_of_players(self, number_of_players):
		self.number_of_players = number_of_players

	def get_number_of_players(self):
		return self.number_of_players

	def register_player(self, player_name): 
		registered_successfully = False
		if(any(player.name == player_name for player in self.players)):
			self.userinterfacemanager.display_message(player_name+' is already in the game')	       
		elif(any(user.name == player_name for user in self.user_manager.get_users())):
			self.players.append(Player(player_name))
			registered_successfully = True
		else:
			self.userinterfacemanager.display_message('Invalid user name')
		print('')
		return registered_successfully
	