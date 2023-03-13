from random import randint

class Die(): 
    """ A Class Representing a Die """ 
    def __init__(self, sides=6): 
        self.sides = sides
    
    def roll(self):
        """ Rolling a Die """ 
        rolling = randint(1, self.sides) 
        return rolling
