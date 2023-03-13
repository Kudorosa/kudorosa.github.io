class Vehicle(): 
    """ Class Representing a Vehicle """ 
    
    def __init__(self, make, model, year, colour=""): 
        """ A Vehicle and it's In-depth Information """ 
        self.make = make 
        self.model = model 
        self.year = year 
        self.colour = colour
        self.mph = 160 #Direct Update Approach. 
        """ Attributes of the Vehicle """ 
        
    def retrieve_vehicle_details(self): 
        if self.colour:
            car = ("\n'" + str(self.year) + " " + self.colour +  " " + self.make + 
                " " + self.model + "'")
        else:
            car = ("\n'" + str(self.year) + " " + self.make + 
                " " + self.model + "'")
        return car.title() 
        
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
