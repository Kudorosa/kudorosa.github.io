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