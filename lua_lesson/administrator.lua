A = require("User") 

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