class GameStats():
    
    def __init__(self, game_settings):
        """ """ 
        self.game_settings = game_settings
        self.reset_stats() 
        self.game_active = False
        
    def reset_stats(self): 
        """ """ 
        self.shots_left = self.game_settings.shots_available
