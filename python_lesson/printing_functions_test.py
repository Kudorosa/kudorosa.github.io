def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
 
 # Simulate creating a 3D print from the design.
        print("Printing model: " + current_design)
        completed_models.append(current_design)
 
def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
 
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []


from vehicle import Vehicle
import electric_vehicle as e

myv = Vehicle("Audi","S-Class",2017,"Black") 
print(myv.retrieve_vehicle_details()) 
myv.refuel_vehicle() 
myv.car_speed() 

myev = e.Electric_Vehicle("Tesla","Model 3",2020,"White") 
print(myev.retrieve_vehicle_details())  
