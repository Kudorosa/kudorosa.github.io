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