M = require("helpful_functions") 

Greet = "Hello, I am Lisa!"
Greet = Greet.."\nMay I know your Name please? "
io.write(Greet) --#io.write() displays a Message to the User.
Name = io.read() --#io.read() allows a displays a Prompt for a User to then follow through.
print("Greetings "..Name.."! I hope you are having a good day!") 
io.write("What is your age please? ")
Message = io.read() 
if tonumber(Message) >= 18 then --#tonumber() changes a String thats a Number into a Numerical Value.
    print("Good, you are an adult, you may pass.") 
else 
    print("Im afraid you didnt meet the standards to enter..") 
end
    
io.write("\nWhat is your current Level right now? ")
Level = io.read() 
Level = tonumber(Level) 

if Level >= 20 then
    print("Great, you can now finally access dungeons.") 
    if Level >= 100 then
        io.write("Wow, you are such a sweat, how long have you been playing the Game for in hours? ")
        Question = io.read()
---@diagnostic disable-next-line: assign-type-mismatch
        Question = tonumber(Question)
        if Question > 50 then
            print(string.upper("Sweaty nerd lol!")) 
        elseif Question < 5 then
            print("Nice hacks man...") 
        end
    end
else 
    print("Wow, you are so low Level, keep farming man..") 
end



io.write("\nGive me a Number and I will tell you if its Even or Odd: ")
Guess = io.read() 
Guess = tonumber(Guess) 

if Guess % 2 == 0 then 
    print("the Number "..Guess.." to which you provided is 'Even'!") 
else 
    print("the Number "..Guess.." is 'odd'.") 
end
    
--#Test V

Cars = {"tesla","toyota","ford","nissan","peugeot"}

io.write("\nHello, what Vehicle would you like to purchase? ")
Sale = io.read() 
Sale = string.lower(Sale)
for i, car in pairs(Cars) do 
repeat
    if Sale == car then 
        print("Yes, we have that Brand of Vehicle, let me get you a "..M.Title(Sale)..".")
        break
    else
        print("We do not have a "..M.Title(Sale)..".")
        break
    end
until Sale == car
end
    
print("\nGreetings, Welcome to Kudo's Dinner!") 
io.write("How much People are in your Party so we can setup a Table? ")
Group = io.read()
Group = tonumber(Group) 

if Group > 8 then 
    print("Unfortunately, due to your Group size of " ..Group..","..
    " you may have to wait for a table to become available to you.")
    io.write("\nIs that okay with you Sir? ")
    Proposal = io.read()
    Proposal = string.lower(Proposal)  
    if Proposal == "yes" then
        print("\nThank you, it should not be too long a wait.") 
    elseif Proposal == "no" then 
        print("\nSorry I could not be of service to you today sir..") 
    end
else  
    print("Alright, we have a Table waiting for you, please follow me!") 
end


io.write("\nAlright, Tell me a Number and I will see if it is a multiple"..
" of 10 then: ")
Number = io.read() 
Number = tonumber(Number) 

if Number % 10 == 0 then 
    print("the Number '"..Number.."' is a multiple of 10!") 
else  
    print("'"..Number.."' is not a multiple of 10.") 
end

--#-----------------------------