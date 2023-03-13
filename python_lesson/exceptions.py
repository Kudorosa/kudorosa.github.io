try: #The 'try' Block holds Code that may Error and if they do, it is passed to the Except Block, else, the Except Block is skipped. 
    print(5/0)
except ZeroDivisionError: #The 'except' Block holds an Error Code and if the Code inside the Try Block matches the Error Code, the Exception Block Runs.
    print("The Number '0' Cannot be Divided!\n") 

a = False

if a == True:
    print("Give me Two Numbers and I will Divide Them!"
    "\n-(Press 'q' to Quit)-") 


while False: 
    first_no = input("1st Number: ") 
    if first_no.lower() == "q":
        break 
    second_no = input("2nd Number: ") 
    if second_no.lower() == "q":
        break
    try:
        answer = int(first_no) / int(second_no)
    except (ValueError, ZeroDivisionError):
        print("\nWarning: Please Ensure to Use Numbers and Not Divide by 0!\n")
    else:
        print(f"\n{answer}\n") 

def word_counter(book): 
    """ Enter a Text File to count the Number of Words inside it """ 
    try:
        with open(book) as file_object: 
            read = file_object.read() 
    except FileNotFoundError: 
        print("Unfortunately, the File '" + book + "' was not Discovered...")
     
    else:
        disect = read.split() #split() disassembles a String and places each individual Word in a List. 
        number_of_words = len(disect) 
        print("The File '" + book + "', has about " + str(number_of_words) 
        + " words in total!".title()) 

def word_counter2(book): 
    """ Enter a Text File to count the Number of Words inside it """ 
    try:
        with open(book) as file_object: 
            read = file_object.read() 
    except FileNotFoundError: 
        pass #'pass' tells Python to do nothing in the Code Block to which 'pass' is present in. 
    else:
        disect = read.split() #split() disassembles a String and places each individual Word in a List. 
        number_of_words = len(disect) 
        print("The File '" + book + "', has about " + str(number_of_words) 
        + " words in total!".title()) 

books = ["txt_files/war and peace.txt", "txt_files/alice.txt", 
"txt_files/ulyss.txt", "txt_files/looking-glass.txt",
"txt_files/great expectations.txt"]
for book in books:
    word_counter(book) 

word_counter2(books[2]) 

#Test V-----------------------------------------
b = False 
if b: 
    print("Hello, give me two Numbers and I will Add them up for you!".title()) 
    print("\n--Press 'q' to Quit--")
    
while False:
    try:
        first = input("Your 1st Number: ")
        if first.lower() == "q":
            break
        first = int(first)
        
        second = input("Now, for your 2nd Number: ")
        if second.lower() == "q": 
            break 
        second = int(second)
        
    except ValueError: 
        print("\nNote: Only Enter Numbers Please!\n") 
    else:
        add = f"\n{int(first)} + {int(second)} = {int(first) + int(second)}\n"
        print(add)

def animal_viewer(animals):
    """ Viewing Names of Animals in a File """ 
    try: 
        with open(animals) as file_object:
            animal = file_object.read()
    except FileNotFoundError:
        pass
    else:
        print("\nAnimal Breeds:\n" + animal.title())
    
    

kitties = animal_viewer("cats.txt") 
doggies = animal_viewer("dogs.txt") 
    

def specific_word(book, word):
    """ Finding a Specific Word in a Book """ 
    try:
        with open(book) as file_object:
            read = file_object.read() 
    except FileNotFoundError:
        print("\nUnfortunately the Book '" + book + "' was not Found!") 
    else:
        print("\nThe Word '" + word + "' has appeared ".title() + 
        str(read.lower().count(word)) + " Times in " + book + ".")#.count() collects and displays the Frequency of a Specific Word/Phrase. 

books = ["txt_files/alice.txt","ulyss.txt","txt_files/looking-glass.txt",
"txt_files/war and peace.txt","txt_files/great expectations.txt"] 
for book in books:
    read = specific_word(book,"help") 
