
from vehicle import Vehicle #You can Import a Module in a Module so the Child Classes can work when a Parent isn't Present.  

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
    """ An Electric Vehicle from the Parent(Vehicle)! """ 
    def __init__(self, make, model, year, colour, p_type = "Electric"): 
        super().__init__(make, model, year, colour) 
        
        self.self_driving = True
        self.battery = Battery() 
    
    def refuel_vehicle(self):
        print("\nElectric Vehicles do not Require Fuel!".title()) 
        
        
