#Last Test--------------
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

import printing_functions_test as test
test.print_models(unprinted_designs, completed_models) 
test.show_completed_models(completed_models) 
#----------------------------------------------------------


def salutation(username): #'def' keyword defines a Function which tells Python the name of the Definition.
    """a simple joyous attitude to learing""" #""" is a type of comment called a 'docstring' which generates Documentation for the Functions.
    print("Greetings " + username.title() + "!")
#^ The Variable inside the Function Definition's () is called a 'Parameter' which is information a Function needs to do it's job. 
salutation("Dean") #A Value inside a Function Call's () is called a 'Arguement' which transmits a Value to the Function Definition Variable.

def display_message():
    """ """ 
    print("\nGreetings, today I am Learning about Pythons Functions!".title())

display_message()

def favourite_book(title):
    """ """ 
    print(("\nHello, my Favourite Book has got to be " + title + "!").title()) 

favourite_book("Harry Potter and the Order of the Pheonix") 


def pizza(toppings, size="4'"): 
    """Description of Pizza"""
    print(("\nHello, the Size of my Pizza will be about " + size + ".").title()) 
    print(("the Toppings which I would like on my Pizza are " + toppings + "."
    ).title()) 

pizza("16'","cheese, pepperoni and meatballs") #< Postional Argument.
pizza("12'","spicy sauce, jalapenos, cheese, peppers and meatballs") 


pizza(toppings = "cheese, pineapple, chicken and peppers", size = "8'") #< Key-Word Argument. 

pizza("cheese and pepperoni") #< Default Value Argument (Follows Postional Argument Rules.).

pizza(size = "2'", toppings = "cheese, sweetcorn, mushrooms and chorizo") 

#Pizza Toppings Versions V 
pizza("Sausage and cheese") 
pizza(toppings = "cheese") 

#Pizza Sizes Versions V 
pizza("chicken tikka and cheese","18'") 
pizza(toppings = "pepperoni, cheese and mushrooms", size = "24'") 
pizza(size = "26'", toppings = "mushrooms, cheese, jalapenos and peppers") 

#Test V----------------

def make_shirt(engraving, size_type="large"): 
    """Description of a Sizeable Shirt and Random Messages on it."""
    print(("\nThe shirt size is " + size_type + "!").title())
    print(("the message engraved on the Shirt reads, '" + engraving + "'."
    ).title())

make_shirt("Xtra Large","programming rules!") 
make_shirt(size_type = "medium", engraving = "-Xbox for life-") 

make_shirt("i love python")
make_shirt(size_type = "medium", engraving = "I love python") 
make_shirt(engraving = "I <3 Roblox!", size_type = "small") 

def describe_city(city, country="the united kingdom"):
    """Description regarding a City and a Country"""
    print(("\n" + city + " is a city, it is located in " + country + ".").title()) 

describe_city("London") 
describe_city("Cape town", country = "south africa") 
describe_city("Beijing", country = "china\n") 

def formatted_name(forename, surname, middle_name=""):
    """Getting a Formatted Full name"""
    if middle_name:
        full_name = forename + " " + middle_name + " " + surname
    else:
        full_name = forename + " " + surname
    return full_name.title() #return retrieves a Value from inside a Function and places it back to the place which called the Function.


print(formatted_name("avneet","chima")) 

name = formatted_name("dean","chinamo.","anotida") 
print(name)

def sandwich(bread, fillings): 
    """ """ 
    order = f"\nthe type of bread I want is {bread}. \nthe fillings I want are: {fillings}."
    return order.title() 

complete_order = sandwich("brown","cheese, bacon, tomatos and lettuce") 
print(complete_order) 



def human(forename, surname, age=""): 
    """ Humanoids name in a Dictionary """
    person = {'first': forename, 'last' : surname} 
    if age: 
        person['age'] = age
    return person
    
programmer = human("Dean","Chinamo",age = 27)
print(programmer)



def names(forename, surname, middle_name=""):
    """ """ 
    full_name = forename + " " + surname
    if middle_name:
        full_name = forename + " " + middle_name + " " + surname
    return full_name.title() 

quiz = False

while quiz: 
    print("\nPlease tell us your full name:".title())
    print("(Type 'q', 'quit' or 'exit' to Abandon this Session.)")  
    
    fore = input("Forename: ") 
    if fore.lower() == 'q' or fore == 'quit' or fore == 'exit':
        break
        
    mid = input("(Optional) Middle Name: ") 
    if mid.lower() == 'q':  
        break
        
    sur = input("Surname: ") 
    if sur.lower() == 'q' or sur == 'quit' or sur == 'exit':
        quiz = False
    
    formatted_name = names(fore,sur,mid) 
    print(("\nGreetings " + formatted_name + "!").title())
    question = input("Would you like to re-enter your details again? ".title()) 
    
    if question.lower() == "no": 
        print(("\nVery well, thank you for your submition " + formatted_name + 
        ".").title()) 
        quiz = False

#Test V-----------

def city_country(city, country): 
    """ City and Countries """ 
    resorts = {'city': city, 'country': country} 
    return resorts 
    
places = city_country("Beijing","china")
print(("\n" + places['city']+ ", " + places['country'] + "\n").title()) 

def make_album(name, title, tracks=""): 
    """ Artist's name and Album """ 
    info = {'artist_name': name, 'album_title': title} 
    if tracks: 
        info['number_of_tracks'] = tracks
    return info 

album = make_album("justin bieber","yummy",7) 
print(album) 

album = make_album("max ritcher","infra",8) 
print(album) 

album = make_album ("billie eilish","girls",15) 
print(album) 

