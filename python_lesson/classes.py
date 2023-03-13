class Cat(): # OOP - a 'class' is a Unit which contains Objects and the Behaviours of it. 
    """ Making a Cat """ 
    def __init__(self, name, age): #__init__ is a Constructer which prevents Python from Assignment of Method Names Conflicting with yours. 
        self.name = name 
        self.age = age 
    """ Name and Age of the Cat """ 
    def meow(self): 
        """ Cats mostly Meow """ 
        print((self.name + " has unleashed a Meow!\n").title()) 
    
    def jump(self): 
        """ Cats mostly Jump on top of things """ 
        print((self.name + " has jumped on top of an Object!\n").title()) 

my_cat = Cat("Daisy",3) 
your_cat = Cat("Millie",5) 

print(my_cat.name.title() + " is my cute intelligent Cat!") 
print(("despite being only " + str(my_cat.age) + " years old, " + " she is"
" very active which is of course is a double-edged sword haha.\n").title())

print((your_cat.name + " is your cute ambitious cat!").title()) 
print("Your Cat's Age is " + str(your_cat.age) + " years old which is good"  
f", it is {your_cat.age - my_cat.age} years older than my cat!\n".title()) 

my_cat.meow() 
your_cat.jump() 

#Test V--------------

class Restaurant(): 
    """ Making a Restaurant """ 
    def __init__(self, restaurant_name, cuisine_type): 
        """ The Restaurant's Name and the Type of Restaurant it is """ 
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type 
    
    def describe_restaurant(self): 
        """ A Description of the Restaurant """ 
        print((self.restaurant_name + " is a " + self.cuisine_type + 
        " restaurant.\n").title()) 
    
    def open_restaurant(self): 
        """ Opening up the Restaurant """ 
        print(self.restaurant_name.title() + " is now Open!\n") 

the_restaurant = Restaurant("Kudos Bites","Fast-food")
 
print(("man, I should try out that new Restaurant called " + 
the_restaurant.restaurant_name + ", it should be good..").title()) 

print(("I heard its a " + the_restaurant.cuisine_type + " Restaurant, good!\n"
).title()) 

the_restaurant.describe_restaurant() 
the_restaurant.open_restaurant() 

good_restaurant = Restaurant("The Sulfa","Diner") 
print(("oooo, there is a nice restaurant in town called '" + 
good_restaurant.restaurant_name + "'.").title()) 
print(("judging by the name, i presume its a " + good_restaurant.cuisine_type + 
" type of Restaurant!\n").title()) 

good_restaurant.describe_restaurant() 

eaters_restaurant = Restaurant("Eaters Paradise","Buffet") 

print(("Im starving! let us goto the Restaurant called " + 
eaters_restaurant.restaurant_name + ".").title()) 
print(("Its also a " + eaters_restaurant.cuisine_type + " type of Restaurant,"
" good, just need to pay only one fee to devour 'everything'!\n").title()) 

eaters_restaurant.describe_restaurant() 

fashion_restaurant = Restaurant("Guccis Indulgence","Fancy Diner")
print(("dude, have you seen the news, theres a new fashion restaurant opening!"
" its called " + fashion_restaurant.restaurant_name + "!").title()) 
print(("the restaurant will probs be a " + fashion_restaurant.cuisine_type + 
".....\n").title()) 

fashion_restaurant.describe_restaurant() 


class User(): 
    """ Creating a User Profile """ 
    
    def __init__(self, forename, location, other, surname=""): 
        self.forename = forename
        self.surname = surname 
        self.location = location 
        self.other = other
    """ Creating a Users Information """ 
    
    def describe_user(self):
        if self.surname:
            print(("Account Information:\n"
            "--------------------\n"
            "First Name: " + self.forename + 
            "\nLast Name: " + self.surname + 
            "\nLocation: " + self.location +
            "\nMiscellaneous: " + self.other).title()) 
        else:
             print(("Account Information:\n"
            "--------------------\n"
            "First Name: " + self.forename + 
            "\nLocation: " + self.location +
            "\nMiscellaneous: " + self.other).title()) 
    """ Information will be stored above """ 
    
    def greet_user(self): 
        if self.surname:
            print(("\nGreetings " + self.forename + " " + self.surname + "," 
            " Hope you are having a Beautiful day today!\n").title()) 
        else: 
            print(("\nGreetings " + self.forename + "," 
            " Hope you are having a Beautiful day today!\n").title()) 
    
profile = User("Dean","United Kingdom","Loves Programming","Chinamo") 

profile.greet_user() 
profile.describe_user() 

profile1 = User("Avneet","United Kingdom","Social Media Star","Chima") 

profile1.greet_user() 
profile1.describe_user() 

profile2 = User("Grace","United Kingdom","Adventurerer","Stevenson") 

