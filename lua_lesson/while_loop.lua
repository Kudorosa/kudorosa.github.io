M = require("helpful_functions") 

Souls = 1
while Souls <= 10 do
    if Souls == 1 then 
        print(Souls.." soul gained!") 
    else
        print(Souls.." Souls gained!") 
    end
    Souls = Souls + 1   
end

Tip = "\nGreetings Traveler, do you wish to speak with me?"
Tip = Tip.."\n-Type 'no' to end conversation- "


Running = true

Response = ""

Dialogue = "\nAlright, what would you like to speak to me about? " 
Life = "\nMy Life has been arduous but now i am starting to see the benefits of it."
Question = "\nanything else you would like to speak to me about Traveller? "
Food = "\nwow well my favourite Food is a beef burger with chilli sauce!" 

while Running do --#'while' is a conditional test which runs code as long as the condition remains True.
    io.write(Tip)
    Response = io.read()
    
    if string.lower(Response) ~= 'no' or Response == "yes" then 
        io.write(Dialogue)
        Response = io.read() 
    
        
        if string.lower(Response) == "life" then
            print(Life) 
            io.write(Question)
            Response = io.read()
            
        elseif string.lower(Response) == "food" then
            print(Food)
            io.write(Question)
            Response = io.read()
        end
            
        if string.lower(Response) == "no" then
            print("\nsafe journeys traveller!")
            Running = false
        end

    else
        print("\nsafe journeys traveller!")
        Running = false 
    end
end

Proposal = "\nWelcome to 'Who Would you Date?'"
Proposal = Proposal.."\n(Type 'exit' to quit.)"
Proposal = Proposal.."\nWho would you date? "

while true do 
    io.write(Proposal)
    Response = io.read()
    if string.lower(Response) == "exit" then
        break --#break immediately stops Code/Blocks from Running.
        
    elseif string.lower(Response) ~= "exit" then
        print("\nI would love to date "..Response..", she is so beautiful!")
repeat
    io.write("\nWho else would you date? ") 

    Response = io.read()
    if string.lower(Response) == "noone" or string.lower(Response) == "exit" then
        break
    else
        print("\nI would also love to date "..Response.." as well!")
    end
until string.lower(Response) == "noone" or string.lower(Response) == "exit" 
break
end
end


Number = 0 
while Number < 10 do
    repeat
    Number = Number + 1
    until Number % 2 ~= 0 --#'continue' returns to the beginning of the Loop.
end
    print(Number.."\n") 
    
X = 0
while X < 5 do
    X = X + 1 
    print(X)
end

--#Test V -----------


Pizza_store = "\nWhat Toppings would you like on your Pizza? "
io.write(Pizza_store)
Order = io.read()

while true do 
    if string.lower(Order)  == "quit" then
        print("Alright, your pizza will be done soon!") 
        break
    elseif Order ~= "quit" then
        print("\nAlright, adding "..M.Title(Order).." to your Pizza!") 
        io.write("\nanything else? ")
        Order = io.read()
    
        if string.lower(Order) == "quit" then 
            break
        end
    end
end
    

Movie = "\nWelcome to Kudo Movies!"
Movie = Movie.."\nTell me your Age so I can decide how much you will pay: "
io.write(Movie)
Price = io.read() 

while true do 
---@diagnostic disable-next-line: assign-type-mismatch
    Age = tonumber(Price) 
    if Age == 0 then 
        break
    elseif Age <= 3 then 
        print("\nYou can watch the Movies for Free!") 
        io.write(Movie)
        Price = io.read()
    elseif Age > 3 and Age < 12 then 
        print("\nyour ticket will cost $10.") 
        io.write(Movie)
        Price = io.read()
    else
        print("\nsince you are 12+, you will have to pay $15 please.") 
        io.write(Movie)
         Price = io.read()
    end
end


while true do --#Conditional Test Version! 
---@diagnostic disable-next-line: assign-type-mismatch
    Age = tonumber(Price) 
    if Age == 0 then
        print("\nFarewell...") 
        break
     elseif Age <= 3 then 
         print("\nYou can watch the Movies for Free!") 
         io.write(Movie)
         Price = io.read()
    elseif Age > 3 and Age < 12 then 
        print("\nyour ticket will cost $10.") 
        io.write(Movie)
        Price = io.read()
    elseif Age >= 12 then 
         print("\nsince you are 12+, you will have to pay $15 please.") 
         io.write(Movie)
         Price = io.read()
    else
        print("\nfarewell") 
    end
