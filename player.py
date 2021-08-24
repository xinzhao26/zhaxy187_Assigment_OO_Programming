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

class Player(User):

	code = ""

	def __init__(self, name):
		User.__init__(self, name)

	def set_code(self, code):
		self.code = code
