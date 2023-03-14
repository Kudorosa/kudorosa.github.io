Humanoid = {} 

function Humanoid:new(o, name) 
    o = o or {} 
    self.__index = self
    setmetatable(o, self) 
    self.name = name
    return o 
end 

function Humanoid:Sleep() 
    print(self.name.." is now sleeping in Bed..")
end

Hum1 = Humanoid:new{name="Dean"} 
Hum1:Sleep() 
Hum2 = Humanoid:new{name="Avneet"} 
Hum2:Sleep() 
Hum1:Sleep()