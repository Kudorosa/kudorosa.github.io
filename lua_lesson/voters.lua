Voters = {}
    --[[ Voters who Vote for Roblox Gaming Ideas ]]--
    function Voters:new(o, question)
        --[[ Creating Questions for the Voters ]]--
        o = o or {}
        self.__index = self
        setmetatable(o, self)
        self.question = question 
        self.results = {}
        return o 
    end
    
    function Voters:Display_question()
    --[[ Displaying the Question ]]--
        print(self.question) 
    end
    
    function Voters:Store_response(response)
    --[[ Storing a Voter's Response into the Results Log]]--
        table.insert(self.results, response)
    end

    
    function Voters:Display_results()
    --[[Displaying all Voter Responses]]--
        print("The Results:\n") 
        for i, responsed in pairs(self.results) do
            print("|-|- "..responsed) 
        end
    end
