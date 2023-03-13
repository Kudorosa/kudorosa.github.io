man_0 = {'colour': "black", 'money': 5} 
man_1 = {'colour': "white", 'money': 10} 
man_2 = {'colour': "blue", 'money': 20} 

enemies = [man_0, man_1, man_2] 
print(enemies) 

armed_men = [] 

for man in range(30): 
    armed_man =  {'colour': "black", 'gun': "pistol", 'money': 5}
    armed_men.append(armed_man) 
    
for man in armed_men[:3]: 
    if man['colour'] == "black":
        man['colour'] = "white"
        man['gun'] = "m4a1"
        man['money'] = 10
    elif man['colour'] == "white":
        man['colour'] = "blue"
        man['gun'] = "m242"
        man['money'] = 20 

for men in armed_men[:5]:
    print(men)
    print("-----------") 
    
print(("Enemies remaining: " + str(len(armed_men))).title()) 
    
pizza = {
    'crust': "stuffed crust", 
    'toppings': ["cheese","pepperoni","mushrooms","ham","pineapples"],
    }

print(f"can I have a {pizza['crust']} pizza with {pizza['toppings']} please?")

print(("\nHello, so you would like your Pizza to be " + pizza['crust'] +
" as well as having the following toppings added which are:").title()) 

for topping in pizza['toppings']: 
    print( topping.title() + ".")

print("\nis that correct sir?" "\nyes, that is correct!\n\n".title()) 

voting_results = {
    'james': ["grand theft bloxo"],
    'philip': ["book of death", "the vault escape"],
    'jack': ["grand theft bloxo", "my pizzeria"],
    'lisa': ["timeless souls", "grand theft bloxo"],
    'avneet': ["grand theft bloxo", "book of death"],
    'bob': ["timeless souls", "mortal bloxa"],
    } 

for name, games in voting_results.items(): 
    if len(games) == 1: 
        print(f"\n{name} has only voted for:\n".title()) 
    else:
        print(f"\n{name} has voted for:\n".title()) 
    for game in games: 
        print("'" + game.title() + "'" + ".") 

users = { 
    'kudorosa' : {
    'forename': "dean",
    'surname': "chinamo",
    'postcode': "Wolverhampton",
    },
    'avn_xo': {
    'forename': "avneet",
    'surname': "chima",
    'postcode': "england",
    },
} 

for username, information in users.items(): 
    print(f"\nGreetings {username}, Welcome to your account page.".title()) 
    print((f"\nyour account information:\n \tFull name: {information['forename']}" 
    f" {information['surname']} \n\tlocation: {information['postcode']}\n").title()) 
print("\n-------------") 
   
#Test V

lover = {
    'first_name': "avneet",
    'last_name': "chima",
    'age': "19",
    'location': "england", 
    } 
    
for info, details in lover.items(): 
    print(f"{info}: {details}.".title()) 
print("-------------") 
    
lover2 = { 
    'first_name': "grace", 
    'last_name': "stevenson",
    'age': "19",
    'location': "england",
    } 
    
for info, details in lover2.items(): 
        print(f"{info}: {details}.".title())
print("-------------") 

sorry = { 
    'first_name': "anatasia",
    'last_name': "raw",
    'age': "19",
    'location': "england",
    }
    
for info, details in sorry.items(): 
        print(f"{info}: {details}.".title())
print("-------------") 
    
people = [lover,lover2,sorry]

for person in people: 
    print(person) 

kudorosa = { 
    'name': "kudorosa",
    'type': "dog",
    'owner': "dean", 
    } 
    
kittykat = {
    'name': "kittykat", 
    'type': "cat",
    'owner': "katherine",
    }

avowulf = {
    'name': "avowulf",
    'type': "dog",
    'owner': "avneet",
}

pets = [kudorosa, kittykat, avowulf] 

for information in pets: 
    print("\n"+ str(information))
    

favourite_places = { 
    'avneet': ["italy, the united states of america, london"],
    'grace': ["the united states of america"],
    'harleen':["dubai"],
    }

for names, places in favourite_places.items(): 
    if len(places) < 2: 
        print("\n" + names.title() + "'s" + " favourite place is: ".title())
    else:
        print("\n" + names.title() + "'s" + " favourite places are: ".title())
    for place in places: 
        print("\t" + place.title() + ".") 

