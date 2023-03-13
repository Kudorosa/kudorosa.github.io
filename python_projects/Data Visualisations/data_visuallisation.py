import matplotlib.pyplot as plt
from random import choice
from random_walk import RandomWalk
from dice import Die

days = [5840, 6570, 6935, 7665, 8395]
ages = [16, 18, 19, 21, 23]

#Sizes of the Title and Line Thickness. 
plt.plot(ages, days, linewidth=10)

#Sizes of the Labels.
plt.title("The Age Demographic", size=19)
plt.xlabel("Ages", size=12)
plt.ylabel("Days Survived", size=12)

#Sets the Size of Tick Labels.
plt.tick_params("both", size=4)



plt.scatter(ages, days, s=50)

plt.title("Age Demographic", size=16)
plt.xlabel("Ages",size=12)
plt.ylabel("Days", size=13)

plt.tick_params("both", size=5)


value1 = list(range(16, 28))
value2 = [number*365 for number in value1] 
colour = (0.2, 0.16, 0.32)
plt.scatter(value1, value2, c=value2, cmap=plt.cm.Reds, 
edgecolor="Yellow", s=40)

plt.title("The Ages") 
plt.xlabel("Ages", size=10)
plt.ylabel("Days", size=10)

plt.axis([16,  28, 5800, 10500]) 


#.savefig() allows you to save the Figure as a Picture, you can use the 'bbox_inches="tight"' to trim the White Space from the Figure.

#TEST V---------------------------------------
non_cube = list(range(0, 6)) 
cube = [x ** 3 for x in non_cube]
plt.scatter(non_cube, cube, c=cube, cmap=plt.cm.Blues, edgecolor="Black",
s=30) 
plt.title("Cuboid Numbers") 
plt.xlabel("Cubes", size=9)
plt.ylabel("Numbers", size=8)
plt.axis([0, 5, 0, 150]) 


non_cube = list(range(0, 5001)) 
cube = [x ** 3 for x in non_cube]
plt.scatter(non_cube, cube, c=cube, cmap=plt.cm.magma, s=30) 
plt.title("Bigger Cubes", size=10) 
plt.xlabel("Numbers", size=8)
plt.ylabel("Cubes", size=8) 

plt.axis([0, 5000, 0, 125000000000])

#-----------------------------------------------
while False:
    rw = RandomWalk(5000) 
    rw.update_walk() 
    
    #Setting the Size of the Figure. 
    plt.figure(figsize=(20, 8))

    solo_dots = list(range(rw.number_points)) 
    plt.plot(rw.x_values, rw.y_values, c="Gray", linewidth=3) 
    #Start and Last Points of the Walk. 
    plt.scatter(0, 0, c="Green", s=500)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c="Red", s=500)
    
    plt.gca().get_yaxis().set_visible(False)  #.gca() retrieves the current Axis.
    plt.gca().get_xaxis().set_visible(False)
    
    
    
    ongoing = input("\nWould you like to Deactivate the Random-Walk? (Y/N) ")
    if ongoing.lower() == "y":
        break

#Test V------------------------
a = Die() 
b = Die()

frequency = [] 
for rolls in range(50000):
    roll = a.roll() + b.roll()
    frequency.append(roll) 

commonity = []
mega_roll = a.sides + b.sides
c = [frequency.count(rolling) for rolling in range(2, mega_roll+1)]
d = [commonity.append(a) for a in c]

plt.figure(figsize=(20, 8)) 

plt.plot(commonity, c="Red", linewidth=5)
plt.title("Roll the Dice!", size=30)
plt.xlabel("Numbers", size=10) 
plt.ylabel("Rolls", size=10)

plt.tick_params("both", size=3)

plt.show()
        

        



