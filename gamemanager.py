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
from random import choice

# This class manages the game play for players
class GameManager:

	def __init__(self, userinterface_manager, user_manager, player_manager, score_board):
		self.__user_interface_manager = userinterface_manager
		self.__user_manager = user_manager
		self.__player_manager = player_manager
		self.__score_board = score_board

		# Only allow R, G, B, Y, W and K
		self.__regular_expression=re.compile('^[RGBYWK]+$')

		self.__letters_list = ['R','G','B','Y','W','K']

	# This method sets the game up by resetting all counters to 0 - players, number of players and requests for user input
	def set_up_game(self):
		self.__player_manager.reset_players()
		self.__player_manager.set_number_of_players(self.__user_interface_manager.display_gameplay_options())
		self.__player_manager.set_up_players()


	# This method setups the codes for code makers to make, and code breakers to break
	def set_up_codes(self):
		
		# Initialise player index to 0
		player_index = 0

		# Get the total number of players
		number_of_players = self.__player_manager.get_number_of_players()
		
		# Run through every player
		while player_index < number_of_players:
			is_valid_code_entered = False
			players = self.__player_manager.get_players()

			player_code_maker = players[player_index]
			# Round robin fashion of determinining code breaker - If it's the last player, the code breaker is the first one in the list, else the next
			if player_index == number_of_players - 1:
				player_code_breaker = players[0]
			else:
				next_index = player_index + 1
				player_code_breaker = players[next_index]

					
			self.__user_interface_manager.display_message('\n* '+player_code_maker.get_name()+'\'s turn to set the code for '+player_code_breaker.get_name()+' to break')

			while is_valid_code_entered == False:
				try:
					# User enters an input if not a computer
					if player_code_maker.get_is_computer() != True:
						code = self.__user_interface_manager.get_user_input('Please enter the code:\n')
						if len(code) != 4 or self.__regular_expression.match(code) == None:
							raise ValueError('')
					
					# Generate a random code for the computer
					else:
						code = self.get_random_code()

					# Set the code
					player_code_maker.set_code(code)
					self.__user_interface_manager.display_message('The code is now set for '+player_code_breaker.get_name()+' to break.')
					is_valid_code_entered = True
				except ValueError:
					self.__user_interface_manager.display_message('Invalid code.  \nIt must be exactly four characters, each can be R, G, B, Y, W, or K.  ')
				
			player_index += 1


	# This method helps code breakers guess the code set for them by the code maker, and then their scores are calculated accordingly
	def guess_and_compute_codes(self):
		# Initialise attempts index to 0
		attempts_index = 0

		# Get the total number of players
		number_of_players = self.__player_manager.get_number_of_players()

		# Get the total number of attempts allowed
		total_attempts_allowed = self.__player_manager.get_number_of_total_attempts()

		# Get all players
		players = self.__player_manager.get_players()

		# Play till all players have finished playing
		while self.__player_manager.are_players_still_playing() == True:
			# Initialise players index to 0
			player_index = 0

			# Iterate through all players
			while player_index < number_of_players:

				player_code_breaker = players[player_index]

				# Play the game is player has not already finished his/her game
				if player_code_breaker.get_playing():

					current_number_of_attempts = player_code_breaker.get_number_of_attempts()
				
					# Round robin fashion of determinining code maker - If it's the last player, the code maker is the first one in the list, else the next
					if player_index == number_of_players - 1:
						player_code_maker = players[0]
					else:
						next_index = player_index + 1
						player_code_maker = players[next_index]


					# If attempts are remaining, allow the code breaker to guess the code
					if current_number_of_attempts <= total_attempts_allowed:
						self.__user_interface_manager.display_message('\n* '+player_code_breaker.get_name()+'\'s turn to guess the code')
						previous_attempts = player_code_breaker.get_number_of_attempts()
						attempts_left = total_attempts_allowed - current_number_of_attempts

						self.__user_interface_manager.display_message('Previous attempts :'+str(previous_attempts))

						# Display old feedback to the code breaker, if present
						if len(player_code_breaker.get_feedback_list()) > 0:
							self.__user_interface_manager.display_message("==============")
							self.__user_interface_manager.display_message("Code Feedback")
							self.__user_interface_manager.display_message("==============")
							for feedback_object in player_code_breaker.get_feedback_list():
								self.__user_interface_manager.display_message(feedback_object.get_code_entered()+' '+" ".join(feedback_object.get_feedback_given()))
							self.__user_interface_manager.display_message("==============")

						self.__user_interface_manager.display_message('Attempts left :'+str(attempts_left))

						is_valid_code_entered = False

						while is_valid_code_entered == False:
							try:
								# User enters an input if not a computer
								if player_code_breaker.get_is_computer() != True:
									code = self.__user_interface_manager.get_user_input('Please enter the code:\n')
									if len(code) != 4 or self.__regular_expression.match(code) == None:
										raise ValueError('')
								# Generate a random answer for the computer
								else:
									code = self.get_random_code()
									self.__user_interface_manager.display_message(player_code_breaker.get_name()+'\'s guess: '+code)
								
								is_valid_code_entered = True
							
								# Incrementing attempts counter for player
								increment = previous_attempts + 1
								player_code_breaker.set_number_of_attempts(increment)

								#Evaluating code entered
								feedback = player_code_maker.evaluate_code(code)

								# Feedback is None which means the correct code was entered
								if feedback == None:
									suffix = ' attempts!'
									if player_code_breaker.get_number_of_attempts() == 1:
										suffix = ' attempt!'
									player_code_breaker.set_playing(False)
									player_code_breaker.set_successful(True)
									self.__user_interface_manager.display_message(player_code_breaker.get_name()+' broke the code in '+str(player_code_breaker.get_number_of_attempts()) +suffix)
								
								# Incorrect code was entered
								else:
									player_code_breaker.add_feedback(code, feedback)
									self.__user_interface_manager.display_message('Feedback: '+feedback)

								# Attempts exhausted and player lost
								if attempts_left <= 1:
									if player_code_breaker.get_playing() == True:
										player_code_breaker.set_playing(False)
										self.__user_interface_manager.display_message(player_code_breaker.get_name()+' failed to break the code.\n')

							except ValueError:
								self.__user_interface_manager.display_message('Invalid code.  \nIt must be exactly four characters, each can be R, G, B, Y, W, or K.  ')
				player_index += 1

		self.__user_interface_manager.display_message('\nThe game is now finished.')
		self.__score_board.calculate_scores()
			

	# This method returns a random 4 character code of R, G, B, Y, W and K
	def get_random_code(self):
		return ''.join(choice(self.__letters_list) for i in range(4))


