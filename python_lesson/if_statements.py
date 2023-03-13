cars = ["audi","mercedes","bmw","tesla","toyota","burger"] 

for car in cars: 
    if car == "burger": # if is a statement which decides whether a Code Block runs or not when given a Condition, if True, the Code Block will run, False and it won't.
        food = cars.pop(-1) 
        print(("haha, a " + food + " is not a car brand...").title()) 
    elif car == "bmw": 
        print(car.upper()) 
    else: # else is a Statement which Runs once all Conditions have failed.
        print(car.title()) 
       
current_experience = 57.65
experience_required = 100
experience_to_next_lvl = experience_required - current_experience

if current_experience < experience_required:
    print("you require".title(),experience_to_next_lvl,"xp in order to level up!".title()) 
while current_experience <= experience_required: # while is a Statement which loops a Code Block. 
    print("monster slain! +12.5xp".title()) 
    print(current_experience,"Experience!\n") 
    current_experience += 12.50
if current_experience >= experience_required:
    print("monster slain! +12.5xp".title()) 
    print(current_experience,"Experience!") 
    print("You levelled up!".title()) 


food = "Egg & Sausage McMuffin"
print(food.lower() == "egg & sausage mcmuffin")
print(food) 


#Revision V

health = 125 
damage = 15

if health > damage: 
    print("Haha, you cant defeat me!".title()) 
while health > damage: 
    damage *= 1.25
    health -= damage
    print("\n",health,"health left!".title()) 
    print("ouch, that hurt!\n".title()) 
    print("Hero was hit for".title(),damage,"damage!\n".title()) 
if health < 20: 
    print("Health is low...".title()) 
if health < 20:
    print("Now for the finishing blow hero, it was good knowing you!".title())
    health -= damage
    print("\nHero was hit for".title(),damage,"damage!\n".title())
if health < 0: 
    print("Aghhhhh, noooooo, I needed to save, the.....world".lower()) 
    print("\n\t-Hero was slain-".title()) 
    
the_code = list(range(1,1000001)) 
print(f"£{max(the_code)}") 
print(f"The actual take is about £{max(the_code) / 8}.".title())  
print("£" + str(max(the_code))) 
print(("The actual take is about " + "£" + str(max(the_code) / 10) + ".").title()) 

number = [] 

for num in range(1,11): 
    cube = num ** 2 
    number.append(cube) 
print(number)

numbo = [] 

for num in range(1,11): 
    numbo.append(num ** 2) 
print(numbo)

chad_number = [num ** 2 for num in range(1,11)] 
print(chad_number)


player_distance = 5000 
car_distance = 1000 

if player_distance > car_distance: 
    print("you are too far away from vehicle!".title()) 
while player_distance > car_distance: 
    difference_in_distance = player_distance - car_distance
    print(f"Travel {difference_in_distance}m","to get to car!".title()) 
    player_distance -= 1000
    if difference_in_distance <= 100: 
        print("(Initiate Car Enter Animation)") 
    
food = "bURger" 
print(food.lower() == "burger") 

sauce = "chili sauce" 

if sauce != "ketchup": 
    print(f"I said I want {sauce}, not ketchup!".title()) 
        
age = 19 

if age != 29: 
    print("\nIm way younger than that!".title()) 
number_guessed = 20
if number_guessed in range(17,23):
    print("\nyou are getting close!".title()) 
number_guessed2 = 19
if number_guessed2 == age: 
    print("\nBingo, thats my age, well done!".title()) 


deans_age = 17 
avneets_age = 20 

if deans_age >= 18 and avneets_age >= 18: # 'and' combines the Conditons which makes it so all Conditions have to turn True to Run the Code Block.
    print("You two are 18+, you may pass!".title()) 
else:
    print("One of you are underage, please show me your IDs!".title()) 

if (deans_age >= 18) or (avneets_age >= 18): # 'or' makes it so a Code Block will Run as long as one Condition is True out of all other Conditons.
    print("\nyou may pass!".title()) 

food = ["hotdog","burger","pizza","chips","sauce","soda"] 
veg = "salad"

