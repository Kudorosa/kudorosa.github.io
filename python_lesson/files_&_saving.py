with open("pi_digits.txt") as file_object: #'with' allows a file to be opened and then closes it when it is no longer needed. 
    pi = file_object.read() 
    print(pi.strip()) 
    
hello = 'txt_files\hello.txt' #Relative File-Path.
with open(hello) as file_object: 
    hello = file_object.read() 
    print("\n" + hello) 

wow = 'C:/Users/Deand/txt_file2/wow.txt' #Absolute File-Path. 
with open(wow) as file_object: 
    wow = file_object.read() 
    print(wow.title() + "\n") 
    
a = 'pi_digits.txt' 
with open(a) as file_object:
    for line in file_object: 
        print(line.rstrip()) 
        
b = 'pi_digits.txt' 
with open(b) as file_object:
    files = file_object.readlines() 

digits = ""
for note in files:
    digits += note.strip()

print("\n" + digits)
print("(" + str(len(digits)) + ")")  

with open("txt_files/hello.txt") as file_object: 
    pi = file_object.read() 
    print(pi) 

with open("C:/Users/Deand/txt_file2/wow.txt") as file_object: 
    wow = file_object.read() 
    print(wow + " I see you're improving at Python!") 

with open("pi_digits.txt") as file_object: 
    lines = file_object.readlines() 

numbers = "" 
for line in lines: 
    numbers += line.strip() 

print(numbers) 
print("[" + str(len(numbers)) + "]") 

million = "C:/Users/Deand/Desktop/1 Million Digits.txt"
with open(million) as file_object: 
    mill = file_object.readlines() 

hold = "" 
for number in mill:
    hold += number.strip() 
print(str(hold[:111]) + "....") 
print("(" + str(len(hold)) + ")") 

dob = "Hello, please enter your Date of Birth (D/M/Y): " 
if dob in hold: 
    print("Congratulations, your Date of Birth appears in our Records!")
else:
    print("Unfortuantely your Date of Birth is not present in our Records!")

#Test V--------------------------------------------------------------
with open("txt_files/learning_python.txt") as file_object: 
    work = file_object.read() 
    print("\n" + work.lower() + "\n")

language = "txt_files/learning_python.txt" 
with open(language) as file_object: 
    for note in file_object: 
        print(note.rstrip().title()) 

with open(language) as file_object: 
    note = file_object.readlines() 

manifesto = "" 
for line in note: 
    manifesto += line.upper() + "\n"

manifesto = manifesto.replace("python".upper(),"lua".upper()) 
print("\n" + manifesto) 
manifesto = manifesto.replace("lua".upper(),"C#") 
print("\n" + manifesto.title()) 
manifesto = manifesto.replace("c#".title(),"c++") 
print("\n" + manifesto.title())  

#---------------------------------------------------------------------
program = "txt_files/programming.txt"
with open(program, "w") as file_object: #"w" initiates Write Mode which allows you to Write inside a Document, IF THE DOCUMENT EXISTS, IT WILL BE ERASED!
    file_object.write("I want to fully Master Programming!\n".title())  #.write() allows you to Write whatever you want inside the Document. 
    file_object.write("I want to create games with my Coding Skill!\n".title())

with open(program, "a") as file_object: #"a" initiates Append Mode which allows you to Edit a Document without it being Erased by Python. 
    file_object.write(("\nI Need to Master Programming so I can make Games!\n"
    ).title())
    file_object.write(("Then afterwards, I need to learn Modelling and Art.."
    ).title()) 

with open(program) as file_object: 
    notes = file_object.read() 
    print(notes) 

#Test V--------------------------------------------------------

guest = input("\nGreetings, what is your name? ".title()) 
names = "txt_files/guest.txt"
with open(names, "w") as file_object: 
    file_object.write("Greetings, ".title()) 

with open(names, "a") as file_object:
    file_object.write(guest.title() + ".") 

with open(names) as file_object: 
    name = file_object.read() 
    print("\n" + name) 

book = "txt_files/guest_book.txt"
check = [] 

with open(book) as file_object:
    checker = file_object.readlines() 

for line in checker: 
    check.append(line.strip().lower())


while False: 
    person = input("Provide me your name please? ".title()) 
    if person.lower() == "no":
        break
        
    elif person.lower().strip() in check:
        print("This person is already in the Guest Book...".title()) 
        
    elif person.lower() not in check:
        check.append(person.lower()) 
        with open(book, "a") as file_object: 
            file_object.write(person.title() + "\n") 
            
        print("\nGreetings " + person.title() + ", I have added you to the"
        " guest book contained as a Text File.\n".title())
        
        question = input("Do you wish to Provide more names? ".title()) 
        if question.lower() == "no": 
            break 
        else: 
            continue

poll = "txt_files/programming_poll.txt"

while False:
    polling = input(("\nHi there, can you please tell me why you like"
                    " programming? ").title()) 
    if polling.lower() == "no":
        print("That's Unfortunate, Farewell..")
        break
        
    elif polling.lower() != "no":
        with open(poll, "a") as file_object:
            file_object.write(("- " + polling + "\n").title()) 
            
        polling = input(("Thank you for your Opinion, is there anybody else" 
        " that is willing to express their opinions in this Poll? ").title())
        if polling.lower() == "no":
            print("Alright, thank you for participating!".title()) 
            break
            
        else:
            continue
    else:
        print("Unfortunate...")
        break
        

with open(book) as file_object: 
    names = file_object.read() 

#-----------------------------------------------------------








    
