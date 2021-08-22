from userinterfacemanager import UserInterfaceManager
from usermanager import UserManager
from playermanager import PlayerManager


class Game():

    game_option = ''
    
    def __init__(self):
        self.userinterfacemanager = UserInterfaceManager()
        self.user_manager = UserManager()
        self.player_manager = PlayerManager(self.user_manager)

    def play_game(self):
        while self.game_option != 'q':
            self.game_option = self.userinterfacemanager.display_game_options()
            if self.game_option == 'r':
            	user_name = input('What is the name of the new user?\n')
            	self.user_manager.register_user(user_name)
            elif self.game_option == 'p':
            	self.player_manager.set_number_of_players(self.userinterfacemanager.display_gameplay_options())

            	player_index = 1
            	while(player_index <= self.player_manager.get_number_of_players()):
            		player_name = input('What is the name of player #'+str(player_index)+"\n")

            		if self.player_manager.register_player(player_name):
            			player_index += 1
