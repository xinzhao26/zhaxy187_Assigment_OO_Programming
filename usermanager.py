#
# File: usermanager.py
# Author: Xin Zhao
# Student Id: 110352998
# Email Id: zhaxy187@mymail.unisa.edu.au
# Date: 22/08/21
# Description: This class manages the users, and their registration
# This is my own work as defined by the University's
# Academic Misconduct policy.
#

from user import User
from userinterfacemanager import UserInterfaceManager

# This class manages the users, and their registration
class UserManager:

    # Set up the computer users HAL9000 and VIKI
    __users = [User('HAL9000', True), User('VIKI', True)]

    def __init__(self):
        self.userinterfacemanager = UserInterfaceManager()

    # This methid returns the users
    def get_users(self):
        return self.__users

    # This method registers a new user with the user_name parameter
    def register_user(self, user_name):  
        # If the user name passed in exists, fail
        if(any(user.get_name() == user_name for user in self.__users)):
             self.userinterfacemanager.display_message('Sorry, the name is already taken')
        
        # Register a new user
        else:
             self.__users.append(User(user_name))
             message = 'Welcome, '+user_name+'!'
             self.userinterfacemanager.display_message(message)
        print('')

    # This method searches for a user in the list of users based on the user name
    def find_user(self, user_name):
        for user in self.__users:
            if user.get_name() == user_name:
                # If found return the user
                return user

    # This method calls on the user's increment game stats method to increment the score and number of games played
    def increment_game_stats(self, user_name, score):
        user = self.find_user(user_name)

        # Increment game stats of users present
        if user != None:
            user.increment_game_stats(score)