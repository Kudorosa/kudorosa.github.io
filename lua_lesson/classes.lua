M = require("helpful_functions")

Bank = {balance = 0}
    function Bank:new (obj)
        obj = obj or {} 
        self.__index = self 
        setmetatable(obj, self) 
        return obj
    end

    function Bank:deposit(a) 
        self.balance = self.balance + a 
        print("$"..self.balance.." was added.")
        print("New Balance = $"..self.balance)
    end 

    function Bank:siphon(a) 
        if a > self.balance then error"Funds are Lacking" end
        self.balance = self.balance - a 
        print("$"..a.." was deducted.")
        print("New Balance = $"..self.balance)
    end 

Dean = Bank:new() 
Dean.deposit(Bank, 1000) 
Dean.siphon(Bank, 100) 

-------------------------------------------------------------------------------------------------

 Cat = {} --# OOP - a '' is a Unit which contains Objects and the Behaviours of it. 
  --[[ Making a Cat ]]-- 
    function Cat:new (O, name, age) --#< This is a Constructer which prevents Lua from Assigning of Method Names Conflicting with Yours. 
    --[[Name and Age of the Cat ]]-- 
        O = O or {}
        setmetatable(O, self)
        self.__index = self
        self.name = name or "N/A"
        self.age = age or 0
        return O
    end

    function Cat:Meow() 
      --[[ Cats mostly Meow ]]-- 
        print(self.name.." has unleashed a Meow!\n") 
    end
    
    function Cat:Jump() 
      --[[ Cats mostly Jump on top of things ]]-- 
        print(self.name.." has Jumped on top of an Object!\n") 
    end

My_cat = Cat:new{name="Daisy", age=3}
My_cat:Meow()
My_cat:Jump()

print(My_cat.name.." is My Cute Intelligent Cat!") 
print("despite being only "..My_cat.age.." years old, ".." she is"..
" very active which is of course is a double-edged sword haha.\n")

Your_cat = Cat:new{name="Millie", age=5} 
Your_cat:Meow() 


print(Your_cat.name.." is Your Fluffy Ambitious Cat!") 
print("Your Cat's Age is "..Your_cat.age.." years old which is Good"..  
", it is "..(Your_cat.age - My_cat.age).." years older than My cat!\n") 

My_cat:Meow() 
Your_cat:Jump() 

