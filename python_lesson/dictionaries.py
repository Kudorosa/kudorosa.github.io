print("hello python world!".title()) 

dean = {
    'age' : "19", 
    'profession' : "novice programmer", 
    'favourite hobby' : "gaming", 
    'love interest' : "avneet chima",
    } #A Dictionary is a List with a Key-Value. 
print(dean) 
print(("dean is " + str(dean['age']) + " years old now.").title()) 
print(f"dean is a {dean['profession']}.".title()) 
print(("deans favourite hobby is " + str(dean['favourite hobby']) + ".").title()) 
print(f"dean really likes {dean['love interest']}, he keeps thinking about her" 
" all the time...".title())

age = dean['age']
job = dean['profession']  
hobby = dean['favourite hobby'] 
love = dean['love interest'] 

print((f"\ndeans age is {age}, his 'job' or profession should I say is being a"
f" {job}, his favourite 'hobby' is {hobby} and the person he loves "
f"most is {love}.").title()) 

dean['favourite food'] = "lasagne"
dean['favourite company'] = "microsoft" 

print(dean['favourite food'].title()) 
print(dean['favourite company'].title()) 

print("Hello Python World!".title()) 

print("Hello dean, welcome to python! \nHere you will learn so much about me!".title()) 

programming_languages = [
    "Lua",
    "c#", "c++",
    "java","javascript",
    "html","css",
    "python",
    ] 

print(f"\n{programming_languages[0]} will be the next language you learn after"
" me but, we are so far away from that now haha!\n".title()) 
print((str(programming_languages[1]) + " is a optional language for you to"
" learn, but will prove beneficial!\n").title()) 
print(f"{programming_languages[2]} is also another optional language which is" 
" primariy used for mobile games!\n".title()) 
print((str(programming_languages[3]) + " is a programming language used to" 
" create software and websites.\n").title()) 
print(f"{programming_languages[4]} is quite a complex and is mainly used for" 
" website building and games!\n".title()) 
print((str(programming_languages[5]) + " is another website oriented"
" programming language for website building!\n").title()) 
print(f"{programming_languages[6]} or 'Cascading Style Sheets' is a website " 
"building programming language, same as 'hyper-text markup language!\n".title()) 
print(("\n\tand lastly, " + str(programming_languages[-1]) + " is the language" 
" you are learning right now!").title()) 

print("\nnow let us remove the languages that you do not need right now.".title()) 

del programming_languages[-2] 
del programming_languages[3]
programming_languages.remove("html") 
programming_languages.remove("javascript") 

print(programming_languages) 
print("\nnow, we have only a few programming languages for you to learn!".title()) 

print((f"the programming languages {programming_languages[1]} "
f"and {programming_languages[2]} will be learnt at a later time, "
"preferrably next year." "\nwhy you say? you only need to learn two "
"programming languages to be really good at programming, these are "
"\nmainly for mobile development which can wait.").title())

print(("\nI agree, I now must focus on " + str(programming_languages[-1]) + 
", then I will move onto Lua for Roblox..").title())  

print("\ngood, now go and make progress my apprentice!".title()) 

buffet = ("Roast pork","pizza","burgers","chips","steak","chicken","sushi") 

customers_order = ["sushi","burgers","pork","ham","chicken wings","ice-cream"] 
my_order = customers_order[:] 

customers_order.append("sausage rolls") 
my_order.append("chips")
my_order.append("pizza") 

for food in customers_order and my_order: 
    if food in buffet: 
        print(("\nalright, we have " + food + ".").title()) 
    elif food not in buffet: 
        print(f"\nwe do not serve {food} here sir.".title()) 

books = {'programming book': "python", 'ambition': "creating games"} 

print(f"\ntoday i am learning about {books['programming book']}!".title())

print(("hopefully one day after I learn all coding languages that I finally "
"start " + str(books['ambition']) + " all by myself!").title()) 
print(len(books)) 

knight_0 = {} 
print(knight_0) 

knight_0['colour'] = "silver"
print(knight_0) 
knight_0['sword type'] = "greatsword"
print(knight_0) 
knight_0['damage'] = "85-245dmg" 
print(knight_0) 
knight_0['spawns'] = "lost citadel and kings keep" 

