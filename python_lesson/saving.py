import json #JavaScript Object Notation.

girls = {
        'lover': "Avneet Chima",
        '2nd' : "Harleen",
        '3rd': "Grace Stevenson",
        '4th': "Shannon Davies",
        } 
log = "secret.json"
with open(log, "w") as file_object: 
    json.dump(girls, file_object) #json.dump() holds Data and a File Object to which it will store the Data in a File.

a = False
if a:
    name = input("Greetings, may you tell me your name? ".title()) 

    data = "name.json"
    with open(data, "w") as file_object:
        json.dump(name, file_object)
        print("Thank you " + name + ", we will remember this moment.".title()) 

#Test V--------------------------------

def reveal_number():
    """ Reveal the User's Number """ 
    memory = remember_number() 
    if memory: 
        print("Ah Ha! I Know Your Favourite Number, it is " + memory + "!") 
    else:
        memory = create_new_number() 
        print("Much Appreciated, Prepare to be Blown Away by my Memory!") 
    
def create_new_number(): 
    """ User is thinking of a New Favourite Number """ 
    prompt = input("Alright User, Please Think of Your Favourite Number! ") 
    
    number = "favourite_number.json"
    with open(number, "w") as file_object: 
        json.dump(prompt, file_object) 
        return prompt

def remember_number():
    """ Remembering the User's Favourite Number """ 
    number = "favourite_number.json" 
    try:
        with open(number) as file_object:
            remember = json.load(file_object)
    except FileNotFoundError: 
        return None 
    else: 
        return remember

reveal_number() 

def greet_user(): 
    """ Greeting the User """ 
    username = load_username() 
    while True:
        if username:
            print("\nIs Your Username '" + username + "'?") 
            question = input("-(Type 'Yes' or 'No')- ") 
            if question.lower().strip() == "no":
                username = create_new_username() 
                break
            elif question.lower().strip() == "yes":
                print("\nGreetings and Welcome Back " + username + ".") 
                break
            elif question.lower().strip() != "no" or question.lower() != "yes":
                print("\n-Note: Please Type 'Yes' or 'No'!-".title()) 
        else:
            username = create_new_username()
            print("Alright, We Will Be Sure to Remember You " + username + ".")
            break

def create_new_username(): 
    """ Creating a New Username """ 
    prompt = input("\nHello, please Enter a Username? ".title()) 
    
    username = "username.json"
    with open(username, "w") as file_object: 
        json.dump(prompt, file_object) 
        print("Alright, We Will Be Sure to Remember You " + prompt + ".")
        return prompt

def load_username():
    """ Loading a User's Username """ 
    username = "username.json" 
    try: 
        with open(username) as file_object:
            found = json.load(file_object) 
    except FileNotFoundError:
        return None
    else:
        return found

greet_user() 
