#
# File: player.py
# Author: Xin Zhao
# Student Id: 110352998
# Email Id: zhaxy187@mymail.unisa.edu.au
# Date: 22/08/21
# Description: This class represents a player
# This is my own work as defined by the University's
# Academic Misconduct policy.
#
from user import User
from feedback import Feedback

# This class represents a player
class Player(User):

	def __init__(self, name, is_computer = False):
		User.__init__(self, name, is_computer)
		self.__feedback_list = []
		self.__code = ""
		self.__is_playing = True
		self.__number_of_attempts = 0
		self.__feedback_list = []
		self.__is_successful = False

	# This method sets the code for the player
	def set_code(self, code):
		self.__code = code

	# This method sets the number of attempts for the player
	def set_number_of_attempts(self, number_of_attempts):
		self.__number_of_attempts = number_of_attempts

	# This method returns the number of atempts of the player
	def get_number_of_attempts(self):
		return self.__number_of_attempts

	# This method sets the flag that denotes if the player is still playing
	def set_playing(self, is_playing):
		self.__is_playing = is_playing

	# This method returns the flag that denotes if the player is still playing
	def get_playing(self):
		return self.__is_playing

	# This method sets the code and feedback for a particular turn for the player
	def add_feedback(self,code, feedback):
		self.__feedback_list.append(Feedback(code, feedback))

	# This method returns the list of feedback items for a player
	def get_feedback_list(self):
		return self.__feedback_list

	# This methods sets the successful flag once the player successfully breaks the code
	def set_successful(self, is_successful):
		self.__is_successful = is_successful

	# This method returns the flag which determines if the player successfully broke the code
	def get_successful(self):
		return self.__is_successful

	# This method compares the code entered against the code set to determine if a feedback is needed or the code match was sucessful
	def evaluate_code(self, code):
		# Entered code matches the code makers' code previously set
		if code == self.__code:
			return None
		else:
			# Feedback string
			feedback = ''

			# Remaining entered code characters after the correct order and colour codes are eliminated
			remnants_code_entered = ''

			# Remaining set code characters after the correct order and colour codes are eliminated
			remnants_code_set = ''

			for entered_code, code_set in zip(code, self.__code):
				# For every correct order and colour, add 'K' to the feedback string
				if entered_code == code_set:
					feedback += 'K'
				# Add the unmatched characters to the remnants string
				else:
					remnants_code_entered += entered_code
					remnants_code_set += code_set

			# Compare the remnant code entered against the remaining code set characters and add a 'W' 
			# to the feedback for every character that matches but not necessarily in the correct position
			for remnant_code in remnants_code_entered:
				if remnant_code in remnants_code_set:
					feedback += 'W'

			return feedback