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

class UserManager:

    users = [User('HAL9000'), User('VIKI')]

    def __init__(self):
        self.userinterfacemanager = UserInterfaceManager()

    def get_users(self):
        return self.users

    def register_user(self, user_name):        
        if(any(user.name == user_name for user in self.users)):
             self.userinterfacemanager.display_message('Sorry, the name is already taken')
        else:
             self.users.append(User(user_name))
             message = 'Welcome, '+user_name+'!'
             self.userinterfacemanager.display_message(message)
        print('')
