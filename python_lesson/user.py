class User(): 
    """ Creating a User Profile """ 
    
    def __init__(self, forename, location, other, surname=""): 
        self.forename = forename
        self.surname = surname 
        self.location = location 
        self.other = other
        self.login_attempts = 0 
    """ Creating a Users Information """ 
    
    def describe_user(self):
        if self.surname:
            print(("Account Information:\n"
            "--------------------\n"
            "First Name: " + self.forename + 
            "\nLast Name: " + self.surname + 
            "\nLocation: " + self.location +
            "\nMiscellaneous: " + self.other).title()) 
        else:
             print(("Account Information:\n"
            "--------------------\n"
            "First Name: " + self.forename + 
            "\nLocation: " + self.location +
            "\nMiscellaneous: " + self.other).title()) 
    """ Information will be stored above """ 
    
    def greet_user(self): 
        if self.surname:
            print(("\nGreetings " + self.forename + " " + self.surname + "," 
            " Hope you are having a Beautiful day today!\n").title()) 
        else: 
            print(("\nGreetings " + self.forename + "," 
            " Hope you are having a Beautiful day today!\n").title()) 
    
    def increment_login_attempts(self): 
        attempts = 1
        self.login_attempts += attempts 
        if self.login_attempts == 1:
            print(str(self.login_attempts) + " Login Attempt!".title())
        else:
            print(str(self.login_attempts) + " Login Attempts!".title())
    
    def reset_login_attempts(self): 
        self.login_attempts = 0 
        print("-Login Attempts Reset to " + str(self.login_attempts) + "-")
