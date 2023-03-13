class Voters(): 
    """ Voters who Vote for Roblox Gaming Ideas """ 
    def __init__(self, question):
        """ Creating Questions for the Voters """ 
        self.question = question 
        self.results = []
    
    def display_question(self):
        """ Displaying the Question """ 
        print(self.question) 
    
    def store_response(self, response):
        """ Storing a Voter's Response into the Results Log """ 
        self.results.append(response)

    
    def display_results(self):
        """ Displaying all Voter Responses """ 
        print("The Results:\n") 
        for response in self.results:
            print("|-|- " + response) 