profile2.greet_user() 
profile2.describe_user() 

profile3 = User("Harleen","Dubai","Influencer") 

profile3.greet_user() 
profile3.describe_user() 

#------------------

class Vehicle(): 
    """ Class Representing a Vehicle, can be used to make Vehicles """ 
    
    def __init__(self, make, model, year, colour): 
        """ A Vehicle and it's In-depth Information """ 
        self.make = make 
        self.model = model 
        self.year = year 
        self.colour = colour
        self.mph = 160 #Direct Update Approach. 
        """ Attributes of the Vehicle """ 
        
    def retrieve_vehicle_details(self): 
        car = ("\n'" + str(self.year) + " " + self.colour +  " " + self.make + 
            " " + self.model + "'")
        print(car.title()) 
        
    def update_car_speed(self, mph): #Method Update Approach. 
        """ Updating Car Speed """ 
        if mph <= self.mph: #Logic Check added to the Method. 
            self.mph = mph
        else:
            print("Vehicles cannot exceed their Top Speed.".title()) 
            
    def refuel_vehicle(self):
        print("Vehicle has been Refueled!") 
    
    def car_speed(self): 
        """ Insight on the Vehicle's Speed """ 
        print("This Vehicle has a Avg Speed of " + str(self.mph) + " Mp/h.")

my_car = Vehicle("Tesla","Model X",2016,"White")  
my_car.retrieve_vehicle_details()
my_car.update_car_speed(160)
my_car.car_speed() 

class OldVehicle(): 
    """ """ 
    def __init__(self, make, model, year): 
        self.make = make 
        self.model = model 
        self.year = year 
        self.top_speed = 100
        """ """ 
    def update_speed(self, current_speed): 
        if current_speed <= self.top_speed: 
            self.top_speed = current_speed 
        else: 
            print("Vehicles cannot exceed their Top Speed!".title())
        
    def decrease_speed(self, speed): 
        """ Decreasing Vehicle Speed """ 
        self.top_speed -= speed 
        
    def car_speed(self): 
        """ The Vehicle's Speed """ 
        print("This Vehicle has an Avg Speed of " + str(self.top_speed) 
        + " Mp/h.")
        
    def vehicle_details(self): 
        """ """ 
        car = f"\n{self.make} {self.model} {self.year}"
        return car.title()

my_old_vehicle = OldVehicle("Nissan","Micra","2001") 
my_old_vehicle.vehicle_details()

my_old_vehicle.decrease_speed(10)
my_old_vehicle.update_speed(90)
my_old_vehicle.car_speed() 

my_old_vehicle.decrease_speed(-30) 
my_old_vehicle.update_speed(80) 
my_old_vehicle.car_speed() 

#Test V---------------

class Restaurant(): 
    """ Making a Restaurant """ 
    def __init__(self, restaurant_name, cuisine_type): 
        """ The Restaurant's Name and the Type of Restaurant it is """ 
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type 
        self.number_served = 10
    
    def describe_restaurant(self): 
        """ A Description of the Restaurant """ 
        print(("\n" + self.restaurant_name + " is a " + self.cuisine_type + 
        " restaurant.").title()) 
    
    def set_number_customers_served(self, served):
        """ Setting the Customers Served """ 
        if served >= self.number_served: 
            self.number_served = served
        else:
            print("Customers Served cannot be decreased!".title()) 
    
    def customers_served(self):
        """ The Amount of Customers in the Restaurant """ 
        served = ("\nThere are currently " + str(self.number_served) + 
        " customers in the restaurant who have been served.")
        return served.title()
    
    def increment_customers_served(self, serving): 
        """ Increasing the Customers Served Amount """ 
        if self.number_served + serving > self.number_served: 
            self.number_served += serving
        else:
            print("\nCustomers Served cannot be decreased!".title()) 
        
       
        
        
    def open_restaurant(self): 
        """ Opening up the Restaurant """ 
        print(self.restaurant_name.title() + " is now Open!\n") 

restaurant = Restaurant("Kudos Burgers","Fast-food") 
restaurant.describe_restaurant() 

print(restaurant.customers_served())
 
restaurant.set_number_customers_served(15) 
print(restaurant.customers_served()) 

restaurant.increment_customers_served(55) 
print(restaurant.customers_served()) 