print("burger" in food) # 'in' checks for a Specific Value in a List and turns to True if a Value is found in the List. 

if veg not in food: # 'not' checks if the Specific Value is not in a List and turns to True if the Value is not found inside the List. 
    print(f"why is there no {veg} in a restaurant?!".title()) 

#Test

gun = "m4a1" 

print("\nis m4a1 == gun? Obviously True...".title())
print("m4a1" == gun) 

print("\nis ak-47 == gun? No, theres only one weapon, False...".title()) 
print("ak-47" == gun) 

print("\n") 

print(5 <= 5) 

print("Bill" != "bill") 

height = 6.25
if height <= 6.5:
    print("sorry, your too short to board this ride...".title()) 
    
colours = ["Red","Blue","Yellow","Green","Orange"] 
print(colours[-3].lower() == "yellow") 

print("Black" not in colours) 

age = 17
identification = ["Drivers License","Photo ID","Birth Certificate"] 

if "Drivers License" in identification:
    print("You have ID, please show me it!".title()) 
    
if "Passport" not in identification or "Photo ID" not in identification:
    print("We Need more Documents off of you!".title()) 

if "Birth Certificate".upper() != identification[-1]: 
    print(f"You have a foraged {identification[-1]} by the way....".title()) 

if "Photo ID1" == identification[1]: 
    print(f"your {identification} is fine.".title()) 
    
if age >= 16:
    print("Oooo, looks like you can have some intimate action!".title()) 

if age <= 18: 
    print("unfortuantely, you are too young to enter, please leave!".title())

#False V

drinks = ["Beer","Spirits","Sake","Whiskey"] 
age = 17 
if "Champagne" in drinks: 
    print("I want a Champagne.".title())  
else:
    print("\nThere is no champagne.".title()) 

if age >= 18: 
    print("Hello, what would you like to drink today!".title()) 
else: 
    print("Get lost kid, this is for 18+ adults only!".title()) 

money = 250
if age == 17 and money >= 300:
    print("Hello, would you like to book a Driving Test?".title()) 
else: 
    print(f"Unfortunately you dont have enough, £{money} is £{300 - money} short...".title())
    
if money > 500 or age > 18:
    print("Dude, we should go to a Nightclub, it will be fun!".title()) 
else: 
    print("wow, you are broke and underage, i am leaving....".title())

if "whiskey".title() not in drinks: 
    print("The Whiskey is out of stock!".title())
else: 
    print("Oh wait, it is in stock, its reserved for a special person..".title()) 

print("Whiskey" == "Whiskey".lower()) 

print("Sake" != "sake".title()) 

print("Champagne" in drinks) 

print(not True) 
    
fact = True 
rumour = not fact 
print(rumour) 

#------------------------
print("\n\n") 

person_age = 16 

if person_age >= 17:
    print("You can now obtain a drivers license!".title()) 
    print("Have you obtained your drivers license beforehand?".title()) 

age = 16 

if age >= 17: 
    print("You can apply for a Drivers License!".title()) 
    print("Have you ever applied for a Drivers License before?".title()) 
else: 
    print("Unfortuately you do not meet the requirements to apply.".title()) 
    print("Please try again once you are of the Age to do so!".title()) 
    
age = 51
price = 26

if age <= 6:
    print(f"\nyou may enter free of charge, have fun!".title()) 
elif age > 6 and age >= 10 and age <= 12:
    print(f"\nyou will have to pay £{price / 4} to enter please.".title()) # elif is a Conditonal Statement which only Runs when the Previous Test has Failed. 
elif age >= 12 and age <= 15:
    print(f"\nHello, the fee to enter is £{price / 2} please!".title()) 
elif age > 6 and age < 10:
    print(f"\nplease pay £{price / 8}.".title()) 
elif age >= 50:
    print(f"\nGreetings, Hope you are having a pleasant day, since you Qualify as a Senior, the price is £{price / 5} please!".title()) 
elif age >= 16:
    print(f"\nI see you are 16+, you will have to pay £{price} please!".title()) 
    
age = 50
price = 26

