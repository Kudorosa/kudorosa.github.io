M = require("helpful_functions")

print("Hello Lua World!") 

Dean = {
    Age ="19", 
    Profession = "novice programmer", 
    Favourite_hobby = "gaming", 
    Love_interest = "avneet chima",
    } --#A Dictionary is a List with a Key-Value. 

print("\n|-- About Dean A Chinamo --|\n") 
for i, info in pairs(Dean) do 
    print(i.." - "..M.Title(info)) 
end
print("Dean is "..M.Title(Dean["Age"]).." years old now.")
print("Dean is a "..M.Title(Dean["Profession"])..".") 
print("Deans favourite hobby is "..M.Title(Dean["Favourite_hobby"])..".")
print("Dean really likes "..M.Title(Dean["Love_interest"])..
" he keeps thinking about her all the time...")

Age = Dean["Age"]
Job = M.Title(Dean["Profession"])  
Hobby = M.Title(Dean["Favourite_hobby"])
Love = M.Title(Dean["Love_interest"]) 

print("\nDeans Age is "..Age.." his 'job' or Profession should I say is".. 
" being a "..Job..", his favourite 'hobby' is "..Hobby.." and the person".. 
" he loves most is "..Love..".\n") 

Dean["Favourite_food"] = "lasagne"
Dean["Favourite_company"] = "microsoft" 

print(M.Title(Dean["Favourite_food"])) 
print(M.Title(Dean["Favourite_company"]).."\n")

print("Hello Lua World!") 

print("Hello Dean, Welcome to Lua! \nHere you will Learn so much about".. 
" me!") 

Programming_languages = {
    "Lua",
    "c#", "c++",
    "java","javascript",
    "html","css",
    "python",
} 

