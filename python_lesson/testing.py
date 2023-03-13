import unittest
from electric_vehicle import Vehicle 
from voters import Voters

print("-(Press 'q' to Quit)-") 
print("Greetings, Please list down your Vehicle Details.\n") 
while False: 
    make = input("Vehicle Make: ") 
    if make.lower() == "q":
        break
    model = input("Vehicle Model: ") 
    if model.lower() == "q":
        break 
        
    try:
        year = input("Vehicle Date: ")
        if year.lower() == "q": 
            break
        year = int(year) 
        if year not in range(1980,2023):
            print("\nPlease enter a Valid Vehicle Date!\n")
            continue
    except ValueError:
        print("\nPlease Enter your Vehicle Date in Numbers only!\n") 
    colour = input("Vehicle Colour: ")
    if colour.lower() == "q":
        break
        
    else:
        your_car = Vehicle(make,model,year,colour) 
        print("\nYour Vehicle Details: " + your_car.retrieve_vehicle_details() 
        + "\n")
         
    options = ["yes","no"]
    question = input(("Do you wish Enter More Details about your other" 
    " Vehicles? ").title()) 
    if question.lower() in options == "yes": 
        continue
    if question.lower() in options == "no":
        print("Very Well, thank you and have a Good day!".title()) 
        break
    elif question.lower() not in options:
        print("We will take that as a No, have a Good Day!".title()) 
        break


class Tests(unittest.TestCase): #In-order to utilise the TestCase, you must create a Class which Inherits from it. 
    """ Various Tests for my Functions """ 
    
    def test_retrieve_vehicle_details(self):
        """ Testing to see if Retrieving Vehicle Details Work """ 
        car = Vehicle("Ford","Mustang",1991,"White")
        a = car.retrieve_vehicle_details()
        self.assertEqual(a, "\n'1991 White Ford Mustang'") #assertEqual() checks if one Value ("The One you expect to receive") and the other Value are Equal. 
    
    def test_retrieve_vehicle_details2(self):
        """ Testing to see if Retrieving some Details Work """ 
        car = Vehicle("Mercedes","S-Class",2016)
        a = car.retrieve_vehicle_details()
        self.assertEqual(a, "\n'2016 mercedes s-class'".title()) 

#Test V------------------------------------
from city_functions import city_country 

class Test(unittest.TestCase):
    """ Testing if City & Country Works """ 
    
    def test_city_country(self): 
        """ Will it output a City and a Country? """ 
        location = city_country("Santiago","Chile") 
        self.assertEqual(location, "santiago, chile".title()) 
    
    def test_city_country_population(self): 
        """ Will it output a City and Country's Population? """ 
        location = city_country("London","The United Kingdom",25000000) 
        b = "London, The United Kingdom - population 25000000"
        self.assertEqual(location, b)
 
question = "Greetings Everyone! Which Games Did you Vote For?" 
the_vote = Voters(question)

the_vote.display_question() 
print("||Type 'Quit' at any time to Abandon this Survey||".title()) 

while False:
    response = input("\nVote: ") 
    if response.title() == "Quit":
        break
    the_vote.store_response(response)
    
print("\nCongratulations for Participating Everyone!")
the_vote.display_results() 

class TestingVote(unittest.TestCase): 
    """ Testing if the Vote is working """ 
    def setUp(self): #setUp() Allows you to reuse Information without having to create it in each Method.
        """ Setting Up so we can continuously use Data """ 
        question = "What Game(s) did you Vote for?" 
        self.vote = Voters(question)
        self.results = ["Vault Evacuation","The Block",
                        "Unbound Soul Simulator"]
    
    def test_response(self):
        self.vote.store_response(self.results[-1]) 
        self.assertIn(self.results[-1], self.vote.results) 
    
    def test_multiple_response(self):
        """ Testing if Multiple Responses are stored """ 
        for response in self.results:
            self.vote.store_response(response) 
        for response in self.results:
            self.assertIn(response, self.vote.results) 

#Test V----------------
class Employee(): 
    """ A Description about an Employee """ 
    def __init__(self, first_name, last_name, annual_salary): 
        """ An Employee with a Name and Annual Salary """ 
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary
        self.bonus = 5000
    
    def give_raise(self,bonus=5000): 
        """ Giving the Employee a Raise increasing his/her/their Salary """ 
        if bonus > self.bonus:
            raised = self.annual_salary + bonus
            print("$" + str(bonus) + " was Added to your Annual Salary!") 
            print(f"{self.first_name} {self.last_name}'s Salary = $" 
            + str(raised)) 
        else:
            raised = self.annual_salary + self.bonus
            print("|The Raise must be $5000 or more!|\n") 
            print("$" + str(self.bonus) + " was added to your Annual Salary!") 
            print(self.first_name + " " + self.last_name + "'s Salary = $" + 
            str(raised)) 
            

dean = Employee("Dean","Chinamo",25000) 
dean.give_raise(300) 


class TestEmployee(unittest.TestCase): 
    """ Testing the Salary Payments """ 
    def setUp(self):
        """ Information Reusage """
        self.employee = Employee("Avneet","Chima",15000)
        self.bonus = 5000
        
    def test_default_raise(self): 
        """ Giving a Default Raise """
        default = self.employee.annual_salary + self.bonus
        self.assertEqual(default, 20000)
    
    def test_custom_raise(self, bonus=0): 
        """ Giving a Custom Raise """ 
        bonus = 10000
        if bonus > self.bonus:
            default = self.employee.annual_salary + bonus
        else:
            default = self.employee.annual_salary + self.bonus
        self.assertEqual(default, 25000) 

unittest.main()
        




























        