class User(): 
    """ Creating a User Profile """ 
    def __init__(self, forename, location, other, surname=""): 
        self.forename = forename
        self.surname = surname 
        self.location = location 
        self.other = other
        self.login_attempts = 0 
    """ Creating a Users Information """ 
    
    def describe_user(self):
        if self.surname:
            print(("Account Information:\n"
            "--------------------\n"
            "First Name: " + self.forename + 
            "\nLast Name: " + self.surname + 
            "\nLocation: " + self.location +
            "\nMiscellaneous: " + self.other).title()) 
        else:
             print(("Account Information:\n"
            "--------------------\n"
            "First Name: " + self.forename + 
            "\nLocation: " + self.location +
            "\nMiscellaneous: " + self.other).title()) 
    """ Information will be stored above """ 
    
    def greet_user(self): 
        if self.surname:
            print(("\nGreetings " + self.forename + " " + self.surname + "," 
            " Hope you are having a Beautiful day today!\n").title()) 
        else: 
            print(("\nGreetings " + self.forename + "," 
            " Hope you are having a Beautiful day today!\n").title()) 
    
    def increment_login_attempts(self): 
        attempts = 1
        self.login_attempts += attempts 
        if self.login_attempts == 1:
            print(str(self.login_attempts) + " Login Attempt!".title())
        else:
            print(str(self.login_attempts) + " Login Attempts!".title())
    
    def reset_login_attempts(self): 
        self.login_attempts = 0 
        print("-Login Attempts Reset to " + str(self.login_attempts) + "-")
          
        


user = User("Dean","Uk","Loves Python","Chinamo") 

user.increment_login_attempts() 
user.increment_login_attempts() 
user.increment_login_attempts() 
user.increment_login_attempts() 

print("Total Login Attempts: " + str(user.login_attempts) + "\n") 

user.reset_login_attempts()
user.increment_login_attempts() 
user.increment_login_attempts() 
user.increment_login_attempts()

print("Total Login Attempts: " + str(user.login_attempts) + "\n") 

user.reset_login_attempts() 
print(user.login_attempts) 
user.increment_login_attempts() 
print(user.login_attempts) 


def Food(name,cal): 
    """ The Name of the Food and it's Calories """ 
    item = ("The Food presented is a " + name + ", it has " + 
    str(cal) + " calories!")
    return item.title() 
     
    
print(Food("Burger",300)) 

class Buffet(): 
    """ A Buffet filled with Food """ 
    
    def __init__(self, name): 
        self.name = name 
        self.amount = 5 
    """ Name of the Food and the Amount of it """ 
    
    def increase_serving(self, serve): 
        if self.amount + serve >= self.amount:
            self.amount += serve
            print(("\n" + str(serve) + " " + self.name + " has been added to" 
            " the Buffet!").title()) 
            print(("New amount of " + self.name + ": " + str(self.amount)
            ).title()) 
        else:
            print("\nPlease do not remove Food before Serving!".title())
            print(("Amount of " + self.name + ": " + str(self.amount)).title()) 
            
    def clear_food(self): 
        """ Clearing the Buffet Food """ 
        self.amount = 0 
        print("\nClearing Food!") 
        print((self.name + " left: " + str(self.amount)).title())
        
    def food(self):
        item = (self.name + " is included in the Buffet, the amount of " 
            + self.name + " available is: " + str(self.amount) + ".")
        print(item)


my_serving = Buffet("chips") 

my_serving.food()

my_serving.increase_serving(4)
my_serving.clear_food() 
my_serving.increase_serving(10) 
my_serving.increase_serving(-2) 

#-Inheritance V--

class Battery(): 
    """ Creating an Electric Vehicle's Battery """ 
    
    def __init__(self, battery_charge=0): 
        self.battery_charge = battery_charge

    def charge_left(self): 
        print(str(self.battery_charge) + "% Battery Charge Left..") 

    def set_battery_charge(self,charge): 
        if self.battery_charge + charge >= self.battery_charge:
            if self.battery_charge + charge <= 100:
                self.battery_charge += charge
                print(str(charge) + "% charge added to Vehicle Battery!".title())
            else:
                print("Vehicle Battery is already fully charged!".title()) 
                self.battery_charge = 100 
        else:
            print("Battery cannot be manually drained!".title()) 
    
    def range(self): 
        """ The Distance Travelled dependant on Battery Charge """ 
        if self.battery_charge == 100 or self.battery_charge >= 90: 
            range = 500 
        elif self.battery_charge <= 90 and self.battery_charge > 50: 
            range = 400 
        elif self.battery_charge <= 50 and self.battery_charge > 25: 
            range = 250
        elif self.battery_charge <= 25 and self.battery_charge > 10:
            range = 200
        else:
            range = 100
            print("\nPlease Consider Recharging your Vehicle!".title()) 
        
        notif = (f"\nThis Vehicle can Travel {range} Metres on" 
        f" {self.battery_charge}% battery.\n")
        print(notif.title())
         
class ElectricVehicle(Vehicle): 
    """ An Electric Vehicle """ 
    
    def __init__(self, make, model, year, colour, p_type = "Electric"): 
        super().__init__(make, year, model, colour) 
        self.self_driving = True
        self.battery = Battery() 
    
    def refuel_vehicle(self):
        print("\nElectric Vehicles do not Require Fuel!".title()) 
    
    