print(knight_0) 

print(f"\nAlright, so the Knights general colour is {knight_0['colour']}, "
f"it wields a {knight_0['sword type']} and it deals "
f"about {knight_0['damage']}?!".title()) 

print("\nYes...")

print("\nWow, so where can we find this clearly overpowered foe?".title())
 
print(("\nwe can find the Knights usually at the " + str(knight_0['spawns']) + 
", I think we may need to level up first before-").title())
 
print((f"\nsplendid, let us journey forth to the " + str(knight_0['spawns']) +
" at once, make haste friend!").title()) 

print("\n....may our souls rest easy on this arduous journey...".title())

knight_0['souls'] = "5650" 
souls = knight_0['souls'] 

print(f"\nKnight slain, you have gained {souls} souls..".title()) 

print(("\nthe knights sword is a " + str(knight_0['sword type']) + 
", he still adorns a " + str(knight_0['colour']) + " colour pallete.").title()) 

knight_0['sword type'] = "Ultra-Greatsword" 
knight_0['colour'] = "Gold"

print(f"\nThe knights sword in now a {knight_0['sword type']} "
f"whilst his armour being emboldened into a {knight_0['colour']} colour!".title()) 

knight_0['speed'] = "normal" 
knight_0['block per second'] = 1

print(f"\nhmmm, the Knight movements are quite {knight_0['speed']}.".title()) 

if knight_0['speed'] == "slow":
    travel = 1  
elif knight_0['speed'] == "normal":
    travel = 2 
else: 
    travel = 3 

knight_0['block per second'] = knight_0['block per second'] + travel 

print(f"\nNew Block Travel distance: {knight_0['block per second']}".title()) 

print(knight_0['sword type']) 

del knight_0['sword type'] 

print(knight_0) 

voting_results = {
    'james': "grand theft bloxo",
    'philip': "book of death",
    'jack': "grand theft bloxo",
    'lisa': "timeless souls",
    'avneet': "grand theft bloxo",
    'bob': "timeless souls",
    } 
                
print(voting_results) 

print(("looks like james and jack want me to make a " + 
    str(voting_results['james']) + " game, amazing!").title()) 
    
#Test V

lover = {
    'first_name': "avneet",
    'last_name': "chima",
    'age': "19",
    'city': "wolverhampton", 
    } 

print("\n") 
print(f"forename: {lover['first_name']}".title()) 
print("----------------") 
print(f"surname: {lover['last_name']}".title()) 
print("----------------") 
print("age: ".title() + str(lover['age']))
print("----------------")  
print("City: ".title() + lover['city'].title()) 

fav_numbers = { 
    'avneet': 42, 
    'harleen': 69,
    'grace': 16, 
    } 

print("\n----------------") 
print(("\navneets favourite number is " + str(fav_numbers['avneet']) + "!\n"
).title()) 

print(("harleens favourite number is of course " + str(fav_numbers['harleen'])
+ "!\n").title()) 

print(f"graces favourite number has got to be {fav_numbers['grace']}!".title()) 

glossary = {
    'true': "this means the value is true and will run",
    'false': "this means the value is false and will not run",
    'variable': "holds any value for later use.",
    '=': "assigns a value.",
    '==': "checks to see if two values are equal.",
    } 
    
print("\n----------------") 
print(("\nThe term 'true', " + glossary['true'] + " any line of code.\n").title()) 
print(f"the term 'false', {glossary['false']} any line of code.\n".title())
print(("the term 'variable', it " + glossary['variable']).title()) 
print(f"\nthe symbol '=' {glossary['=']}".title()) 
print(("\nthe '==' symbol " + glossary['==']).title()) 
print("\n----------------\n") 

#-----------------------

user_1 = {
    'username': "kudorosa",
    'forename': "dean",
    'surname': "chinamo",
    } 

for info, details in user_1.items(): #.items() Returns a List of Key-Value Pairs. 
    if info == 'username' and details == "kudorosa":
        print(f"your {info} is {details}.\n".title())
    elif info == 'forename' and details == "dean": 
        print(("your " + info + " is " + details + ".\n").title()) 
    elif info == 'surname' and details == "chinamo":
        print(f"and your {info} is {details}.".title()) 

