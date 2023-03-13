import json 

log = "secret.json"
with open(log) as file_object:
    girls = json.load(file_object) #json.load() Retrieves a File with previously Saved Data to then allow Python to utilise it again. 
    for rank, name in girls.items(): 
        if rank.lower() == "lover":
            rank = rank.replace("lover","1st")
        print("Rank: " + rank + "\nName: " + name + ".\n") 
 
        
def greet_person():
    """ Greeting the Person or Prompt the Person to Enter their Name """
    name = get_name()
    if name:
        print("Welcome back " + name + "!") 
    else: 
        name = person_provide_name() 
        print(("Thank you " + name + ", hopefully we meet again.").title()) 

def person_provide_name():
    """ The Person's Response which will Hopefully Grant us their Name """ 
    prompt = input("Hello, may I know your name please? ".title()) 
    log = "name.json"
    with open(log, "w") as file_object: 
        json.dump(prompt, file_object)
        return prompt

def get_name():
    """ Getting the Persons Name """ 
    log = "name.json"
    try:
        with open(log) as file_object: 
            name = json.load(file_object) 
    except FileNotFoundError: 
        return None 
    else: 
        return name
        
#Test V------------------------

memory = "favourite_number.json"
with open(memory) as file_object:
    remember = json.load(file_object) 
    print("Hahaha, I know your Favourite Number, it's " + remember + "!") 
    
       
