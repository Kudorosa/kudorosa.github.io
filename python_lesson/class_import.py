
""" Sandwich Creator """ 
class Sandwich(): 
    """ Making a Sandwich, can be used to make a Sandwich with fillings """ 
    def __init__(self,filling, sauce, *extras): 
        self.filling = filling
        self.sauce = sauce 
        self.extras = extras 
        
    def build_sandwich(self): 
        maker = "\n" + self.filling + " was added to your sandwich! \n"
        maker += "\n" + self.sauce + " was added to your sandwich! \n"
        for item in self.extras:
            maker += "\n" + item + " was added to your sandwich! \n" 
        return maker.title() 

class Cat(): 
    """ Making a Cat, can be used to make a Cat that does Cat-like things """ 
    def __init__(self, name, age):  
        self.name = name 
        self.age = age 
    """ Name and Age of the Cat """ 
    
    def meow(self): 
        """ Causes a Cat to make Noise """ 
        print((self.name + " has unleashed a Meow!\n").title()) 
    
    def jump(self): 
        """ Causes a Cat to Jump on something. """ 
        print((self.name + " has jumped on top of an Object!\n").title()) 
    
    def scratch(self):
        """ Causes the Cat to Scratch something. """ 
        print(f"{self.name} has scratched an object tearing it!".title()) 

#Test V-------------------------------------
from classes import IceCreamStand

ice = IceCreamStand("Creamy Sheemy","Stand") 
ice.describe_restaurant() 

import classes as clas

ad = clas.Admin("Dean","UK","Administrator","Chinamo") 
ad.privilege.show_privileges() 

import admininstrator as admin 
from user import User 

ade = admin.Admin("Dave","UK","Administrator","Aere") 
ade.privilege.show_privileges() 

#------------------------

from collections import OrderedDict

voted = OrderedDict() 

voted['deathdean'] = "Unbound Soul Simulator"
voted['kudorosa'] = "Return of the Insects!" 
voted['avn'] = "WASPS!" 
print("\n") 
for people, games in voted.items(): 
    print((people + " has voted for '" + games + "' to be created!\n").title()) 
    
#Test V-----------------------------------------
from collections import OrderedDict 

glossary2 = OrderedDict() 

glossary2['true'] = "this means the value is true and will run"
glossary2['false'] = "this means the value is false and will not run"
glossary2['variable'] = "holds any value for later use"
glossary2['='] = "assigns a value"
glossary2['=='] = "checks to see if two values are equal"
glossary2['print'] = "displays any code written inside it"
glossary2['set'] = "ensures Values are unique without any repeats"
glossary2['append'] = "adds a value to the end of a list"
glossary2['del'] = "permanently removes a list/variable/value"
glossary2['pop'] = "removes a value but allows for it to be used"
     
print("\n----------------") 
for term, meaning in glossary2.items(): 
    print(("The Programming Term '" + term + "', " + meaning + ".\n").title())

from random import randint #Importing from a Python Standard Library.

class Die(): 
    """ A Die which can be rolled, can be used to make Dice """ 
    def __init__(self): 
        self.sides = 6 
    """ A Die with Six Sides """ 
    
    def roll_die(self): 
        """ Rolling a Dice! """ 
        r = randint(1, self.sides)
        if r == self.sides:
            print(("Amazing Luck! You Rolled a " + str(self.sides) + "!"
            ).title()) 
        else:
            print("You Rolled A " + str(r) + "!")  

roll = Die() 


class AdvancedDie(Die): 
    """ A Child of the Die, An Advanced Die """ 
    
    def __init__(self):
        """ Die Information """ 
        super().__init__()
        self.sides = 10
        """ This Die will have 10 Sides """ 
        
advanced_roll = AdvancedDie()

    

class MasterDie(AdvancedDie): 
   """ A Child of the AdvancedDie, A Master Die """
   
   def __init__(self): 
       """ Another Die """ 
       
       super().__init__()
       self.sides = 20 
       """ This Die will have 20 Sides """ 

master_roll = MasterDie() 
master_roll.roll_die() 

import math 

print("Pi: " + str(math.pi)) 
print("Infinity: " + str(math.inf)) 

import random 

class Lootbox(): 
    """ My Attempt at making a Lootbox """ 
    
    def __init__(self): 
        """ Lootboxes """ 
        self.loot = ["Guns","Swords","Armour"] 
    
    def open(self): 
        """ Open up a Lootbox """ 
        prize = random.choice(self.loot)
        print("You have Unlocked " + prize + "!") 

a = Lootbox() 
a.open() 
    
        
       
   

