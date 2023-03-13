import pygal 
from random import randint
from random_walk import RandomWalk
from dice import Die

a = Die()
b = Die(10)
frequency = [] 
for rolls in range(50000):
    roll = a.roll() * b.roll()
    frequency.append(roll) 

commonity = []
mega_roll = a.sides + b.sides
c = [frequency.count(rolling) for rolling in range(2, mega_roll+1)]
d = [commonity.append(a) for a in c]

    
hist = pygal.Bar() 
hist.title = "50k Rolls of a Two Six Sided Dies at Once!"
hist.x_labels = [x+1 for x in range(1, mega_roll)] 
hist.x_title = "Side Numbers of Two Dices"
hist.y_title = "The Results of Two Dices"

hist.add("Two Six Sided Dice", commonity)  

#Test V------------------

pg = RandomWalk(2500)
pg.update_walk()
l = pg.x_values + pg.y_values

hist = pygal.Bar()
hist.title = "A Graph Representing a Random Walk"
hist.x_labels = "X_Values","Y_Values"
hist.y_title = "Results"

hist.add("Random Walk", l)
hist.render_to_file("Random Walk Graph.svg")

