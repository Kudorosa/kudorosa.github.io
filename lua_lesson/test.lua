print("Hello World")

Burgers = {"cheese burger","chicken burger","donner burger",
"ham burger","special burger","burger store"}
Sauce = {}
Toppings = {}
Total_amount = 120
Card1 = 95
Card2 = 150
Card_pin = 5830
Number_entered = 5530

table.insert(Burgers, #Burgers, "..fries")
table.insert(Burgers, #Burgers, "..large meal")

for i, n in pairs(Burgers) do 
    print(n.."\n") 
end 

print("Dean: man, i am starving, say, where do you wanna go to eat?"..
"\n\nGirl: where you say? Well, theres a really good "..Burgers[#Burgers].." closeby, "..
"why dont we eat there?\n") 
print("Dean: Alright, thats a great idea, lets goto the "..Burgers[#Burgers]..
" i love Burgers so much! \n\nGirl: yes, me as well!\n") 
print("Cashier: Hello, welcome to kudomania "..Burgers[#Burgers]..
" how may i help you today? \n\nDean: Hello, just give me a brief moment to ".. 
"check out the menu please.\n")
print("Cashier: Alright, take your time Sir! \n\nDean: Alright, so what would".. 
" you like a--? \n\nGirl: i want a "..Burgers[1].." and a "..Burgers[3].." please!\n")
print("Dean: okay, i want the same as hers plus a "..Burgers[1]..", "..
Burgers[4].." and some "..Burgers[6].." all as a "..Burgers[7].." please!\n")
print("Cashier: wow Alright, thats a huge order! \n\nGirl: haha, isnt that too".. 
" much for you Dean? \n\nDean: nothing is too much for me!\n")
print("Cashier: Alright so, you want 2 "..Burgers[1].." 2 "..Burgers[3].."s with ".. 
"one of each being included in a "..Burgers[7].." correct?\n")      
print("Dean: yes thats correct! \n\nCashier: okay, then you want a "..Burgers[2]..
", a "..Burgers[5].." and "..Burgers[6].." which is all included as a "..Burgers[7]..
" right?\n")
print("Dean: yes, that is correct, you everything correct! \n\nCashier: thats ".. 
"good to hear! \n\nAlright, so all together, that will be err....£"..Total_amount..
" please!\n")
print("Girl: wow! \n\nDean: what the?!?! lets see if i have enough money to ".. 
"complete this transaction, bare with me please. \n\nCashier: that is fine.\n")
print("Dean: (Dean whispers) i dont think i have enough money for this ".. 
"hahaha.. \n\nGirl: (Girl whispers) i thought you said 'nothing is too much for ".. 
"me'.\n")
print("Dean: (still whispering) yes, i was talking about the food, not the "..  
"cost hahaha....now to try my card, it should work.\n")

if Card1 >= Total_amount then
	print(string.upper("'Beep' order complete, printing receipt!"))
else
	print("Card Pay Machine:"..string.upper(" ..card declined, please try again!\n"))
end
	
--
print("Dean: Alright, that did not work, let me try my other card!\n")

if Total_amount <= Card2 then
	print("card pay machine:"..string.upper(" ..beep card accepted, please enter ".. 
                                            "..your pin!\n"))
end
--
print("Dean: Alright, now for the pin, lets hope i can still remember it.\n")

if Number_entered == Card_pin then 
	print("card pay machine:".." ..correct, order complete!\n")
elseif Number_entered ~= Card_pin then
	print("card pay Machine:".." ..incorrect, 2 attempts remaining!\n")
--

Number_entered = Number_entered + 100

print("Dean: i entered the wrong pin, i have 2 attempts remaining....\n")

if Number_entered ~= Card_pin then
	print("card pay machine:"..string.upper(" ..incorrect, 1 attempt remaining!\n"))
elseif Number_entered == Card_pin then
	print("card pay machine:"..string.upper(" ..correct, order complete!\n"))
end
--

Number_entered = Number_entered + 200


print("Dean:oh no! i have 1 attempt left, if i fail one more time, my "..
"credit card will be locked! \n\nGirl: dont fail then, the food is counting on ".. 
"us!\n")
print("Dean: Alright, here it goes, my final attempt, please, i hope this ".. 
"will work!\n")

if Number_entered == Card_pin then
	print("card pay machine:".." ..correct, order complete!\n")
else
	print("card pay machine:".." ..all attempts exhausted, card locked!\n") 
end
--
print("Dean: yes, lets go! i.. i mean, we beat the system! \n\nGirl: indeed, "..
"nice one.. \n\nCashier: congratulations, now, what would you like on your ".. 
"Burgers after when there cooked?\n")

table.insert(Sauce, "ketchup")
table.insert(Sauce, "mayonnaise")

print("\nGirl: Alright, so i want "..Sauce[1].." on my "..Burgers[1].." and "..Sauce[1]..
" on my "..Burgers[2].." please. \nDean: what about the Toppings?\n")

table.insert(Toppings, "onions")
table.insert(Toppings, "tomatos")
table.insert(Toppings, "lettuce")

print("Girl: ohhh, i forgot heh, the Toppings i would like are "..Toppings[1].. 
" on my "..Burgers[1].."and, "..Toppings[2].." and "..Toppings[3].." on my \n"..Burgers[3].. 
" please!")

table.insert(Sauce, "Mint Sauce")
table.insert(Sauce, "Chili Sauce")
table.insert(Sauce, "Special Sauce")
table.insert(Toppings, "Special Toppings")

print("Dean: Alright, so its me next! i would like same as hers on my Burgers"..
", i then would like"..Sauce[2].."on my \n"..Burgers[1].." and "..Sauce[3].." on my "..
Burgers[4].." the Toppings i would like on my Burgers are, "..Toppings[1]..
Toppings[1].." and \n"..Toppings[2].." on my "..Burgers[1].." and then, i would like"..
" the random special assortment on my "..Burgers[4].." since it is \nspecial after".. 
" all ha!")
print("Cashier: Alright, so for the "..Burgers[4].." you want "..Sauce[4].." and "..
Toppings[3].." right?")
print("Dean: correct! \nCashier: Alright, please take a seat while the food "..
"is being made please. \nDean: Alright, lets take a seat. \nGirl: sure!")

print("\n\t                                    - To Be Continued -") 
	
	
Guests = {"Avneet","Harleen","Katherine"}

print("Greetings "..Guests[1]..".., How would you like to join me on a "..
"Dinner Party starting in a few Hours?")
print("Hello "..Guests[#Guests]..".., Wanna join a romantic dinner i setup? ".. 
"you won't regret it.")
print("Hi "..Guests[1]..".. the beautiful, i wanna ask you out on a "..
"date where we will have dinner with some other people, wanna join love?") 

Unavailable = table.remove(Guests, 3)
print("Oh, looks like "..Unavailable..".. said she wont make it, "..
"appparently shes held up with other issues unfortunately...") 
print("Let me invite someone else, someone I want to make up to..")

table.insert(Guests, "Anastasia") 
print("Hiya "..Guests[#Guests]..".., I know its unexpected to message you "..
"after what we've been through but, i want to make it up to you, wanna join "..
"my dinner party? one person you know will be there.")
print("still wanna join the dinner party "..Guests[1].."..?")
print("the date is still on if you want to join "..Guests[1].. 
".., i will wait for as long as it takes for you <3 <3 xxxx.")
print("Hmm, looks my a large dinner table i ordered is imbound, good, now to "..
"invite more Girls!")

print("'Guests Remaining': "..#Guests) --Extra. 

table.insert(Guests, 1 ,"Grace")

print("'Guests Remaining': "..#Guests) --Extra.

table.insert(Guests, 3 ,"Shannon")

print("'Guests Remaining': "..#Guests) --Extra.

table.insert(Guests, #Guests, "Erin")

print("Hello "..Guests[1]..".., wanna join a dinner party? it will be "..
"exciting, I promise!")
print("Hi "..Guests[2]..".., a dinner party is up for joining, it will "..
"be a blast.")
print("Greetings "..Guests[#Guests]..".., i have setup a dinner party, the "..
"invitation is practically given where you can attend any time at your "..
"discretion.")

print("Flip man, the delivery driver ended up in an accident, looks like my "..
"dinner table wont arrive now, I only have room for two people....ahhh!")
print("Looks like I have to rebuke a lot of the invitations i sent out "..
"unfortuately...hope they wont take it the wrong way...")
for i, guest in pairs(Guests) do
    print(guest:sub(1,1):upper()..guest:sub(2)..".")
end

print("'Guests Remaining': "..#Guests) --Extra. 

Sorry_Harleen = table.remove(Guests, 1)
print("Sorry "..Sorry_Harleen..".., i dont have enough space for the "..
"party unfortunately....")

print("'Guests Remaining': "..#Guests) --Extra.

Sorry_Grace = table.remove(Guests, 3)
print("my bad "..Sorry_Grace..".., i dont have the space rn to allow "..
"more people, maybe nxt time ToT.")

print("'Guests Remaining': "..#Guests) --Extra.

Sorry = table.remove(Guests, 2)
print("Sorry "..Sorry..".., i wanted to use this opportunity to make it "..
"up to you but, my delivery driver for a bigger table crashed, i dont have "..
"space for more people, i am so sorry, i hope we makeup next time without any "..
"inconveniences.")

print("'Guests Remaining': "..#Guests) --Extra. 

print("You're still invited "..Guests[1]..".., I love you so much, please "..
"turn up, i beg.")
print("lucky day today "..Guests[1]..".., you are still invited, cannot "..
"wait to see a beautiful lady such as yourself.") 

print(" -a few hours after the party- ".." Ughh,uhh, yeah, harder, deeper!"
.." Ahhhh, its about to release "..Guests[1].."..!")
print(" -a few years later-".." Dean, im pregnant.")

table.remove(Guests, 1)

print("'Guests Remaining': "..#Guests) --Extra.

table.remove(Guests, 1) 

print("'Guests Remaining': "..#Guests) --Extra.

table.remove(Guests, 1) 

print("'Guests Remaining': "..#Guests) --Extra.

for i, guest in pairs(Guests) do
    print(guest:sub(1,1):upper()..guest:sub(2)..".")
end
end