end


Pizza_store = "\nWhat Toppings would you like on your Pizza? "
io.write(Pizza_store)
Order = io.read()


Order_ongoing = true

while Order_ongoing do --#Active Variable Version!
    if string.lower(Order)  == "quit" then
        Order_ongoing = false

    else
        print("\nAlright, adding "..Order.." to your Pizza!") 
        io.write("\nanything else? ")
        Order = io.read()
    end
end
        
while true do --#Break Version!
    if string.lower(Order)  == "quit" or string.lower(Order)  == "nothing" then
        break
    else
        print("\nAlright, adding "..Order.." to your Pizza!") 
        io.write("\nanything else? ")
        Order = io.read()
    end
end
        
--#--------------------------------

Storage = {"sauce","burgers","buns"} 
Fridge = {} 

while #Fridge < 2 do 
    Refridgerator = table.remove(Storage, 1) 
    print("Adding "..Refridgerator.." to the Fridge!\n") 
    
    table.insert(Fridge, Refridgerator) 
end
    
print("The items added to the Frige were: ") 
for i, item in pairs(Fridge)  do 
    print(M.Title(item)..".") 
end   

print("\n") 
Games = {"gta","gta","gta","gta","minecraft","roblox","gta","gta","gta"}

local test = Games -- Original Table with Duplicates. 
local hash = {} -- Unique Key Creation. 
local res = {} -- New Table. 

for _, v in ipairs(test) do -- Duplicate Remover.
    if not hash[v] then 
        res[#res+1] = v 
        hash[v] = true 
    end 
    test = res 
end 
for i, game in pairs(test) do 
    if game == "gta" then 
        print(M.Title(game).." |18+|")
    else
        print(M.Title(game).." |7+|")
    end
end
        
Participants = {} 

Voting_active = true 

while Voting_active do 
    io.write("\nGreetings, what is your Name please? ")
    Name = io.read() 
    io.write("\nWhat game Idea would you like to vote for today? ")
    Idea = io.read() 
    
    Participants[Name] = Idea
    
    io.write("\nWould you like to vote on somebodys behalf? (yes/no) ")
    Retry = io.read()

    if string.lower(Retry) == "no" then 
        Voting_active = false
    end
end

print("\n---------Vote Results------------") 
for Name, Idea in pairs(Participants) do
    print(Name.." has voted for "..Idea.." to be created on RobloX!") 
end

--#Test V------------------------
    
Orders = {"pastrami","pastrami","pastrami","pastrami","tuna","egg mayonnaise",
    "bacon, lettuce and tomato","pastrami","chicken triple","breakfast",
    "chicken & stuffing","pastrami","pastrami"} 

Finished_sandwiches = {}    

print("\nUh-oh, looks like the we have run out of Pastrami!\n")

local test1 = Orders
local hash1 = {}
local res1 = {}
for _, v in ipairs(test1) do -- Duplicate Remover
    if not hash1[v] then 
        res1[#res1+1] = v 
        hash1[v] = true 
    end 
    test1 = res1 
end 

while #test1 > 1 do 
    Complete_orders = table.remove(test1, #test1) 
    print("Finished Making your "..Complete_orders.." Sandwich!\n") 
    
    table.insert(Finished_sandwiches, Complete_orders)
end

print("\nThe Sandwiches Perfectly Homemade for you Are: \n") 
for i, sandwich in pairs(Finished_sandwiches) do
    print("1x "..M.Title(sandwich).." Sandwich.") 
end

People = {}

Questionnaire_active = true

while Questionnaire_active do
    io.write("\nGreetings Human, please provide me your Name: ")
    Name = io.read()
    io.write("\nIf you could Travel Anywhere Around the World,"..
    " where would you Goto? ")
    Vacation = io.read() 
                    
    People[Name] = Vacation 
    io.write("\nWill Someone else Answer? (yes/no) ")
    Repetition = io.read() 
    if string.lower(Repetition) == "no" then 
        Questionnaire_active = false 
    end
end
    
print("\n---------Questionnaire Results:") 
for name, vacation in pairs(People) do
    print("Wow so "..M.Title(name).." would like to go to "..M.Title(vacation).." for a"..
    " Vaction! simply Amazing!\n") 
end

--#------------------------------