fav_numbers = { 
    'avneet': [42,38,100],
    'harleen': [69],
    'grace': [16,18],
    } 

for name, numbers in fav_numbers.items():
    if len(numbers) < 2:
        print("\n" + name.title() + "'s" + " favourite number is:".title()) 
    else:
        print("\n" + name.title() + "'s" + " favourite numbers are: ".title()) 
    for number in numbers: 
        print(str(number) + ".") 

cities = { 
    'london': {
    'population': "10+ Million",
    'country': "england",
    'fact': "place where most knife crime occurs.",
    },
    'wolverhampton':{
    'population': "1+ Million",
    'country': "england",
    'fact': "I lived here my whole life.",
    },
    'cape town': {
    'population': "100k+",
    'country': "south africa",
    'fact': "most dangerous city in africa.",
    }
}

for information, statistics in cities.items(): 
    print(("City: " + information + " - " + str(statistics)).title()) 

print(f"\nLondon: {cities['london']}".title())  
print(("\nWolverhampton: " + str(cities['wolverhampton'])).title())
print(f"\ncape town: {cities['cape town']}".title()) 

favorite_languages = { #Edit of the Example in the Python Crash Course Book. 
 'jen': ["python", "ruby"],
 'sarah': ["c"],
 'edward': ["ruby", "go"],
 'phil': ["python", "haskell"],
 'john': [],
 'david': ["c++", "html", "css"],
 'dean': ["python","lua"],
 }
 
for name, languages in favorite_languages.items():
    if len(languages) > 1: 
        print(f"\n{name.title()}'s","favourite language is:".title()) 
    elif len(languages) == 0:
        print(f"\nlooks like {name} has no favourite programming"
        " language, how sad...".title()) 
    else:
        print(f"\n{name.title()}'s","favorite languages are:".title())
    for language in languages:
        print(f"'{language}'".title())
#------------------------------------------------------------
        
foods = {
    'main course': ["steak","pizza","burger","lasagne","spaghetti bolognese"],
    'sides': ["chips","mash","gravy","wedgies","salad"],
    'snacks': ["crisps","fruit","chocolate"],
    'desserts': ["ice-cream","fudge","cake","apple pie","muffin"],
    } 
    
print("\nso, what are we having for lunch today?".title()) 
print("\nI had a feeling you would not ask!".title()) 
print("\nWell, here is the menu of items you can choose:\n".title()) 

for setting, food in foods.items():
    print(f"{setting}: {food}\n".title()) 
    
print(("wow, that is a lot of items to choose from! since it is dinner,"
" i will focus on the 'main course' and 'sides' and the \n'desserts' list!\n"
).title()) 

print("Hmm, everything is so good, my order will be: \n".title()) 

lisas_main_order = ["steak","mash","gravy","salads"] 

for food in lisas_main_order: 
    if food in foods['main course'] or foods['sides']: 
        print(food.title() + ",\n") 

lisas_main_order.append("muffin") 

print(f"and for dessert....i will have...\n".title()) 

for food in lisas_main_order: 
    if food in foods['desserts']: 
        print("a...." + food.title() + "!") 
        
print("\nalright, im done with my order haha, sorry it took so long..".title()) 
print(("no need to apologise lisa, it is fine, great, now im getting hungry.."
).title()) 

print("I will probably have something from the 'main course' and 'sides'"
" menu.".title()) 

deans_order = [] 

if "burger" in foods['main course']: 
    deans_order.append("burger") 
if "chips" in foods['sides']:
    deans_order.append("chips")
if len(deans_order) < 4: 
    print("I need more than that..".title()) 
    while len(deans_order) < 4: 
        for food in foods['main course']:
            deans_order.append(food)
            print(deans_order) 
if len(deans_order) >= 4: 
    print("alright, thats enough.\n".title()) 
    
print(deans_order)
deans_order = set(deans_order) 
print(deans_order) 

print("\nlet me remove some items, this is too much...".title()) 

deans_order.remove("spaghetti bolognese") 

print(str(len(deans_order)) + " items, nice, that should be enough.".title()) 

#---------------
grunt = {
    'armour': False, 
    'speed': "slow", 
    'gold': 5,
    }


money = grunt['gold'] 

print("Grunt slain, you've just earned " + str(money) + " Gold.") 




        
        


















    

        
    

    

 