if age <= 6:
    price = 0 
    print(f"\nyou may enter free of charge, have fun!".title()) 
elif age > 6 and age >= 10 and age <= 12:
   price /= 4 
elif age >= 12 and age <= 15:
    price/= 2
elif age > 6 and age < 10:
   price /= 8 
elif age >= 50:
    price /= 5
else: 
    price = price

print(f"\nyou will have to pay £{price} to enter please!".title()) 

food = ("Beef","Cheese","Bacon") 

if "beef".title() in food: 
    print(f"\n{food[0]} has been added to your burger!".title()) 
if "cheese".title() in food:
    print(f"adding {food[1]} to your burger!".title()) 
if "ketchup".title() in food: 
    print("a dollop of Ketchup added to your Burger!".title()) 

print("\nBurger Complete, please collect your Burger!".title()) 
print("Thank you for using Build-A-Burger!".title())

#Test 2 V

alien_colour = "Green"

if alien_colour == "Green":
    print("\nYou have scored 5 Points!".title()) 
if alien_colour == "Yellow":
    print("You have scored 10 points!") 

if alien_colour == "Green":
    print("\nYou have scored 5+ points!".title()) 
else: 
    print("You have scored 10 points!".title()) 
    
if alien_colour != "Green": 
    print("You have scored 5++ Points!".title()) 
else:
    print("\nYou have scored 10 points!".title()) 
    
if alien_colour == "Green": 
    print("\nYou have scored 5+++ points!".title()) 
elif alien_colour == "Yellow":
    print("You have scored 10+!".title()) 
else:
    print("You have scored 15 points!".title()) 

alien_colour = "Yellow" 

if alien_colour == "Green": 
    print("You have scored 5++++ points!".title()) 
elif alien_colour == "Yellow":
    print("\nYou have scored 10++ points!".title()) 
else:
    print("You have scored 15+ points!".title()) 
    
alien_colour = "Red" 

if alien_colour == "Green":
    print("You have scored 5* points!".title()) 
elif alien_colour == "Yellow":
    print("You have scored 10+++ points!".title()) 
else:
    print("\nYou have scored 15+++ points!".title()) 
    
stage_of_life = 19 

if stage_of_life < 2: 
    print("\nYou are a Baby.".title()) 
elif stage_of_life >= 2 and stage_of_life < 4:
    print("\nYou are a Toddler.".title()) 
elif stage_of_life >= 4 and stage_of_life < 13: 
    print("\nYou are a Kid.".title()) 
elif stage_of_life >= 13 and stage_of_life < 20: 
    print("\nYou are a Teenager now!".title()) 
elif stage_of_life >= 20 and stage_of_life < 65: 
    print("\nYou are an Adult now, a lot of Responisibilty comes!".title()) 
else:
    print("\nYou are now an Elder with a Fulfilled Life!".title()) 

favourite_fruits = ["Lychee","Dragon Fruit","Pomegranate"] 

if "Bananas" in favourite_fruits: 
    print("You really like Bananas!".title()) 
if "lychee".title() in favourite_fruits: 
    print(f"\nYou really like {favourite_fruits[0]}!".title()) 
if "Grapes" in favourite_fruits: 
    print("You really like Grapes!".title()) 
if "dragon fruit".title() in favourite_fruits: 
    print("\nYou really love ".title() + str(favourite_fruits[1]) + "!") 
if "pomegranate".title() in favourite_fruits: 
    print(f"\nThe Final Fruit you like is {favourite_fruits[-1]}!".title()) 
    
#----------------------------

requested_toppings = ["Pepperoni","Chili Flakes","Meatballs","Extra Cheese"] 

for toppings in requested_toppings: 
    print(f"\nAdding '{toppings}' to your pizza...".title()) 
    if toppings == "pepperoni".title():
        print("\nUnfortunately the 'Pepperoni' is Depleted...".title())
        print("Chef has been Notified....".title())
    else:
        print(f"'{toppings}' has been added to your Pizza!".title()) 

print("\nYour pizza is ready to be retrieved, careful, its Hot!".title()) 
 
