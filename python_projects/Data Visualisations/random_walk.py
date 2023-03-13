from random import choice

class RandomWalk():
    """ A Class Representing a Data Representation decided by Chance! """ 
    def __init__(self, number_points=6000):
        """ Initiallizing the Attributes""" 
        self.number_points = number_points
        
        #All the Walks will start at (0,0).
        self.x_values= [0]
        self.y_values= [0]
        self.get_step()
        
    def get_step(self):
        """ Refactor """ 
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
        steps = direction * distance 
        return steps

    def update_walk(self):
        """ Updating the Walk """
        #Continuing the Walk until the Statement is False. 
        while len(self.x_values) <  self.number_points:
            x_step = self.get_step()
            
            #Allowing the Walk to go Left (-1) or Right (1) with the Distance being from 0 to 5.
            y_step = self.get_step()
            
            #Negating the Walk from being on Hiatus.
            if x_step == 0 and y_step == 0:
                continue
            
            #Calculate the Next Values.    
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
            
            self.x_values.append(next_x)
            self.y_values.append(next_y)
