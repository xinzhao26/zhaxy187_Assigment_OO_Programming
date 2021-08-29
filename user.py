#
# File: user.py
# Author: Xin Zhao
# Student Id: 110352998
# Email Id: zhaxy187@mymail.unisa.edu.au
# Date: 22/08/21
# Description: This class represents a user
# This is my own work as defined by the University's
# Academic Misconduct policy.


#This class represents a user
class User:

	# User name
	__name = ""

	# Flag that tells us if this user is a computer user
	__is_computer = False

	def __init__(self, name, is_computer = False):
		self.__name = name
		self.__is_computer = is_computer
		self.__user_score = 0
		self.__user_games_played = 0

	# Returns the user's name
	def get_name(self):
		return self.__name

	# Returns if the user is a computer
	def get_is_computer(self):
		return self.__is_computer

	# Returns the user score
	def get_user_score(self):
		return self.__user_score

	# Returns the user games played
	def get_user_games_played(self):
		return self.__user_games_played

	# Increments the game stats
	def increment_game_stats(self, score):
		# Add to the total score of the score
		self.__user_score += score

		# Increment the number of games played by 1
		self.__user_games_played += 1
