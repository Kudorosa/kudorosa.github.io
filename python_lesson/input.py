greet = "Hello, I am Lisa!".title()
greet += "\nMay I know your name please? ".title()

name = input(greet) #input() allows a displays a Prompt for a User to then follow through.
print(f"Greetings {name}! I hope you are having a good day!".title()) 
message = input("What is your age please? ".title()) 
if int(message) >= 18: #int() changes a String thats a Number into a Numerical Value.
    print(f"Good, you are an adult, you may pass.".title()) 
else:
    print("Im afraid you didnt meet the standards to enter..".title()) 
    
level = input("\n\nWhat is your current level right now? ".title()) 
level = int(level) 

if level >= 20:
    print("Great, you can now finally access dungeons.".title()) 
if level >= 100:
    question = input("Wow, you are such a sweat, how long have you been playing the Game for in hours? ".title())
    question = int(question)
    if question > 50:
        print("Sweaty nerd lol!".upper()) 
    elif question < 5:
        print("Nice hacks man...".title()) 
else:
    print("Wow, you are so low level, keep farming man..".title()) 

guess = input("Give me a Number and I will tell you if its Even or Odd: ".title()) 
guess = int(guess) 

if guess % 2 == 0: 
    print(f"the number {guess} to which you provided is 'Even'!".title()) 
else:
    print(f"the Number {guess} is 'odd'.".title()) 
    
#Test V

cars = ["tesla","toyota","ford","nissan","peugeot"] 

sale = input("Hello, what Vehicle would you like to purchase? ".title()) 
sale = sale.lower() 
if sale not in cars:
    print(("We do not have a " + sale + ".").title())
else:
    print(("Yes, we have that brand of Vehicle, let me get you a " + sale + "."
    ).title())

    
print("\n\nGreetings, Welcome to Kudo's Dinner!") 
group = input("\nHow much people are in your party so we can setup a table? ".title())
group = int(group) 

if group > 8: 
    print(("Unfortunately, due to your group size of " + str(group) + "," + 
    " you may have to wait for a table to become available to you.").title())
    proposal = input("\nIs that okay with you Sir? ".title())
    proposal = proposal.lower()  
    if proposal == "yes":
        print("\nThank you, it should not be too long a wait.".title()) 
    elif proposal == "no": 
        print("\nSorry I could not be of service to you today sir..".title()) 
else: 
    print("Alright, we have a Table waiting for you, please follow me!".title()) 

number = input(("\nAlright, Tell me a Number and I will see if it is a multiple"
" of 10: ").title()) 
number = int(number) 

if number % 10 == 0: 
    print(("the Number '" + str(number) + "' is a multiple of 10!").title()) 
else: 
    print(("'" + str(number) + "' is not a multiple of 10.").title()) 

#-----------------------------



