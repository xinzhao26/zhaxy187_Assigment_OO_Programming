import game
import random

# This class is the entry point of the application
class WorldOfMastermind:

    def __init__(self):
    	# Create a new instance of game
        self.game = game.Game()
    
    # This method calls on the play_game function from the Game class to commence the game
    def run(self):
    	# Begin playing the game
    	self.game.play_game()

# Run the world of mastermind application
wom = WorldOfMastermind()
wom.run()