while False: 
    print("\nHello, Please Tell me your Artist and their Album please.".title())
    artist = input("\nArtist's Name: ") 
    if artist.lower() == "q" or artist.lower() == "quit":
        break
    album_title = input("\nAlbum Name: ") 
    if album_title.lower() == "q" or album_title.lower() == "quit":
        break
    
    full_album = make_album(artist,album_title) 
    print(full_album) 
    question = input("\nWould You Like to Re-Enter Another Artist and Album? ")
    if question.lower() == "no":
        break
        
def greeting(names): 
    """ Greeting people in Lists """ 
    for name in names: 
        message = "Hello " + name + ", what a lovely day to meet you!"
        print("\n" + message.title())
        
people = ["Hannah","Avneet","Grace"] 
greeting(people) 
print("\n")

def votes(games, voted_games): 
    """ Votes which will turn into Games """
    while voted_games: 
        creation = voted_games.pop()
        print("Game Creation: ".upper() + creation.title() + "\n")
        games.append(creation)
        

def game_creation(games):
    """ Games which in turn will be created """ 
    print(f"\n{len(games)} Games to Create: ".upper()) 
    for game in games:
        print(game.title()) 

voted_games = ["timeless souls","grand theft bloxo","book of death",
            "unbound soul simulator","abandon the vault"] 
    
games = [] 
    
votes(games,voted_games[:]) #placing [:] on a List during a Function Call will make a Copy of the Original List.
game_creation(games) 
print(voted_games) 
     
    
#Test V--------------------------------        

magicians = ["rosandra","jess","arthur","avneet","kudorosa"]
great_magicians = []

def show_magicians(magicians): 
    """ Revealing the Magicians """
    for magician in magicians:
        print("\n" + magician.title() + ".")
    

def make_great(great_magicians, magicians): 
    """ Adding a Title to a Magician """
    while magicians:
        great = "the Great " + magicians.pop()
        great_magicians.append(great)
     
 
show_magicians(magicians)
make_great(great_magicians,magicians[:])

print(magicians) 
print(great_magicians)

#----------------------------------------------------

def make_pizza(*toppings): #* allows the Parameter to receive Multiple Arguments. 
    """ Collect Customers Order """ 
    print("\nYour Pizza will be made with the following toppings:".title()) 
    for topping in toppings: 
        print("'" + topping.title() + "'")
    
make_pizza("Ham") 
make_pizza("pepperoni","cheese","mushrooms","pineapples") 

def make_pizza(size, *toppings):
    """ Positional and Arbitary Arguments """ 
    print(("\nThe size of your pizza is " + str(size) + "', the toppings which"
        " were added are:").title()) 
    for topping in toppings: 
        print("~ '" + topping.title() + "'") 

make_pizza(18,"Cheese","pepperoni","chili peppers","meatballs") 
make_pizza(8,"Extra Cheese","pineapples","mushrooms","vegan meat") 


def create_profile(first, last, **additional_info):#Two '*' are used to allow Python to create an Empty Dictionary to store Key-Value Pairs. 
    """ Creating a User Profile as a Dictionary """ 
    profile = {} 
    profile['forename'] = first
    profile['surname'] = last
    for subject, info in additional_info.items(): 
        profile[subject] = info
    return profile

account = create_profile("Avneet","Chima", 
                        location = "Wolverhampton",
                        interest = "Fashion",
                        best_food = "Pizza") 
print(account) 
    

#Test V-----------------------

def make_sandwich(*fillings): 
    """ A Variety of Sandwiches """
    print(("\nso you want a sandwich with " + str(len(fillings)) + " fillings"
    " which consist of:").title()) 
    for item in fillings:
        print("- " + item.title())

make_sandwich("Tuna","egg","sausage")
make_sandwich("Steak","cheese","tomatos","lettuce") 
make_sandwich("bacon","lettuce","tomatos","black pepper","mayonnaise") 


def build_profile(forename, surname, **info): 
    """ Building a Profile in a Dictionary Format """ 
    profile = {} 
    profile['forename'] = forename
    profile['surname'] = surname 
    for key, value in info.items(): 
        profile[key] = value
    return profile

my_profile = build_profile("Dean","Chinamo", 
                        hobby = "programming",
                        lover = "Avneet",
                        language = "English")
print(my_profile)



def selected_car(make, model, **specs): 
    """ Ordering a Specific Vehicle """
    car = {} 
    car['make'] = make 
    car['model'] = model
    for key, value in specs.items(): 
        car[key] = value 
    return car

order_car = selected_car("Tesla","Model X", 
                        colour = "White",
                        self_driving = True,
                        supercharging = False,
                        electric = True) 
print(order_car) 

#------------------------------------------------------

import burgers as b #'import' allows you to use Code from another Module in your Current Session.
b.make_burgers("Beef and Cheese","Tomato") 

from burgers import make_gun as guns, make_burgers as burger #'from' allows you to use a Variety of Functions from a Module in your current Session. 
guns("acog","silencer","grip","stock","drum mag") #'as' allows us to rename a Function or Module from the Import Statement. 
burger("chicken steak and lettuce","chilli")

from burgers import * #'import *' allows you to use all Functions inside the Module. 
decisions("lua","it is so much more easier and rewarding","python") 

print("\n") 
#Test V--------------------------

import burgers 
burgers.make_burgers("sausage and bacon","brown") 

import burgers as b 
b.make_burgers("Plant-based meat and cheese","tomato") 

from burgers import make_burgers as mb
make_burgers("steak, cheese and bacon","barbeque") 

from burgers import make_gun
make_gun("suppressor","holographic sight","angled grip","extended magazine") 

from burgers import * 
make_burgers("steak patty, cheese, iceberg lettuce, onions and pickles",
            "big mac") 
make_gun("reflex sight","extended barrel") 


#Test End---------------------








