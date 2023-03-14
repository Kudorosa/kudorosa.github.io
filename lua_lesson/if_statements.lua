Cars = {"audi", "mercedes","bmw", "tesla", "toyota", "burger"}

for i, car in pairs(Cars) do 
    if car == "burger" then 
        Food = table.remove(Cars, #Cars)
        print("Haha, a "..Food:sub(1,1):upper()..Food:sub(2).." is not a Car Brand...")
    elseif car == "bmw" then 
        print(string.upper(car)) 
    else 
        print(car:sub(1,1):upper()..car:sub(2)) 
    end
end

Current_experience = 57.65
Experience_required = 100 
Experience_to_next_lvl = Experience_required - Current_experience

if Current_experience < Experience_required then 
    print("You Require "..Experience_to_next_lvl.."xp in-order to Level up!")
    while Current_experience <= Experience_required do 
        print("Monster Slain! +12.5xp") 
        print(Current_experience.." Experience!\n") 
        Current_experience = Current_experience + 12.5 
        if Current_experience >= Experience_required then 
            print("Monster Slain! +12.5xp") 
            print(Current_experience.." Experience!") 
            print("You Levelled Up!\n") 
        end 
    end
end 

Food = "Egg & Sausage McMuffin" 
---@diagnostic disable-next-line: param-type-mismatch
print(string.lower(Food) == "egg & sausage mcmuffin") 
print("\n"..Food) 

--Revision V 

Health = 125 
DamAge = 15 

if Health > DamAge then 
    print("Haha, you can't Defeat me!") 
    while Health > DamAge do 
        DamAge = DamAge * 1.25 
        Health = Health - DamAge 
        print("\n"..Health.." Health left!")
        print("Ouch, that Hurt!\n") 
        print("Hero was Hit for "..DamAge.." DamAge!\n")
        if Health < 20 then 
            print("Health is Low...") 
            if Health < 20 then 
                print("Now for the Finishing Blow Hero! It was Good Knowing you!") 
                Health = Health - DamAge 
                print("\nHero was Hit for "..DamAge.." DamAge!\n") 
                if Health < 0 then 
                    print(string.lower("Agghhhh, Nooooo, I needed..to...save, the World......"))
                    print("\n\t-Hero was Slain-") 
                end 
            end 
        end 
    end 
end 

The_code = {} 
for x=1, 1000000 do 
    table.insert(The_code, x) 
end 
print("($"..The_code[#The_code]..")") 
print("The Actual Take is about $"..The_code[#The_code] / 8 ..".") 
print("($"..The_code[#The_code]..")") 
print("The Actual Take is about ".."$"..The_code[#The_code] / 10 .. ".") 

Number = {} 

for num=1,10 do
    Cube = num ^ 2 
    table.insert(Number, Cube) 
end 
for i, n in pairs(Number) do 
    print(n) 
end 
print("\n") 
Numbo = {}

for num=1,10 do 
    table.insert(Numbo, num ^ 2) 
end 
for i, n in pairs(Numbo) do 
    print(n) 
end 
print("\n") 

Player_distance = 5000 
Car_distance = 100

if Player_distance > Car_distance then 
    print("You are Too Far Away from the Vehicle") 
    while Player_distance > Car_distance do 
        Difference_in_distance = Player_distance - Car_distance
        print("Travel "..Difference_in_distance.."m to get to the Car!") 
        Player_distance = Player_distance - 100
        if Difference_in_distance <= 100 then 
            print("Initiate Car Enter Animation") 
        end 
    end
end 

Food = "bURger" 
---@diagnostic disable-next-line: param-type-mismatch
print(string.lower(Food) == "burger") 

Sauce = "chili sauce" 

if Sauce ~= "ketchup" then 
    print("I said I wanted "..Sauce:sub(1,1):upper()..Sauce:sub(2)..", Not Ketchup!") 
end 

Age = 19 

if Age ~= 29 then 
    print("\nI'm way Younger than that!") 
end
Number_guessed = 20 
for x=17,23 do
    if x == Number_guessed then 
        print("\nYou're getting Close!") 
        break
    end
end 

Number_guessed2 = 19 
if Number_guessed2 == Age then
    print("\nBingo, thats my Age, Well Done!") 
end 

Deans_Age = 17 
Avneets_Age = 20 

if Deans_Age >= 18 and Avneets_Age >= 18 then 
    print("You two are 18+, you may pass")
else
    print("One of you is UnderAge, Please Show me your IDs!")
end 

if (Deans_Age >= 18) or (Avneets_Age >= 18) then 
    print("\nYou may Pass!") 
end 

Food = {"hotdog","burger","pizza","chips","sauce","soda"}
Veg = "salad"

for i, n in pairs(Food) do 
     if "burger" == n then 
        print(true) 
        break 
     end
end 

for i, n in pairs(Food) do 
    if Veg ~= n then 
        print("Why is there no "..Veg.." in a Restaurant?!") 
        break
    end 
end 

Gun = "m4a1" 

print("\nIs M4A1 == Gun? Obviously True...") 
print("m4a1" == Gun) 

print("Is Ak-47 == Gun? No, Theres only One Weapon, False...") 
print("ak-47" == Gun) 

print("\n") 

print(5 <= 5) 

print("Bill" ~= "bill") 

Height = 6.25
if Height <= 6.5 then
    print("Sorry, your too short to board this ride...") 
end 
Colours = {"Red","Blue","Yellow","Green","Orange"} 
print(string.lower(Colours[3]) == "yellow") 

for i, n in pairs(Colours) do 
    print("black" == n) 
end 

Age = 17
Identification = {"Drivers License","Photo ID","Birth Certificate"} 
for i, n in pairs(Identification) do 

    if "Drivers License" == n then 
                print("You have ID, please show me it!") 
            
        if "Passport" ~= n or "Photo ID" ~= n then 
            print("We Need more Documents off of you!") 

            if string.upper("Birth Certificate") ~= Identification[#Identification] then 
                print("You have a Foraged "..Identification[#Identification].." by the way....") 

                if "Photo ID1" == Identification[2] then 
                    print("your "..n.." is fine.") 
                end 
            end
        end 
    end 
end       

if Age >= 16 then 
    print("Oooo, looks like you can have some Intimate Action!") 
end

if Age <= 18 then 
    print(string.upper("Unfortuantely, you are too young to enter, please leave!"))
end

-- False V

Drinks = {"Beer","Spirits","Sake","Whiskey"} 
Age = 17 
for i, drink in pairs(Drinks) do 

    if "Champagne" == drink then  
        print("I want a Champagne.")  
    else
        print("\nThere is no Champagne.") 
        break
    end 
end

if Age >= 18 then 
    print("Hello, What Would you like to Drink Today!") 
else
    print(string.upper("Get lost kid, this is for 18+ Adults Only!"))
end

Money = 250
if Age == 17 and Money >= 300 then 
    print("Hello, would you like to book a Driving Test?") 
else 
    print("Unfortunately you don't have enough, $"..Money.." is $".. 300 - Money.." short...")
end 
    
if Money > 500 or Age > 18 then 
    print("Dude, we should go to a Nightclub, it will be fun!") 
else
    print("Wow, you are Broke and Underage, I'm leaving....")
end 

for i, drink in pairs(Drinks) do
    if "whiskey" == drink then 
        print("The Whiskey is out of stock!")
    else
        print("Oh wait, it is in stock, its reserved for a special person..") 
        break
    end 
end

print("Whiskey" == string.lower("Whiskey"))

print("Sake" ~= "sake") 

for i, drink in pairs(Drinks) do 
    if "Champagne" == drink then 
        print(true) 
        break 
    end 
end 

print(not true) 
    
Fact = true 
Rumour = not Fact 
print(Rumour) 

-- ----------------------------
print("\n\n") 

Person_age = 16 

if Person_age >= 17 then 
    print("You can now obtain a drivers license!") 
    print("Have you obtained your drivers license beforehand?") 
end

Age = 16 

if Age >= 17 then 
    print("You can apply for a Drivers License!") 
    print("Have you ever applied for a Drivers License before?") 
else  
    print("Unfortuately you do not meet the requirements to apply.") 
    print("Please try again once you are of the Age to do so!")
end
    
Age = 51
Price = 26

if Age <= 6 then 
    print("\nyou may enter free of charge, have fun!") 
elseif Age > 6 and Age >= 10 and Age <= 12 then
    print("\nyou will have to pay $"..Price / 4 .." to enter please.") -- elseif is a Conditonal Statement which only Runs when the Previous Test has Failed. 
elseif Age >= 12 and Age <= 15 then 
    print("\nHello, the fee to enter is $"..Price / 2 .." please!") 
elseif Age > 6 and Age < 10 then 
    print("\nplease pay $"..Price / 8 ..".") 
elseif Age >= 50 then 
    print("\nGreetings, Hope you are having a pleasant day, since you Qualify as a Senior, the Price is $"..Price / 5 .." please!") 
elseif Age >= 16 then 
    print("\nI see you are 16+, you will have to pay $"..Price.." please!") 
end 
    
Age = 50
Price = 26

if Age <= 6 then 
    Price = 0 
    print("\nyou may enter free of charge, have fun!") 
elseif Age > 6 and Age >= 10 and Age <= 12 then 
   Price = Price / 4 
elseif Age >= 12 and Age <= 15 then 
    Price = Price / 2
elseif Age > 6 and Age < 10 then 
   Price = Price / 8 
elseif Age >= 50 then 
    Price = Price / 5
else
    Price = Price
end 

print("\nyou will have to pay $"..Price.." to enter please!") 

Food = {"Beef","Cheese","Bacon"} 

for i, item in pairs(Food) do 
    if "beef" == item then  
        print("\n"..item[1].." has been added to your burger!") 
        if "cheese" == item then 
            print("adding "..item[2].." to your burger!") 
            if "ketchup" == item then
                print("a dollop of Ketchup added to your Burger!") 
            end 
        end 
    end 
end
print("\nBurger Complete, please collect your Burger!") 
print("Thank you for using Build-A-Burger!")

-- Test 2 V

Alien_colour = "Green"

if Alien_colour == "Green" then 
    print("\nYou have scored 5 Points!") 
    if Alien_colour == "Yellow" then 
        print("You have scored 10 points!") 
    end
end

if Alien_colour == "Green" then 
    print("\nYou have scored 5+ points!") 
else 
    print("You have scored 10 points!") 
end
    
if Alien_colour ~= "Green" then  
    print("You have scored 5++ Points!") 
else
    print("\nYou have scored 10 points!") 
end
    
if Alien_colour == "Green" then  
    print("\nYou have scored 5+++ points!") 
elseif Alien_colour == "Yellow" then 
    print("You have scored 10+!") 
else
    print("You have scored 15 points!") 
end

Alien_colour = "Yellow" 

if Alien_colour == "Green" then
    print("You have scored 5++++ points!") 
elseif Alien_colour == "Yellow" then
    print("\nYou have scored 10++ points!") 
else
    print("You have scored 15+ points!") 
end
    
Alien_colour = "Red" 

if Alien_colour == "Green" then 
    print("You have scored 5* points!") 
elseif Alien_colour == "Yellow" then 
    print("You have scored 10+++ points!") 
else 
    print("\nYou have scored 15+++ points!") 
end 
    
Stage_of_life = 19 

if Stage_of_life < 2 then 
    print("\nYou are a Baby.") 
elseif Stage_of_life >= 2 and Stage_of_life < 4 then
    print("\nYou are a Toddler.") 
elseif Stage_of_life >= 4 and Stage_of_life < 13 then 
    print("\nYou are a Kid.") 
elseif Stage_of_life >= 13 and Stage_of_life < 20 then 
    print("\nYou are a Teenager now!") 
elseif Stage_of_life >= 20 and Stage_of_life < 65 then
    print("\nYou are an Adult now, a lot of Responisibilty comes!") 
else
    print("\nYou are now an Elder with a Fulfilled Life!") 
end

Favourite_fruits = {"Lychee","Dragon Fruit","Pomegranate"} 
for i, fruit in pairs(Favourite_fruits) do 
    if "Bananas" == fruit then 
        print("You really like Bananas!") 
        if "Lychee" == fruit then 
            print("\nYou really like "..Favourite_fruits[1].."!") 
            if "Grapes" == fruit then 
                print("You really like Grapes!") 
                if "Dragon Fruit" == fruit then 
                    print("\nYou really love "..Favourite_fruits[2].."!") 
                    if "Pomegranate" == fruit then 
                        print("\nThe Final Fruit you like is "..Favourite_fruits[#Favourite_fruits]) 
                    end
                end
            end
        end
    end
end
    
----------------------------

Requested_topping = {"Pepperoni","Chili Flakes","Meatballs","Extra Cheese"}

for i, toppings in pairs(Requested_topping) do 
    print("\nAdding "..toppings.." to your pizza...") 
    if toppings:sub(1,1):upper()..toppings:sub(2) == "Pepperoni" then
        print("\nUnfortunately the 'Pepperoni' is Depleted...")
        print("Chef has been Notified....")
    else
        print(toppings.." has been added to your Pizza!") 
    end
end

print("\nYour pizza is ready to be retrieved, careful, its Hot!") 
 
Requested_toppings = {}

if Requested_toppings then --#Empty List Check. 
    for i, toppings in pairs(Requested_topping) do
        print("\nAdding "..toppings.." to your pizza...") 
        if toppings == "pepperoni" then
            print("\nUnfortunately the 'Pepperoni' is Depleted...")
            print("Chef has been Notified....")
    print(toppings.." has been added to your Pizza!") 
else
    print("\nYour pizza is Plain and Topping(less)...Do you want to continue?") 
end
        end
    end

Toppings = {}

if Toppings then
    for i, topping in pairs(Toppings) do 
        print("\nAdding "..topping.." to your pizza...") 
        print(topping.." has been added to your pizza!") 
    print("\nYour pizza is about to be made!")
        if not Toppings then
            print("\nWarning! No Toppings were Added to the Pizza, do you want to Continue?") 
        end
    end
end


    
Available_toppings = {"Ham","SausAge","Extra Cheese","Peppers",   
                            "Meatballs","Mushrooms","Sweetcorn"}
                            
Customers_order = {"Ham","Extra Cheese","Chili Flakes","Tomatos"} 

for i, topping in pairs(Customers_order) do
    for i, logic in pairs(Available_toppings) do
        if topping == logic then
            print("\nAdding "..topping.." to your pizza...") 
            print(topping.." has been added to your pizza...") 
        else
            print("\nAdding "..topping.." to your pizza...") 
            print("Unfortuantely we do not have "..topping.." at this time..") 
            break
        end
    end
end

print("\nYour Pizza is Ready to be Collected, Please Take Caution as it is Hot!") 
print("\n") 

--#Test V. 

Usernames = {"john","mary","peter","harleen","avneet","Administrator"} 
if Usernames then
    for i, username in pairs(Usernames) do  
        if string.lower(username) == "administrator" then
            print("\nGreetings "..Usernames[#Usernames]..", would you like to open up the Console Admin Menu?") 
        elseif username ~= "administrator" then 
            print("\nGreetings "..username:sub(1,1):upper()..username:sub(2)..", welcome back to Ucraft.")
else 
    print("\nMore Users are required in order to create a Ucraft server!") 
end 
end 
end
print("\n")

Current_users = {"john","mary","harleen","avneet","james"} 

New_users = {"MARY","JAMES","gibson","tyler","grace"}


for i, c in pairs(Current_users) do 
    for i, users in pairs(New_users) do 
        if string.lower(users) == c then 
            print("\nthe username "..users.." has been taken, please enter a new username.")
            table.remove(New_users, 1) 
            table.remove(New_users, 2)   
        elseif string.lower(users) ~= c then
            print("\nWelcome "..users.." to the Ucraft website, thank you for joining!") 
        end
    end
end
print("\n") 

Ordinal_numbers = {1,2,3,4,5,6,7,8,9,10} 

for i, number in pairs(Ordinal_numbers) do
    if number == 1 then
        print(number.."st")  
    elseif number == 2 then
        print(number.."nd") 
    elseif number == 3 then
        print(number.."rd") 
    else
        print(number.."th") 
    end
end
    
print("\n")         

Games = {"red dead redemption","red dead redemption 2","gta v","roblox","minecraft"} 
Installed_games = {"minecraft","roblox"}
Owned_games = {"gta v","roblox","minecraft"}

print(Games[4]:sub(1,1):upper()..Games[4]:sub(2).."\n") 

for i, game in pairs(Games) do 
    print("I love "..game:sub(1,1):upper()..game:sub(2).." so much, its so fun!") 
    print("My friends can't afford "..game:sub(1,1):upper()..game:sub(2).." so I have to play by myself..\n") 
end
    
for i, i_game in pairs(Installed_games) do
    print("\n"..i_game:sub(1,1):upper()..i_game:sub(2).." is already installed, would you like to Play?")
    for i, o_game in pairs(Owned_games) do
        if i_game == o_game then 
            print("\nYou Own "..i_game:sub(1,1):upper()..i_game:sub(2).." would you like to play?") 
        elseif i_game ~= o_game then
            print("\nYou Own "..o_game:sub(1,1):upper()..o_game:sub(2).." would you like to install it?")
        end
    end
end
   

        
Age = 19

if Age <= 2 then
    print("Baby") 
elseif Age >= 2 and Age < 6 then
    print("Toddler") 
elseif Age >= 6 and Age < 10 then 
    print("kid") 
elseif Age >= 10 and Age < 18 then 
    print("teenAger") 
else
    print("You are an Adult now!")
end
   

