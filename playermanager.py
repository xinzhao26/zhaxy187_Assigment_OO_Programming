#
# File: playermanager.py
# Author: Xin Zhao
# Student Id: 110352998
# Email Id: zhaxy187@mymail.unisa.edu.au
# Date: 22/08/21
# Description: This class manages the players, and their game play
# This is my own work as defined by the University's
# Academic Misconduct policy.
#

from user import User
from player import Player
from userinterfacemanager import UserInterfaceManager
from usermanager import UserManager

# This class manages the players, and their game play
class PlayerManager:

	def __init__(self, user_manager):
		 # User interface manager to handle user interface functions
		self.__user_interface_manager = UserInterfaceManager()

		 # User manager to handle user related operations
		self.__user_manager = user_manager

		# Total number of players
		self.__number_of_players = 0

		# Total number of players
		self.__number_of_total_attempts = 0

		# Initialise an empty list of players
		self.__players=[]

	# This method sets the total number of players
	def set_number_of_players(self, number_of_players):
		self.__number_of_players = number_of_players

	# This method sets the total number of attempts for each player
	def set_number_of_total_attempts(self, number_of_total_attempts):
		self.__number_of_total_attempts = number_of_total_attempts

	# This method returns the total number of players
	def get_number_of_players(self):
		return self.__number_of_players

	# This method returns the total number of attempts for each player
	def get_number_of_total_attempts(self):
		return self.__number_of_total_attempts

	# This method returns a list of all players
	def get_players(self):
		return self.__players

	# This method resets the player configuration
	def reset_players(self):
		# Initialise an empty list of players
		self.__players = []

		# Total number of players set to 0
		self.__number_of_players = 0

		# Total number of attempts set to 0
		self.__number_of_total_attempts = 0

	# This method adds players to the list of players
	def add_player(self, player):
		self.__players.append(player)

	# This method registers a player with a player_name passed in
	def register_player(self, player_name): 
		registered_successfully = False

		# Check if it's a valid player from the list of registered users
		user = self.__user_manager.find_user(player_name)

		# User with player_name not found
		if user == None:
			self.__user_interface_manager.display_message('Invalid user name')

		# Duplicate player registration
		elif(any(player.get_name() == player_name for player in self.__players)):
			self.__user_interface_manager.display_message(player_name+' is already in the game')  

		else:
			# Register player successfully
			self.__players.append(Player(player_name, user.get_is_computer()))
			registered_successfully = True

		return registered_successfully

	# This method helps set up the list of players with user input
	def set_up_players(self):
		#Initialise player index to 1
		player_index = 1

		while(player_index <= self.__number_of_players):

			# Ask the user to enter a player name
			player_name = self.__user_interface_manager.get_user_input('What is the name of player #'+str(player_index)+"\n")

			# If registered sucessfully move on to the next 
			if self.register_player(player_name):
				player_index += 1
		
		# Read the total number of attempts to be set for each player, from the user input
		while self.__number_of_total_attempts < 5 or self.__number_of_total_attempts > 10:
			try:
				self.__number_of_total_attempts = int(self.__user_interface_manager.get_user_input('How many attempts will be allowed for each player (5-10)\n'))
				
				# Raise a value error if an invalid number of attempts is entered
				if(self.__number_of_total_attempts < 5 or self.__number_of_total_attempts > 10):
					raise ValueError('')
			except ValueError:
				self.__user_interface_manager.display_message('\nPlease enter a valid number between 5 and 10')
			except:
				self.__user_interface_manager.display_message('\nInvalid input')

	# This method determines if the players are still playing
	def are_players_still_playing(self):
		# From the list of all players return true, if any one of the players has its is_playing flag set to true
		return any(player.get_playing() == True for player in self.__players)