--#Test V--------------

 Restaurant = {}
  --[[ Making a Restaurant ]]-- 
    function Restaurant:new(o, name_restuarant, cuisine_type) 
      --[[ The Restaurant's Name and the Type of Restaurant it is ]]-- 
        o = o or {}
        setmetatable(o, self)
        self.__index = self
        self.name_restuarant = name_restuarant or "none"
        self.cuisine_type = cuisine_type or "N/A" 
        return o
    end
    
    function Restaurant:Describe_restaurant() 
      --[[ A Description of the Restaurant ]]-- 
        print(self.name_restuarant.." is a "..self.cuisine_type.. 
        " Restaurant:\n") 
    end
    
    function Restaurant:Open_restaurant() 
      --[[ Opening up the Restaurant ]]-- 
        print(self.name_restuarant.." is now Open!\n") 
    end

The_restaurant = Restaurant:new{name_restuarant="Kudos Bites", cuisine_type="Fast-Food"}
 
print("Man, I should try out that new Restaurant called "..
The_restaurant.name_restuarant..", it should be Good..") 

print("I heard its a "..The_restaurant.cuisine_type.." Restaurant, Good!\n"
) 

The_restaurant:Describe_restaurant() 
The_restaurant:Open_restaurant() 

Good_restaurant = Restaurant:new{name_restuarant="The Sulfa", cuisine_type="Diner"}
print("oooo, there is a nice Restaurant in town called '"..
Good_restaurant.name_restuarant.."'.") 
print("judging by the name, i presume its a "..Good_restaurant.cuisine_type.. 
" type of Restaurant!\n") 

Good_restaurant:Describe_restaurant() 

Eaters_restaurant = Restaurant:new{name_restuarant="Eaters Paradise", cuisine_type="Buffet"} 

print("Im starving! let us goto the Restaurant called "..
Eaters_restaurant.name_restuarant..".") 
print("Its also a "..Eaters_restaurant.cuisine_type.." type of Restaurant,"..
" Good, just need to pay only one fee to devour 'everything'!\n") 

Eaters_restaurant:Describe_restaurant() 

Fashion_restaurant = Restaurant:new{name_restuarant="Guccis Indulgence", cuisine_type="Fancy Diner"}
print("dude, have you seen the news, theres a new Fashion Restaurant opening!"..
" its called "..Fashion_restaurant.name_restuarant.."!") 
print("the Restaurant will probs be a "..Fashion_restaurant.cuisine_type..
".....\n") 

Fashion_restaurant:Describe_restaurant() 


 User = {}
  --[[ Creating a User Profile ]]-- 
    function User:new(o, forename, surname, location, other) 
        --[[ Creating a Users Information ]]-- 
        o = o or {}
        self.__index = self
        setmetatable(o, self)
        self.forename = forename or nil
        self.surname = surname or ""
        self.location = location or nil
        self.other = other or nil
        return o
    end
  
    
    function User:Describe_user()
        --[[ Information will be stored above ]]-- 
        if #self.surname >= 4 then
            print("Account Information:\n"..
            "--------------------\n"..
            "First Name: "..self.forename.. 
            "\nLast Name: "..self.surname.. 
            "\nLocation: "..self.location..
            "\nMiscellaneous: "..self.other) 
        else
             print("Account Information:\n"..
            "--------------------\n"..
            "First Name: "..self.forename.. 
            "\nLocation: "..self.location..
            "\nMiscellaneous: "..self.other) 
        end
    end
  
    
    function User:Greet_user() 
        if not nil then 
            if #self.surname >= 4 then
                print("\nGreetings "..self.forename.." "..self.surname..",".. 
                " Hope you are having a Beautiful day today!\n") 
            else
                print("\nGreetings "..self.forename..","..
                " Hope you are having a Beautiful day today!\n") 
            end
        end
    end
    
Profile = User:new{forename="Dean", location="United Kingdom",  other="Loves Programming", surname="Chinamo"} 

Profile:Greet_user() 
Profile:Describe_user() 

Profile1 = User:new{forename="Avneet", location="United Kingdom", other="Social Media Star", surname="Chima"}

Profile1:Greet_user() 
Profile1:Describe_user() 

Profile2 = User:new{forename="Grace",location="United Kingdom",other="Adventurerer",surname="Stevenson"}

Profile2:Greet_user() 
Profile2:Describe_user() 

Profile3 = User:new{forename="Harleen",location="Dubai",other="Influencer"}

Profile3:Greet_user() 
Profile3:Describe_user() 

--#------------------

Vehicle = {} 
  --[[  Representing a Vehicle, can be used to make Vehicles ]]-- 
    
    function Vehicle:new(o, make, model, year, colour)
      --[[ A Vehicle and it's In-depth Information ]]-- 
        o = o or {} 
        self.__index = self
        setmetatable(o, self) 
        self.make = make or nil
        self.model = model or nil 
        self.year = year or nil
        self.colour = colour or nil
        self.mph = 150 --#Direct Update Approach. 
        return o
    end
      
        
    function Vehicle:Retrieve_vehicle_details() 
        --[[ Attributes of the Vehicle ]]-- 
        Car = ("\n'"..self.year.." "..M.Title(self.colour).." "..M.Title(self.make).. 
            " "..M.Title(self.model).."'")
        print(Car) 
    end
        
    function Vehicle:Update_car_speed(mph) --#Method Update Approach. 
      --[[ Updating Car Speed ]]-- 
        if mph <= self.mph then --#Logic Check added to the Method. 
            self.mph = mph
        else
            print("Vehicles cannot exceed their Top Speed.") 
        end
    end
            
    function Vehicle:Refuel_vehicle()
        print("Vehicle has been Refueled!") 
    end
    
    function Vehicle:Car_speed() 
      --[[ Insight on the Vehicle's Speed ]]-- 
        print("This Vehicle has a Avg Speed of "..self.mph.." Mp/h.")
    end

My_Car = Vehicle:new{make="Tesla",model="Model X",year=2016,colour="White"}  
My_Car:Retrieve_vehicle_details()
My_Car:Update_car_speed(130)
My_Car:Car_speed() 

 OldVehicle = {}
  --[[ ]]-- 
    function OldVehicle:new(o, make, model, year) 
        --[[ ]]-- 
        o = o or {}
        self.__index = self
        setmetatable(o, self) 
        self.make = make 
        self.model = model 
        self.year = year 
        self.top_speed = 100
        return o 
    end
    function OldVehicle:Update_speed(current_speed) 
        if current_speed <= self.top_speed then
            self.top_speed = current_speed 
        else
            print("Vehicles cannot exceed their Top Speed!")
        end
    end
        
    function OldVehicle:Decrease_speed(speed) 
      --[[ Decreasing Vehicle Speed ]]-- 
        self.top_speed = self.top_speed - speed 
    end
        
    function OldVehicle:Car_speed() 
      --[[ The Vehicle's Speed ]]-- 
        print("This Vehicle has an Avg Speed of "..self.top_speed .." Mp/h.")
    end
        
    function OldVehicle:Vehicle_details() 
      --[[ ]]-- 
        Car = "\n"..M.Title(self.make).." "..M.Title(self.model).." "..M.Title(self.year)
        return Car
    end

My_old_vehicle = OldVehicle:new{make="Nissan", model="Micra", year="2001"}
print(My_old_vehicle:Vehicle_details())

My_old_vehicle:Decrease_speed(10)
My_old_vehicle:Update_speed(90)
My_old_vehicle:Car_speed() 

My_old_vehicle:Decrease_speed(-30) 
My_old_vehicle:Update_speed(80) 
My_old_vehicle:Car_speed() 

--#Test V---------------

Restaurant = {}
  --[[ Making a Restaurant ]]-- 
    function Restaurant:new(o, restaurant_name, cuisine_type) 
      --[[ The Restaurant's Name and the Type of Restaurant it is ]]-- 
        o = o or {}
        self.__index = self
        setmetatable(o, self)
        self.restaurant_name = restaurant_name or nil
        self.cuisine_type = cuisine_type or nil
        self.number_served = 10
        return o
    end
    
    function Restaurant:Describe_restaurant() 
      --[[ A Description of the Restaurant ]]-- 
        print("\n"..self.restaurant_name.." is a "..self.cuisine_type.. 
        " Restaurant:") 
    end
    
    function Restaurant:Set_number_customers_served(Served)
      --[[ Setting the Customers Served ]]-- 
        if Served >= self.number_served then
            self.number_served = Served
        else
            print("Customers Served cannot be Decreased!") 
        end
    end
    
    function Restaurant:Customers_served()
      --[[ The Amount of Customers in the Restaurant ]]-- 
        Served = ("\nThere are currently "..self.number_served..
        " customers in the Restaurant who have been Served.")
        return Served
    end
    
    function Restaurant:Increment_customers_served(serving) 
      --[[ Increasing the Customers Served Amount ]]-- 
        if self.number_served + serving > self.number_served then 
            self.number_served = self.number_served + serving
        else
            print("\nCustomers Served cannot be Decreased!") 
        end
    end
        
    function Restaurant:Open_restaurant() 
      --[[ Opening up the Restaurant ]]-- 
        print(self.restaurant_name.." is now Open!\n")
    end 

Restaurant = Restaurant:new{restaurant_name="Kudos Burgers", cuisine_type="Fast-Food"}
Restaurant:Describe_restaurant() 

print(Restaurant:Customers_served())
 
Restaurant:Set_number_customers_served(15) 
print(Restaurant:Customers_served()) 

Restaurant:Increment_customers_served(55) 
print(Restaurant:Customers_served()) 


User = {}
  --[[ Creating a User Profile ]]-- 
    function User:new(o, forename, surname, location, other) 
        --[[ Creating a Users Information ]]-- 
        o = o or {}
        self.__index = self
        setmetatable(o, self)
        self.forename = forename or nil
        self.surname = surname or ""
        self.location = location or nil
        self.other = other or nil
        self.login_attempts = 0
        return o
    end
  
    
    function User:Describe_user()
        --[[ Information will be stored above ]]-- 
        if #self.surname >= 4 then
            print("Account Information:\n"..
            "--------------------\n"..
            "First Name: "..self.forename.. 
            "\nLast Name: "..self.surname.. 
            "\nLocation: "..self.location..
            "\nMiscellaneous: "..self.other) 
        else
             print("Account Information:\n"..
            "--------------------\n"..
            "First Name: "..self.forename.. 
            "\nLocation: "..self.location..
            "\nMiscellaneous: "..self.other) 
        end
    end
  
    
    function User:Greet_user() 
        if not nil then 
            if #self.surname >= 4 then
                print("\nGreetings "..self.forename.." "..self.surname..",".. 
                " Hope you are having a Beautiful day today!\n") 
            else
                print("\nGreetings "..self.forename..","..
                " Hope you are having a Beautiful day today!\n") 
            end
        end
    end
    
    function User:Increment_login_attempts() 
        Attempts = 1
        self.login_attempts = self.login_attempts + Attempts 
        if self.login_attempts == 1 then
            print(self.login_attempts.." Login Attempt!")
        else
            print(self.login_attempts.." Login Attempts!")
        end
    end
    
    function User:Reset_login_attempts() 
        self.login_attempts = 0 
        print("-Login Attempts Reset to "..self.login_attempts.."-")
    end
          
        


Userd = User:new{forename="Dean",location="Uk",other="Loves Python",surname="Chinamo"}

Userd:Increment_login_attempts() 
Userd:Increment_login_attempts() 
Userd:Increment_login_attempts() 
Userd:Increment_login_attempts() 

print("Total Login Attempts: "..Userd.login_attempts.."\n") 

Userd:Reset_login_attempts()
Userd:Increment_login_attempts() 
Userd:Increment_login_attempts() 
Userd:Increment_login_attempts()

print("Total Login Attempts: "..Userd.login_attempts.."\n") 

Userd:Reset_login_attempts() 
print(Userd.login_attempts) 
Userd:Increment_login_attempts() 
print(Userd.login_attempts) 


function Food(name,cal) 
  --[[ The Name of the Food and it's Calories ]]-- 
    Item = ("The Food presented is a "..name..", it has "..
    cal.." calories!")
    return Item 
end
     
    
print(Food("Burger",300)) 

Buffet = {}
  --[[ A Buffet filled with Food ]]-- 
    function Buffet:new(o, name) 
        --[[ Name of the Food and the Amount of it ]]-- 
        o = o or {}
        self.__index = self
        setmetatable(o, self) 
        self.name = name
        self.amount = 5 
        return o
    end
  
    function Buffet:Increase_serving(serve) 
        if self.amount + serve >= self.amount then
            self.amount = self.amount + serve
            print("\n"..serve.." "..self.name.." has been added to".. 
            " the Buffet!") 
            print("New amount of "..self.name..": "..self.amount) 
        else
            print("\nPlease do not remove Food before Serving!")
            print("Amount of "..self.name..": "..self.amount) 
        end
    end
            
    function Buffet:Clear_food() 
      --[[ Clearing the Buffet Food ]]-- 
        self.amount = 0 
        print("\nClearing Food!") 
        print(self.name.." left: "..self.amount)
    end
        
    function Buffet:Food()
        Item = (self.name.." is included in the Buffet, the amount of ".. 
                self.name.." available is: "..self.amount..".")
        print(Item)
    end


My_serving = Buffet:new{name="chips"} 

My_serving:Food()

My_serving:Increase_serving(4)
My_serving:Clear_food() 
My_serving:Increase_serving(10) 
My_serving:Increase_serving(-2) 

--#-Inheritance V--

Battery = {battery_charge=0}
  --[[ Creating an Electric Vehicle's Battery ]]-- 
    
    function Battery:new(o, battery_charge) 
        o = o or {}
        self.__index = self 
        setmetatable(o, self) 
        self.battery_charge = battery_charge
        return o
    end

    function Battery:Charge_left() 
        print(self.battery_charge.."% Battery Charge Left..") 
    end

    function Battery:Set_battery_charge(charge) 
        if self.battery_charge + charge >= self.battery_charge then
            if self.battery_charge + charge <= 100 then
                self.battery_charge = charge
                print(charge.."% charge added to Vehicle Battery!")
            else
                print("Vehicle Battery is already fully charged!") 
                self.battery_charge = 100 
            end
        else
            print("Battery cannot be manually drained!") 
        end
    end
    
    function Battery:Get_range() 
      --[[ The Distance Travelled dependant on Battery Charge ]]-- 
        if self.battery_charge == 100 or self.battery_charge >= 90 then 
            Range = 500 
        elseif self.battery_charge <= 90 and self.battery_charge > 50 then 
            Range = 400 
        elseif self.battery_charge <= 50 and self.battery_charge > 25 then  
            Range = 250
        elseif self.battery_charge <= 25 and self.battery_charge > 10 then
            Range = 200
        else
            Range = 100
            print("\nPlease Consider Recharging Your Vehicle!") 
        end
        
        Notif = ("\nThis Vehicle can Travel "..Range.." Metres on ".. 
        self.battery_charge.."% battery.\n")
        print(Notif)
    end


ElectricVehicle = Vehicle:new()


   Ev = ElectricVehicle:new{p_type="Electric"} 
  --[[ An Electric Vehicle ]]-- 
    function Ev:new(o) 
        o = o or {}
        self.__index = self
        setmetatable(o, self)
        self.self_driving = true
        self.battery = Battery
        return o
    end
    
    function Refuel_vehicle()
        print("\nElectric Vehicles do not Require Fuel!") 
    end
    
    

My_ev = Ev:new{make="Tesla",model="Model S",year="2017",colour="Black"}
My_ev:Retrieve_vehicle_details()
My_ev:Update_car_speed(2000) 
My_ev:Car_speed() 

print("\n(Vehicle Self-Driving = "..tostring(My_ev.self_driving == true)..")") 

My_ev.battery:Set_battery_charge(40) 
My_ev.battery:Charge_left() 
My_ev.battery:Get_range() 
 
--#Test V----------------

IceCreamStand = Restaurant:new()
ICS = IceCreamStand:new()
  --[[ An Icecream Stand Inheriting from the Restaurant]]--

    function ICS:new(o)
        --[[ Name of the Restaurant and the Cuisine Type ]]--
        o = o or {}   
        self.__index = self
        setmetatable(o, self)  
        self.flavors = {"vanilla","chocolate","mint","strawberry"}
        return o
    end
        
    function ICS:Display_flavors() 
        print("Greetings! Welcome to "..self.restaurant_name.."!") 
        print("We Have the Following Ice-Cream Flavours Available: \n") 
        for i, flavors in pairs(self.flavors) do 
            print(M.Title(flavors)) 
            print("--------------") 
        end
    end

Store = ICS:new{restaurant_name="Kudo Delights", cuisine_type="Ice-Cream Stand"}
Store:Display_flavors() 


Privileges = {privileges = {"can Add post","can Remove Post","can Ban User",
        "can Modify User","can Access Mod Menu","can Ban other Administrators"}}
  --[[ Administrator's Privileges ]]--
    function Privileges:new(o, self) 
        o = o or {} 
        self.__index = self
        setmetatable(o, self) 
        return o
    end
        
    function Privileges:Show_privileges() 
        print("\nHello Administrator.")
        print("\nCurrently Showing Privileges: ")
        print("-------------------------------------") 
        for i, privilege in pairs(self.privileges) do
            if string.lower(privilege) == "can ban other administrators" then 
                print("{"..privilege.."}".." = False")
            else
                print("{"..privilege.."}".." = True") 
            end
        end
    end





Admin = User:new()
Ad = Admin:new()
  --[[ A Child of the 'User' , ]]-- 
    
    function Ad:new(o) 
      --[[ Administrator Inheriting from the User]]-- 
        o = o or {}
        self.__index = self
        setmetatable(o, self) 
        self.privilege = Privileges
        return o  
    end


Administrator = Ad:new{forename="Dean", location="UK", other="Administrator", surname="Chinamo"}
Administrator.privilege:Show_privileges() 

 Battery = {battery_size=70}
  --[[A simple attempt to model a Battery for an Electric Car.]]--
 
    function Battery:new(o, battery_size)
      --[[Initialize the Battery's Attributes.]]--
        self.__index = self
        setmetatable(o, self) 
        self.battery_size = battery_size
    end

    function Battery:Describe_battery()
      --[[Print a statement describing the Battery Size.]]--
        print("This Vehicle has a "..self.battery_size.."-kWh battery.\n") 
    end
    
    function Battery:Get_range() 
      --[[ A Vehicle's Range dependant on the Battery Size ]]-- 
        if self.battery_size == 70 then
            Range = 240
        elseif self.battery_size == 85 then
            Range = 270 
        end
        message = "This Car can Travel up to "..Range.." miles"
        message = message.." provided it is fully charged!\n" 
        print(message) 
    end
    
    function Battery:Upgrade_battery() 
      --[[ Upgrading a Vehicle's Battery ]]-- 
        self.battery_size = 85 
        print("Your Vehicle Battery Was Upgraded!\n") 
    end
    
    function Battery:Downgrade_battery() 
      --[[ Downgrading a Vehicle's Battery ]]-- 
        self.battery_size = 70
        print("Your Vehicle Battery was Downgraded!\n") 
    end
 
 ElectricCar = Vehicle:new()
 Ev = ElectricCar:new()
  --[[Representing Aspects of a Car, specific to Electric Vehicles.]]--
    
    function Ev:new(o)
      --[[
        Initialize attributes of the parent .
        Then initialize attributes specific to an electric Car.
      ]]--
        self.__index = self
        setmetatable(o, self) 
        self.battery = Battery
        return o  
    end
 
My_tesla = Ev:new{make='tesla', model='model s', year=2016, colour="White"}
My_tesla:Retrieve_vehicle_details() 
My_tesla.battery:Describe_battery()

My_tesla.battery:Get_range() 

My_tesla.battery:Upgrade_battery()
My_tesla.battery:Describe_battery() 
 
My_tesla.battery:Get_range() 

My_tesla.battery:Downgrade_battery() 

My_tesla.battery:Describe_battery() 
My_tesla.battery:Get_range() 

--#----------------------------------------------