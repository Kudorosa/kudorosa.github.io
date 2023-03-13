class Statistics(): 
    
    def __init__(self, game_settings): 
        """ """ 
        self.game_settings = game_settings 
        self.reset()
        self.game_ongoing = True 
        
    def reset(self): 
        """ Allowing the Game to Reset """ 
        self.tries_left = self.game_settings.tries_remaining
