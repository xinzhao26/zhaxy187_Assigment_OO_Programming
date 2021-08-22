import game

class WorldOfMastermind:
	
    def __init__(self):
        self.game = game.Game()
    
    def run(self):
        self.game.play_game()





wom = WorldOfMastermind()
wom.run()
