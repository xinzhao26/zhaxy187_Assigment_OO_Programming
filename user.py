#
# File: user.py
# Author: Xin Zhao
# Student Id: 110352998
# Email Id: zhaxy187@mymail.unisa.edu.au
# Date: 22/08/21
# Description: This class represents a plaer
# This is my own work as defined by the University's
# Academic Misconduct policy.
#
class User:

    name = ""
   
    def __init__(self, name):
        self.name = name

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name