print((f"\ngreetings, {user_1['username']} ({user_1['forename']} "
f"{user_1['surname']})!").title()) 

for name, games in voting_results.items(): 
    print(f"\n{name}".title()+ " has voted for me to create".title(),
    f"'{games}'.".title()) 
   
for info, details in user_1.items(): 
    print(("\nTopic: " + info + "").title()) 
    print(("Informationd: " + details + "\n").title()) 

for names, games in voting_results.items(): 
    print((names + " voted for " + games + " to be made.\n").title()) 
    
for name in voting_results.keys(): #.keys() Returns a List of Keys only. 
    print("\nName: " + name.title() + ".") 

for game in voting_results.values(): #.values() Returns a List of Values only. 
    print("\nVoted Game Idea: " + game.title() + ".") 

crush = 'avneet' 
for name in voting_results.keys(): 
    print("\n" + name.title()) 
    
    if name in crush: 
        print(("Wow, Hello " + name + ", did not expect to see you here," 
        " I see you have voted for " + voting_results[name] + 
        " to be created" "!\ninteresting, I will fulfill your"
        " request this instant! \n\nTrust me, you will enjoy it!").title())
    
        if 'harleen' not in voting_results.keys():
            print("\nHarleen, please take part in the Vote, please!".title()) 
    
        if "assassins blox" not in voting_results.values(): 
            print("\nwow, no-one voted for an Assassins creed-esque game..".title()) 

for name in sorted(voting_results.keys()): 
    print(("\nthank you " + name + " for taking part in the Vote,"
    " it means a lot!").title())
    
    if name == 'avneet':
        print(f"{name}, I promise to make that game for you...".title()) 
        
print("\n\nA list of Game Ideas:".title()) 
for games in set(voting_results.values()): #set() Ensures there is no Repeats of Information.
    print(f"{games}.".title()) 

#Test V--------------------------------------------------------------------
glossary2 = {
    'true': "this means the value is true and will run",
    'false': "this means the value is false and will not run",
    'variable': "holds any value for later use",
    '=': "assigns a value",
    '==': "checks to see if two values are equal",
    'print': "displays any code written inside it",
    'set': "ensures Values are unique without any repeats",
    'append': "adds a value to the end of a list",
    'del': "permanently removes a list/variable/value",
    'pop': "removes a value but allows for it to be used",
    } 
print("\n----------------") 
for term, meaning in glossary2.items(): 
    print(("The Programming Term '" + term + "', " + meaning + ".\n").title())

print("----------------\n") 

rivers = {
    'nile': "egypt",
    'thames': "england",
    'yangtze': "china",
    'rio grande': "mexico",
    }

for river, country in rivers.items(): 
    print(("\nThe River " + river + " flows and runs through " + country 
    + ".").title()) 

print("\nList of Rivers:\n") 
for river in rivers.keys(): 
    print(("River " + river + ".").title()) 
    
print("\nList of Countries:\n") 
for country in rivers.values(): 
    print(country.title() + ".") 

print("\n----------------\n") 

voters = ['avneet','harleen','jess','bob','james','lisa','grace']

for name in voters: 
    if name in voting_results.keys(): 
        if name == 'avneet':
            print(name.title() + "! \n") 
        print(("Greetings " + name + ", I see you already voted!\n").title()) 
    else:
        print(("Welcome " + name + ", please take part in the Vote.\n").title()) 

#-------------------------------

food = ["ham","cheese","ham","sausage","ham","egg","cheese","ham"] 

def items(item): 
    """ """ 
    pack = ("\nthere are " + str(food.count(item)) + " pieces of " + item  + 
            " in the fridge.")
    if food.count(item) == 1:
        pack = ("\na " + item  + " is in the fridge.")
    return pack.title() 
    
bag = items("ham") 
print(bag) 

bag = items("cheese") 
print(bag)

bag = items("sausage") 
print(bag)

bag = items("egg") 
print(bag) 
     



    

    






























