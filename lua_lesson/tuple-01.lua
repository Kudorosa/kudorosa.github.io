local m = require("helpful_functions") -- Module

Menu = {"burgers","pizzas","desserts","sides","drinks","extras"} --#A Tuple uses () which forms a List where Values cannot be Added or Removed. 
for i, items in pairs(m.Slice(Menu, 3, 5)) do 
    print(m.Title(items))
end

print("\nOriginal Menu:") 
for i, items in pairs(Menu) do  
    print(m.Title(items))
end

Menu = {"Cheeseburger","hamburger","chicken burger","fries"} 

print("\nActual Menu:") 
for i, items in pairs(Menu) do  
    print(m.Title(items))
end
Buffet = {"Turkey","roast pork","chips","burgers","chicken nuggets","sandwich"}

print("\nTodays Buffet Menu:") --#Test. 
for i, food in pairs(Buffet) do
    print(m.Title(food))
end 

Buffet = {"turkey","pizzas","muffins","burgers","chicken wings"} 

print("\nTomorrows Buffet Menu:") 
for i, food in pairs(Buffet) do
    print(m.Title(food))
end 

table.remove(Buffet, 1)  


