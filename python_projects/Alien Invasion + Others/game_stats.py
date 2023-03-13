import json

class GameStats():
    
    def __init__(self, game_settings):
        """ """ 
        self.game_settings = game_settings
        self.reset_stats() 
        self.game_active = False
        
        score = "Alien Invasion High-Score.txt"
        try:
            with open(score) as file_object:
                highest_score = json.load(file_object)
            self.high_score = int(highest_score)
        
        except FileNotFoundError:
            self.high_score = 0
            
        
        
    def reset_stats(self): 
        """ """ 
        self.ships_left = self.game_settings.ships_available
        self.score = 0
        self.level = 1  
