from userinterfacemanager import UserInterfaceManager
from usermanager import UserManager
from playermanager import PlayerManager
from gamemanager import GameManager


class Game():

    game_option = ''
    
    def __init__(self):
        self.userinterface_manager = UserInterfaceManager()
        self.user_manager = UserManager()
        self.player_manager = PlayerManager(self.user_manager)
        self.game_manager = GameManager(self.userinterface_manager, self.user_manager, self.player_manager)

    def play_game(self):
    	while self.game_option != 'q':
            self.game_option = self.userinterface_manager.display_game_options()
            if self.game_option == 'r':
            	user_name = input('What is the name of the new user?\n')
            	self.user_manager.register_user(user_name)
            elif self.game_option == 'p':
            	self.game_manager.set_up_game()
            	self.game_manager.set_up_codes()




