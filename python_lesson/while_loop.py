souls = 1
while souls <= 10: 
    if souls == 1: 
        print(str(souls) + " soul gained!".title()) 
    else:
        print(str(souls) + " souls gained!".title()) 
    souls += 1 

tip = "\nGreetings Traveler, do you wish to speak with me?".title()
tip += "\n-Type 'no' to end conversation- ".title()


running = False

response = ""

dialogue = "\nAlright, what would you like to speak to me about? ".title() 
life = "\nMy life has been arduous but now i am starting to see the benefits of it.".title()
question = "\nanything else you would like to speak to me about Traveller? ".title()
food = "\nwow well my favourite food is a beef burger with chilli sauce!".title() 

while running: #'while' is a conditional test which runs code as long as the condition remains True.
    response = input(tip)
    
    if response.lower() != 'no' or response == "yes": 
        response = input(dialogue) 
        
        if response.lower() == "life":
            print(life) 
            response = input(question)
            
        elif response.lower() == "food":
            print(food)
            response = input(question)
            
        if response.lower() == "no":
            print("\nsafe journeys traveller!".title())
            running = False
    else:
        print("\nsafe journeys traveller!".title())
        running = False 

proposal = "\nWelcome to 'Who Would you Date?'"
proposal += "\n(Type 'exit' to quit.)".title()
proposal += "\nWho would you date? ".title()

while False: 
    response = input(proposal)
    if response.lower() == "exit":
        break #break immediately stops Code/Blocks from running.
        
    elif response.lower() != "exit":
        print(("\nI would love to date " + response + ", she is so beautiful!").title()) 
        response = input("\nWho else would you date? ".title())
        
        if response.lower() == "noone" or "exit":
            break
        else:
            print(f"\nI would also love to date {response} as well!".title())

number = 0 
while number < 10:
    number += 1
    if number % 2 == 0:
        continue #'continue' returns to the beginning of the Loop.
   
    print(f"{number}\n") 
    
x = 0
while x < 5: 
    x += 1 
    print(x)

#Test V -----------


pizza_store = "\nWhat Toppings would you like on your Pizza? ".title()
order = input(pizza_store)

while False: 
    if order.lower() == "quit":
        print("Alright, your pizza will be done soon!".title()) 
        break
    elif order != "quit":
        print(("\nAlright, adding " + order + " to your Pizza!").title()) 
        order = input("\nanything else? ".title())
        if order.lower == "quit": 
            break
    else:
        continue

movie = "\nWelcome to Kudo Movies!".title()
movie += "\nTell me your Age so I can decide how much you will pay: ".title()

price = input(movie) 

while False: 
    age = int(price) 
    if age <= 3: 
        print("\nYou can watch the Movies for Free!".title()) 
        price = input(movie)
    elif age > 3 and age < 12: 
        print("\nyour ticket will cost $10.".title()) 
        price = input(movie)
    else:
        print("\nsince you are 12+, you will have to pay $15 please.".title()) 
        price = input(movie)


 
while True: #Conditional Test Version! 
    age = int(price) 
    if age == 0:
        print("\nFarewell...".title()) 
        break
    if age <= 3: 
        print("\nYou can watch the Movies for Free!".title()) 
        price = input(movie)
    elif age > 3 and age < 12: 
        print("\nyour ticket will cost $10.".title()) 
        price = input(movie)
    elif age >= 12: 
        print("\nsince you are 12+, you will have to pay $15 please.".title()) 
        price = input(movie)
    else:
        print("\nfarewell".title()) 


pizza_store = "\nWhat Toppings would you like on your Pizza? ".title()
order = input(pizza_store)


order_ongoing = False

while order_ongoing: #Active Variable Version!
    if order.lower() == "quit":
        order_ongoing = False
    else:
        print(("\nAlright, adding " + order + " to your Pizza!").title()) 
        order = input("\nanything else? ".title())
        
while True: #Break Version!
    if order.lower() == "quit" or order.lower() == "nothing":
        break
    else:
        print(("\nAlright, adding " + order + " to your Pizza!").title()) 
        order = input("\nanything else? ".title())
        
#--------------------------------

storage = ["sauce","burgers","buns"] 
fridge = [] 

while storage: 
    refridgerator = storage.pop() 
    print(f"adding {refridgerator} to the Fridge!\n".title()) 
    
    fridge.append(refridgerator) 
    
print("The items added to the Frige were:".title()) 
for item in fridge: 
    print(item.title() + ".") 
    
    
games = ["gta","gta","gta","gta","minecraft","roblox","gta","gta","gta"] 

while "gta" in games: 
    games.remove("gta") 
    print(games) 
    
participants = {} 

voting_active = False 

while voting_active: 
    name = input("\nGreetings, what is your name please? ".title()) 
    idea = input("\nWhat game idea would you like to vote for today? ".title()) 
    
    participants[name] = idea
    
    retry = input("\nWould you like to vote on somebodys behalf? (yes/no) ".title())
    if retry.lower() == "no": 
        voting_active = False

print("\n---------Vote Results------------") 
for name, idea in participants.items(): 
    print(f"{name} has voted for {idea} to be created on Roblox!".title()) 

#Test V------------------------
    
orders = ["pastrami","pastrami","pastrami","pastrami","tuna","egg mayonnaise",
    "bacon, lettuce and tomato","pastrami","chicken triple","breakfast",
    "chicken & stuffing","pastrami","pastrami"] 
finished_sandwiches = []     

print("\nuh oh, looks like the we have run out of Pastrami!\n".title())

while "pastrami" in orders: 
    orders.remove("pastrami") 
    print(orders)

while orders: 
    complete_orders = orders.pop() 
    print(("finished making your " + complete_orders + " sandwich!\n").title()) 
    
    finished_sandwiches.append(complete_orders)

print("\nThe sandwiches perfectly homemade for you are: \n".title()) 
for sandwich in finished_sandwiches: 
    print("1x " + sandwich.title() + " sandwich.".title()) 

people = {} 

questionnaire_active = False

while questionnaire_active:
    name = input("\nGreetings Human, please provide me your name: ".title())
    vacation = input(("\nif you could travel anywhere around the World,"
                    " where would you goto? ").title()) 
                    
    people[name] = vacation 
    repetition = input("\nwill someone else answer? (yes/no) ".title()) 
    if repetition.lower() == "no": 
        questionnaire_active = False 
    
print("\n---------Questionnaire Results:") 
for name, vacation in people.items(): 
    print(("wow so " + name + " would like to go to " + vacation + " for a" +
    " vaction! simply amazing!\n").title()) 

#------------------------------



    



    
    


       
        
    
    
    
 
    
    




    
        
        
    


    
        
