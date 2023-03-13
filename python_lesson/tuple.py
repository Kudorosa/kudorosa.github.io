menu = ("burgers","pizzas","desserts","sides","drinks","extras") #A Tuple uses () which forms a List where Values cannot be Added or Removed. 
print(menu[2:4]) 

print("original menu:".title()) 
for items in menu: 
    print(items.title())

menu = ("Cheeseburger","hamburger","chicken burger","fries") 

print("\nactual menu:".title()) 
for items in menu:
    print(items.title()) 

buffet = ("Turkey","roast pork","chips","burgers","chicken nuggets","sandwich")

print("\ntodays buffet menu:".title()) #Test. 
for food in buffet: 
    print(food.title()) 

buffet = ("turkey","pizzas","muffins","burgers","chicken wings") 

print("\ntomorrows buffet menu:".title()) 
for food in buffet: 
    print(food.title()) 

del buffet[0] 



    
