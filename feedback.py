#
# File: feedback.py
# Author: Xin Zhao
# Student Id: 110352998
# Email Id: zhaxy187@mymail.unisa.edu.au
# Date: 27/08/21
# Description: This class represents a feedback
# This is my own work as defined by the University's
# Academic Misconduct policy.
#

class Feedback():

	# Constructor
	def __init__(self, code_entered, feedback_given):
		# Represents code entered by the code breaker
		self.__code_entered = code_entered

		#Represents feedback for the code entered
		self.__feedback_given = feedback_given

	# Returns the code entered
	def get_code_entered(self):
		return self.__code_entered

	# Returns the feedback provided
	def get_feedback_given(self):
		return self.__feedback_given