print("\n"..Programming_languages[1].." will be the next language you learn"..
" after me but, we are so far away from that now haha!\n") 
print(M.Title(Programming_languages[2]).." is a optional language for you to"..
" learn, but will prove beneficial!\n")
print(M.Title(Programming_languages[3]).." is also another optional language which is".. 
" primariy used for mobile games!\n") 
print(M.Title(Programming_languages[4]).." is a programming language used to".. 
" create software and websites.\n") 
print(M.Title(Programming_languages[5]).." is quite a complex and is mainly used for".. 
" website building and games!\n") 
print(M.Title(Programming_languages[6]).." is another website oriented"..
" programming language for website building!\n") 
print(M.Title(Programming_languages[7]).." or 'Cascading Style Sheets' is a website".. 
" building programming language, same as 'Hyper-Text Markup Language!\n") 
print("\n\tand lastly, "..M.Title(Programming_languages[#Programming_languages])..
" is the language you are learning right now!") 

print("\nNow let us remove the languages that you do not need right now.") 

table.remove(Programming_languages, 7)
table.remove(Programming_languages, 5)
table.remove(Programming_languages, 4)
table.remove(Programming_languages, 2)

for i, language in pairs(Programming_languages) do 
    print(M.Title(language))
end
print("\nNow, we have only a few programming languages for you to learn!") 

print("the programming languages "..M.Title(Programming_languages[2])..
" and "..M.Title(Programming_languages[3]).." will be learnt at a later time,"..
" preferrably next year.".."\nwhy you say? you only need to learn two"..
" programming languages to be really good at programming, these are"..
" \nmainly for mobile development which can wait.")

print("\nI agree, I now must focus on "..
M.Title(Programming_languages[#Programming_languages])..
", then I will move onto Lua for Roblox..")  

print("\nGood, Now go and make Progress my Apprentice!") 

Buffet = {"sushi","burgers","pork","ham","chicken wings","ice-cream","roast pork", "chicken"}

Customers_orders = {"sushi","burgers","pork","ham","chicken wings","ice-cream"} 
My_order = M.Clone(Customers_orders)

table.insert(Customers_orders, #Customers_orders, "sausage rolls") 
table.insert(My_order, #My_order, "chips")
table.insert(My_order, #My_order, "pizza") 


for i, buffet in pairs(Buffet) do
    for i, food in pairs(Customers_orders and My_order) do
        if food == buffet then
            print("\nAlright, we have "..M.Title(food)..".") 
        else 
            print("\nWe do not Serve "..M.Title(food).." here Sir.") 
        end
    end
    break
end
Books = {Programming_book = "lua", Ambition = "creating games"} 

print("\nToday I am learning about "..M.Title(Books["Programming_book"]).."!")

print("Hopefully one day after I learn all Coding Languages that I Finally"..
" start "..M.Title(Books["Ambition"]).." all by myself!") 
print(#Books)

Knight = {} 
for i, stat in pairs(Knight) do
    print(i.." : "..M.Title(stat)) 
end 

print("\n") 
Knight["Colour"] = "silver"

for i, stat in pairs(Knight) do
    print(i.." : "..M.Title(stat)) 
end 

print("\n") 
Knight["Sword_type"] = "greatsword"

for i, stat in pairs(Knight) do
    print(i.." : "..M.Title(stat)) 
end 

print("\n") 
Knight["Damage"] = "85-245dmg" 

for i, stat in pairs(Knight) do
    print(i.." : "..M.Title(stat)) 
end 

print("\n") 
Knight["Spawns"] = "lost citadel and kings keep" 
 
for i, stat in pairs(Knight) do
    print(i.." : "..M.Title(stat)) 
end 

print("\nAlright, so the Knights general colour is "..M.Title(Knight["Colour"])..","..
" it wields a "..M.Title(Knight["Sword_type"]).."..and it deals"..
" about "..M.Title(Knight["Damage"]).."?!") 

print("\nYes...")

print("\nWow, so where can we find this clearly overpowered foe?")
 
print("\nwe can find the Knights usually at the "..M.Title(Knight["Spawns"])..
", I think we may need to level up first before-")
 
print("\nsplendid, let us journey forth to the "..M.Title(Knight["Spawns"])..
" at once, make haste friend!") 

print("\n....may our Souls rest easy on this arduous journey...")

Knight["Souls"] = "5650" 
Souls = Knight["Souls"] 

print("\nKnight slain, you have gained "..Souls.." Souls..") 

print("\nthe knights sword is a "..M.Title(Knight["Sword_type"])..
", he still adorns a "..M.Title(Knight["Colour"]).." colour pallete.") 

Knight["Sword_type"] = "Ultra-Greatsword" 
Knight["Colour"] = "Gold"

print("\nThe knights sword in now a "..M.Title(Knight["Sword_type"])..
" whilst his armour being emboldened into a "..M.Title(Knight["Colour"]).." colour!") 

Knight["Speed"] = "normal" 
Knight["Block_per_second"] = 1

print("\nhmmm, the Knight movements are quite "..M.Title(Knight["Speed"])..".") 

if Knight["Speed"] == "slow" then
    Travel = 1  
elseif Knight["Speed"] == "normal" then
    Travel = 2 
else
    Travel = 3 
end

Knight["Block_per_second"] = Knight["Block_per_second"] + Travel 

print("\nNew Block Travel distance = "..Knight["Block_per_second"]..".") 

print(M.Title(Knight["Sword_type"]))

table.remove(Knight, Knight[#Knight]) 

for i, stat in pairs(Knight) do 
    print(i.." : "..stat) 
end

print("\n") 

Voting_results = {
    James = "grand theft bloxo",
    Philip = "book of death",
    Jack = "grand theft bloxo",
    Lisa = "timeless Souls",
    avneet = "grand theft bloxo",
    bob = "timeless Souls",
    } 
                
for i, votes in pairs(Voting_results) do
    print(M.Title(votes)) 
end

print("\n") 

print("looks like James and Jack want me to make a "..Voting_results["James"]..
" game, amazing!") 
    
--#Test V

Lover = {
    First_name = "avneet",
    Last_name = "chima",
    Age = "19",
    City = "wolverhampton", 
    } 

print("\n") 
print("Forename = "..M.Title(Lover["First_name"])) 
print("----------------") 
print("Surname = "..M.Title(Lover["Last_name"])) 
print("----------------") 
print("Age = "..Lover["Age"])
print("----------------")  
print("City = "..M.Title(Lover["City"])) 

Fav_numbers = { 
    Avneet = 42, 
    Harleen = 69,
    Grace = 16, 
    } 

print("\n----------------") 
print("\nAvneet's favourite number is "..Fav_numbers["Avneet"].."!\n"
) 

print("Harleen's favourite number is of course "..Fav_numbers["Harleen"].."!\n") 

print("Grace's favourite number has got to be "..Fav_numbers["Grace"].."!") 

Glossary = {
    True = "this means the value is True and will run",
    False = "this means the value is False and will not run",
    Variable = "holds any value for later use.",
    Assign = "Assigns a value.",
    Equal = "checks to see if two values are Assign.",
    } 
    
print("\n----------------") 
print("\nThe term True, "..Glossary["True"].." any line of code.\n") 
print("the term False, "..Glossary["False"].." any line of code.\n")
print("the term Variable, it "..Glossary["Variable"]..".") 
print("\nthe symbol Assign "..Glossary["Assign"]..".") 
print("\nthe Equal symbol "..Glossary["Equal"]..".") 
print("\n----------------\n") 

--#-----------------------

User = {
    Username = "kudorosa",
    Forename = "Dean",
    Surname = "chinamo",
    } 

for info, details in pairs(User) do -- #.items() Returns a List of Key-Value Pairs. 
    if info == User["Username"] and details == "kudorosa" then 
        print("your "..info.." is "..details.."\n")
    elseif info == User["Forename"] and details == "Dean" then 
        print("your "..info.." is "..details..".\n") 
    elseif info == User["Surname"] and details == "chinamo" then
        print("and your "..info.." is "..details..".") 
    end
end

print("\nGreetings, "..M.Title(User["Username"]).."("..M.Title(User["Forename"])..
" "..M.Title(User["Surname"])..")!") 

for name, games in pairs(Voting_results) do 
    print("\n"..M.Title(name).." has voted for me to create "..M.Title(games)..".") 
end
   
for info, details in pairs(User) do
    print("\nTopic = "..info..".") 
    print("Information = "..M.Title(details).."\n") 
end

for names, games in pairs(Voting_results) do 
    print(M.Title(names).." voted for "..M.Title(games).." to be made.\n") 
end 

for keys, name in pairs(Voting_results) do  --#.keys() Returns a List of Keys only. 
    print("\nName = "..M.Title(keys)..".") 
end

for keys, game in pairs(Voting_results) do --#.values() Returns a List of Values only. 
    print("\nVoted Game Idea = "..M.Title(game)..".") 
end

Crush = "Avneet" 
for keys, name in pairs(Voting_results) do
    print("\n"..M.Title(name)) 

    if keys == Crush then 
        print("Wow, Hello "..M.Title(keys)..", did not expect to see you here,".. 
        " I see you have voted for "..M.Title(Voting_results[name])..
        " to be created! \ninteresting, I will fulfill your"..
        " request this instant! \n\nTrust me, you will enjoy it!")
    
        if 'harleen' ~= keys then
            print("\nHarleen, please take part in the Vote, please!") 
    
            if "assassins blox" ~= name then 
                print("\nwow, no-one voted for an Assassins creed-esque game..") 
            end
        end
    end
end

table.sort(Voting_results) 

for voter, idea in pairs(Voting_results) do 
    print("\nthank you "..M.Title(voter).." for taking part in the Vote,"..
    " it means a lot!")
    
    if M.Title(voter) == "Avneet" then
        print(M.Title(voter).." I promise to make that Game for you...")  
    end
end
        
print("\n\nA list of Game Ideas:") 
table.sort(Voting_results) 

for voter, idea in pairs(Voting_results) do  -- #set() Ensures there is no Repeats of Information.
    print(M.Title(idea)..".")
end
-- #Test V--------------------------------------------------------------------
Glossary2 = {
    True = "this means the Value is True and will run",
    False = "this means the Value is False and will not run",
    Variable = "holds any value for later use",
    Assign = "Assigns a value",
    Equal = "checks to see if two values are Equal",
    Print = "displays any code written inside it",
    Set = "ensures Values are unique without any repeats",
    Append = "adds a value to the end of a list",
    Del = "permanently removes a list/Variable/value",
    Pop = "removes a value but allows for it to be used",
    } 
print("\n----------------") 
for term, meaning in pairs(Glossary2) do
    print("The Programming Term '"..term.."', "..meaning..".\n")
end

print("----------------\n") 

Rivers = {
    Nile = "egypt",
    Thames = "england",
    Yangtze = "china",
    Rio_grande = "mexico",
    }

for river, country in pairs(Rivers) do
    print("\nThe River "..M.Title(river).." flows and runs through "..M.Title(country)..".") 
end

print("\nList of Rivers:\n") 
for river, values in pairs(Rivers) do
    print("River "..M.Title(river)..".") 
end
    
print("\nList of Countries:\n") 
for keys, country in pairs(Rivers) do
    print(M.Title(country)..".") 
end

print("\n----------------\n") 

Voters = {"avneet",'harleen','jess', "bob", "james", "lisa",'grace'}

for keys, name in pairs(Voters) do
    if name == keys then 
            if name == "avneet" then
                print(name.."! \n") 
            print("Greetings "..name..", I see you already voted!\n") 
        else
            print("Welcome "..name..", please take part in the Vote.\n") 
        end
    end
end

--#-------------------------------

Food = {"ham","cheese","ham","sausage","ham","egg","cheese","ham"} 

function Items(a) 
    --[[Improvised .Count() Function to Count Number of Occurrences.]]--
    local count = 0 
    for i, item in pairs(Food) do 
        local string = item
        for x in string:gmatch(a) do
            count = count + 1 
        end
    end
    print(count)
end


Bag = Items("ham") 

Bag = Items("cheese") 

Bag = Items("sausage") 

Bag = Items("egg") 



