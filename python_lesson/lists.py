sandwiches = ["Ham sandwich","Bacon, lettuce & Tomatos","Egg & cress"]#[] Allows you to create a List for you to store whatever Information you want.
print(sandwiches[1].title())#variable[1] Will Collect the 2nd Value in the List.
print(sandwiches[2].upper())#variable[2] Will Collect the 3rd Value in the List.
print(sandwiches[0].lower())#variable[0] Will Collect the 1st Value in the List.
print(sandwiches)#print(variable) containing a List will Print out ALL Values.
print(sandwiches[-1])#[-1] Allows you to collect the Last Value inside of a List, additionally you can increase the Number to Collect Values backwards. 
print("\n\t")

Money = "£12"  

Message = "Cashier: Hello, welcome to wichesRus! What would you like to order? \nMe: Hi, I would like to order a " + sandwiches[0].title() + " and a " + sandwiches[-1].title() + " sandwich please!".title()
Message1 = "\nCashier: Alright, that will be " + str(Money) + " please Sir. \nMe: Wowza, thats Expensive! Alright Here is the " + Money + "."
print(Message,Message1)
print("\n\t")

lovers = ["Harleen","Avneet","Grace","Katherine"]
print(lovers[1])
print(lovers[0])
print(lovers[-2])
print(lovers[-1]) 
print("\nGreetings " + lovers[0] + ", it has been awhile.")
print("\nHello " + lovers[2] + ", hope you're treating the fidget spinner well!".title())
print(f"\n{lovers[-1]}" + ", Im Sorry, can we please just start over, give me a chance, I beg you...".title())
print("\nHi " + lovers[1] + ", it has been a long time my love, I never forgot you, why?".title(),"Because I Love you!".title())
#                        0             1                 2            3  
favourite_cars = ["Tesla Model X","Polestar 1","Mercedes S-Class","Teslas"]
print("\nMan, my Dream Car in the Future has got to be the " + favourite_cars[0] + ", it is so futuristic with Self Driving and Everything!")
print("\nRandom Voice: How predictable, you and your love for " + favourite_cars[-1] + ", well, my favourite dream car has got to be \nthe " + favourite_cars[-2] + "!")
print("\nRandom Girl: Eww, those cars suck, nothing can beat the " + favourite_cars[-3] + ", it beats all " + favourite_cars[-1] + " \nand the " + favourite_cars[-2] + " combined!")