requested_toppings = [] 

if requested_toppings: #Empty List Check. 
    for toppings in requested_toppings: 
        print(f"\nAdding '{toppings}' to your pizza...".title()) 
    if toppings == "pepperoni".title():
        print("\nUnfortunately the 'Pepperoni' is Depleted...".title())
        print("Chef has been Notified....".title())
    print(f"'{toppings}' has been added to your Pizza!".title()) 
else:
    print("\nYour pizza is Plain and Topping(less)...Do you want to continue?".title()) 

toppings = [] 

if toppings: 
    for topping in toppings: 
        print(f"\nAdding {topping} to your pizza...".title()) 
        print(f"{topping} has been added to your pizza!".title()) 
    print("\nYour pizza is about to be made!".title())
else:
    print("\nWarning! No Toppings were Added to the Pizza, do you want to Continue?".title()) 
    
    
available_toppings = ["Ham","Sausage","Extra Cheese","Peppers",   
                            "Meatballs","Mushrooms","Sweetcorn"] 
                            
customers_order = ["Ham","Extra Cheese","Chili Flakes","Tomatos"] 

for topping in customers_order: 
    if topping in available_toppings: 
        print(f"\nadding {topping} to your pizza...".title()) 
        print(f"{topping} has been added to your pizza...".title()) 
    else:
        print(f"\nadding {topping} to your pizza...".title()) 
        print(f"Unfortuantely we do not have {topping} at this time..".title()) 

print("\nyour pizza is ready to be collected, take caution as it is hot!".title()) 
print("\n") 

#Test V. 

usernames = ["john","mary","peter","harleen","avneet","Administrator"] 
if usernames: 
    for username in usernames: 
        if username == "administrator".title(): 
            print(f"\nGreetings " + usernames[-1] + ", would you like to open up the Console Admin Menu?".title()) 
        else: 
            print(("\nGreetings " + username + ", welcome back to Ucraft.").title())
else: 
    print("\nMore Users are required in order to create a Ucraft server!".title()) 
print("\n")

current_users = ["john","mary","harleen","avneet","james"] 

new_users = ["MARY","JAMES","gibson","tyler","grace"] 

for users in new_users: 
    if users.lower() in current_users: 
        print(f"\nthe username '{users}' has been taken, please enter a new username.".title()) 
    else:
        print(f"\nWelcome '{users}' to the Ucraft website, thank you for joining!".title()) 
print("\n") 

ordinal_numbers = list(range(1,10)) 

for number in ordinal_numbers:
    if number == 1:
        print(f"\n{number}st")  
    elif number == 2:
        print(f"\n{number}nd") 
    elif number == 3:
        print(f"\n{number}rd") 
    else: 
        print(f"\n{number}th") 
    
        

games = ["red dead redemption","red dead redemption 2","gta v","roblox","minecraft"] 
installed_games = ["minecraft","roblox"]
owned_games = ["gta v","roblox","minecraft"] 

print(games[:4]) 

for game in games: 
    print(f"I love {game} so much, its so fun!".title()) 
    print(f"My friends cant afford {game} so I have to play by myself..\n".title()) 
    
for game in installed_games and owned_games and games: 
    if game in games: 
        if game not in owned_games:
            print(f"you do not own {game}, would you like to Purchase it?".title())
        if game in owned_games and game not in installed_games:
            print(f"\nyou own {game} would you like to install it?".title()) 
        if game in installed_games: 
            print(("\n" + str(game) + " is already installed, would you like to play?").title()) 
    elif game not in installed_games and owned_games:
        print("There is no Games in your Library, redirecting to the Marketplace..".title()) 
    else: 
        print("Game Library empty!".title()) 
        
age = 19

if age <= 2: 
    print("Baby".title()) 
elif age >= 2 and age < 6: 
    print("Toddler".title()) 
elif age >= 6 and age < 10: 
    print("kid".title()) 
elif age >= 10 and age < 18: 
    print("teenager".title()) 
else:
    print("You are an Adult now!".title()) 
    
    
    

    







    
    
    

    
































