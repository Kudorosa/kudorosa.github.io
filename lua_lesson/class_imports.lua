M = require("helpful_functions")

--[[Sandwich Creator ]]--
Sandwich = {} 
    --[[Making a Sandwich, can be used to make a Sandwich with fillings ]]--
    function Sandwich:new(o, filling, sauce, ...)
        o = o or {}
        self.__index = self
        setmetatable(o, self) 
        self.filling = filling
        self.sauce = sauce 
        self.extras = ...
        return o 
    end 
        
    function Sandwich:Build_sandwich() 
        Maker = "\n"..self.filling.." was Added to your sandwich! \n"
        Maker = Maker.."\n"..self.sauce.." was Added to your sandwich! \n"
        for i, item in pairs(self.extras) do
            Maker = Maker.."\n"..item.." was Added to your sandwich! \n" 
        end
        return Maker
    end

 Cat = {}
    --[[Making a Cat, can be used to make a Cat that does Cat-like things ]]--
    function Cat:new(o, name, age) 
        o = o or {}
        self.__index = self
        setmetatable(o, self)
        self.name = name 
        self.age = age 
        return o 
    end 
    --[[Name and Age of the Cat ]]--
    
    function Cat:Meow(self)
        --[[Causes a Cat to make Noise ]]--
        print(self.name.." has unleashed a Meow!\n") 
    end
    
    function Cat:Jump(self)
        --[[Causes a Cat to Jump on something. ]]--
        print(self.name.." has jumped on top of an Object!\n") 
    end

    function Cat:Scratch(self)
        --[[Causes the Cat to Scratch something. ]]--
        print(self.name.." has scratched an object tearing it!") 
    end
--#Test V-------------------------------------
A = require("classes") 

Ice = IceCreamStand:new{restaurant_name="Creamy Sheemy", cuisine_type="Stand"}
Ice:Describe_restaurant() 

B = require("classes")

Ada = Ad:new{forename="Dean", location="UK", other="Administrator", surname="Chinamo"} 
Ada.privilege:Show_privileges() 

C = require("administrator")
D = require("user") 

Ade = Ad:new{forename="Dave", location="UK", other="Administrator", surname="Aere"} 
Ade.privilege:Show_privileges() 

--#------------------------

Voted = {}

Voted['deathdean'] = "Unbound Soul Simulator"
Voted['kudorosa'] = "Return of the Insects!" 
Voted['avn'] = "WASPS!" 
print("\n") 
for people, games in pairs(Voted) do 
    print(M.Title(people).." has Voted for '"..games.."' to be created!\n") 
end
    
--#Test V-----------------------------------------

Glossary2 = {}

Glossary2['true'] = "this means the value is true and will run"
Glossary2['false'] = "this means the value is false and will not run"
Glossary2['variable'] = "holds any value for later use"
Glossary2['='] = "assigns a value"
Glossary2['=='] = "checks to see if two values are equal"
Glossary2['print'] = "displays any code written inside it"
Glossary2['set'] = "ensures Values are unique without any repeats"
Glossary2['table.insert(value, #tablename)'] = "Adds a value to the end of a list"
Glossary2['table.remove'] = "permanently removes a list/variable/value"
Glossary2['table.remove'] = "also removes a value but allows for it to be used"
     
print("\n----------------") 
for term, meaning in pairs(Glossary2) do
    print("The Programming Term '"..term.."', "..meaning..".\n")
end
--#Importing from a Lua Standard Library.

Die = {}
    --[[A Die which can be Rolled, can be used to make DIce ]]--
    function Die:new(o)
        o = o or {}
        self.__index = self
        setmetatable(o, self) 
        self.sides = 6 
        return o 
    end

    --[[A Die with Six Sides ]]--
    
    function Die:Roll_die() 
        --[[Rolling a DIce! ]]--
        R = math.random(1, self.sides)
        if R == self.sides then
            print("Amazing Luck! You Rolled a "..self.sides.."!") 
        else
            print("You Rolled A "..R.."!")  
        end
    end

Roll = Die:new() 
Roll:Roll_die()

AdvancedDie = Die:new()
 function AdvancedDie:new(o)
    --[[A Child of the Die, An Advanced Die ]]--
        --[[Die Information ]]--
        o = o or {}
        self.__index = self
        setmetatable(o, self)
        self.sides = 10
        --[[This Die will have 10 Sides ]]--
        return o 
 end
        
Advanced_Roll = AdvancedDie:new()

MasterDie = AdvancedDie:new() 
 function MasterDie:new(o)
   --[[A Child of the AdvancedDie, A Master Die ]]--
    o = o or {}
    self.__index = self
    setmetatable(o, self) 
    self.sides = 20
    --[[Another Die v ]]--
    --[[This Die will have 20 Sides ]]--
    return o 
end

Master_roll = MasterDie:new() 



math.inf = 1/0
print("Pi: "..math.pi)
print("Infinity: "..math.inf)


Lootbox = {}
    --[[My Attempt at making a Lootbox ]]--
    
    function Lootbox:new(o)  
        --[[Lootboxes ]]--
        o = o or {}
        self.__index = self
        setmetatable(o, self)
        self.loot = {"Guns","Swords","Armour"}
        return o 
    end 
    
    function Lootbox:Open()
        --[[Open up a Lootbox ]]--
        Prize = self.loot[math.random(1, #self.loot)]
        print("You have Unlocked "..Prize.."!") 
    end

A = Lootbox:new() 
A:Open() 