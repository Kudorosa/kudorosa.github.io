M = require("helpful_functions") 

T = {}

function T.Print_models(unprinted_designs, completed_models)
    --[[
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    --]]
    while #unprinted_designs > 0 do
        Current_design = table.remove(unprinted_designs, #unprinted_designs) 
 --# Simulate creating a 3D print from the design.
        print("Printing model: "..M.Title(Current_design))
        table.insert(completed_models, Current_design)
    end
end
 
function T.Show_completed_models(completed_models)
    --[[ Show all the models that were printed. ]]--
    print("\nThe following models have been printed:")
    for i, completed_model in pairs(completed_models) do
        print(M.Title(completed_model))
    end
end 

A = require("vehicle") 
B = require("electric_vehicle")

Myv = Vehicle:new{make="mercedes", model="s-Class", year=2017, colour="black"}
Myv:Refuel_vehicle() 
Myv:Car_speed() 

Myev = Ev:new{make="tesla", model="model 3", year=2020, colour="white"} 
print(Myev:Retrieve_vehicle_details())

return T