#
# File: scoreboard.py
# Author: Xin Zhao
# Student Id: 110352998
# Email Id: zhaxy187@mymail.unisa.edu.au
# Date: 28/08/21
# Description: This class manages the score for players
# This is my own work as defined by the University's
# Academic Misconduct policy.
#
from player import Player
from userinterfacemanager import UserInterfaceManager
from usermanager import UserManager
from playermanager import PlayerManager

# This class manages the score for players
class ScoreBoard:

	def __init__(self, user_interface_manager, user_manager, player_manager):
		self.__user_interface_manager = user_interface_manager
		self.__user_manager = user_manager
		self.__player_manager = player_manager

	# This method helps calculate scores for the code breaker and increments the relevant user's game stats
	def calculate_scores(self):
		# Player index set to 0
		player_index = 0

		# Get the total number of players
		total_players = len(self.__player_manager.get_players())

		# Get all players
		players = self.__player_manager.get_players()

		while(player_index != total_players):
			# Get the code breaker
			player_code_breaker = players[player_index]

			# Only computer scores for non computer users
			if player_code_breaker.get_is_computer() == False:

				# Round robin fashion of determinining code breaker - If it's the last player, the code breaker is the first one in the list, else the next
				if player_index == total_players - 1:
					player_code_maker = players[0]
				else :
					next_player_index = player_index + 1
					player_code_maker = players[next_player_index]

				# If the player was successful, calculate the code breaking score = Number of attempts - Number of attempts taken to break the code + 1
				if player_code_breaker.get_successful() == True:
					code_breaking_score = self.__player_manager.get_number_of_total_attempts() - player_code_breaker.get_number_of_attempts() + 1
				else:
					code_breaking_score = 0

				# Calculate the code making score = Number of attempts the code maker needed to break the code - 1
				code_making_score = player_code_maker.get_number_of_attempts() - 1

				# Adding the 2 scores above gives us the total score
				total_score = code_breaking_score + code_making_score

				self.__user_interface_manager.display_message(player_code_breaker.get_name()+' receives '+str(code_breaking_score)+' + '+str(code_making_score)+' = '+str(total_score))


			self.__user_interface_manager.display_message('')

			# Increment game stats
			self.__user_manager.increment_game_stats(player_code_breaker.get_name(), total_score)

			player_index += 1

	# This method shows the score board to the user
	def show_score_board(self):
		self.__user_interface_manager.display_message("=====================================")
		self.__user_interface_manager.display_message("Name\t\tScore Games Average")
		self.__user_interface_manager.display_message("=====================================")

		# Display the score for all users
		for user in self.__user_manager.get_users():
			if user.get_is_computer() != True:
				average_score = 0
				if user.get_user_games_played() > 0:
					average_score = user.get_user_score()/user.get_user_games_played()

				self.__user_interface_manager.display_message(user.get_name()+'\t\t'+f"{user.get_user_score():>5}"+' '+f"{user.get_user_games_played():>5}"+' '+f"{average_score:>5}")
		
		self.__user_interface_manager.display_message("=====================================\n")


