A = require("vehicle")

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
    