my_ev = ElectricVehicle("Tesla","Model S","2017","Black") 
my_ev.retrieve_vehicle_details()
my_ev.update_car_speed(2000) 
my_ev.car_speed() 

print("\n(Vehicle Self-Driving = " + str(my_ev.self_driving == True) + ")") 

my_ev.battery.set_battery_charge(15) 
my_ev.battery.charge_left() 
my_ev.battery.range() 
 
#Test V----------------

class IceCreamStand(Restaurant): 
    """ An Icecream Stand Inheriting from the Restaurant Class """
     
    def __init__(self, restaurant_name, cuisine_type): 
        """ Name of the Restaurant and the Cuisine Type """ 
        super().__init__(restaurant_name, cuisine_type) 
        self.flavors = ["vanilla","chocolate","mint","strawberry"] 
        
    def display_flavors(self): 
        print(("Greetings! Welcome to " + self.restaurant_name + "!").title()) 
        print("We Have the Following Ice-cream Flavors Available: \n") 
        for flavors in self.flavors: 
            print(flavors.title()) 
            print("--------------") 

store = IceCreamStand("Kudo Delights","Ice-Cream Stand") 
store.display_flavors() 


class Privileges(): 
    """ Administrator's Privileges """
    def __init__(self): 
     self.privileges = ["can add post","can remove post","can ban user",
                        "can modify user","can access Mod Menu",
                        "can ban other administrators"] 
        
    def show_privileges(self): 
        print("\nHello Administrator.")
        print("\nCurrently Showing Privileges: ")
        print("-------------------------------------") 
        for privilege in self.privileges: 
            if privilege.lower() == "can ban other administrators":
                print("{" + privilege.title() + "}" " = False")
            else:
                print("{" + privilege.title() + "}" " = True") 





class Admin(User):
    """ A Child of the 'User' Class, """ 
    
    def __init__(self, forename, location, other, surname=""): 
        """ Administrator Inheriting from the User Class """ 
        super().__init__(forename, location, other, surname="") 
        self.privilege = Privileges() 


administrator = Admin("Dean","UK","Administrator","Chinamo") 
administrator.privilege.show_privileges() 

class Battery():
    """A simple attempt to model a Battery for an Electric Car."""
 
    def __init__(self, battery_size=70):
        """Initialize the Battery's Attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the Battery Size."""
        print("This Vehicle has a " + str(self.battery_size) + "-kWh battery.") 
    
    def get_range(self): 
        """ A Vehicle's Range dependant on the Battery Size """ 
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270 
        message = "This Car can Travel up to " + str(range) + " miles "
        message += "provided it is fully charged!" 
        print(message.title()) 
    
    def upgrade_battery(self): 
        """ Upgrading a Vehicle's Battery """ 
        self.battery_size = 85 
        print("Your Vehicle Battery Was Upgraded!") 
    
    def downgrade_battery(self): 
        """ Downgrading a Vehicle's Battery """ 
        self.battery_size = 70
        print("Your Vehicle Battery was Downgraded!") 
 
 
class ElectricCar(Vehicle):
    """Representing Aspects of a car, specific to Electric Vehicles."""
    
    def __init__(self, make, model, year, colour=""):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year, colour)
        self.battery = Battery()
 
my_tesla = ElectricCar('tesla','model s', 2016, "White")
my_tesla.retrieve_vehicle_details() 
my_tesla.battery.describe_battery()

my_tesla.battery.get_range() 

my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery() 
 
my_tesla.battery.get_range() 

my_tesla.battery.downgrade_battery() 

my_tesla.battery.describe_battery() 
my_tesla.battery.get_range() 

#----------------------------------------------

from class_import import Sandwich, Cat

my_sandwich = Sandwich("Bacon","Mustard","Egg","Ham") 
print(my_sandwich.build_sandwich()) 

my_kitty = Cat("Kudiri",3) 
my_kitty.meow() 
my_kitty.scratch() 


from electric_vehicle import ElectricVehicle, Vehicle 

cars = ElectricVehicle("Polestar","1",2021,"white") 
print(cars.retrieve_vehicle_details()) 
cars.refuel_vehicle() 
print(cars.self_driving)

my_ice = Vehicle("Ford","Focus",2012,"grey") 
my_ice.refuel_vehicle() 
print(my_ice.retrieve_vehicle_details()) 
my_ice.car_speed() 
my_ice.update_car_speed(95) 
my_ice.car_speed()

import class_import as c 
my_kat = c.Cat("smithens",2)
my_kat.scratch() 
my_kat.meow() 

 

















