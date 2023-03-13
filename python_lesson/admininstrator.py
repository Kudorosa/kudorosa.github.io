from user import User 

class Privileges(): 
    """ Administrator's Privileges """
    
    def __init__(self): 
     self.privileges = ["can add post","can remove post","can ban user",
                        "can modify user","can access Mod Menu",
                        "can ban other administrators"] 
        
    def show_privileges(self): 
        print("\nHello Administrator.")
        print("\nCurrently Showing Privileges: ")
        print("-------------------------------------") 
        for privilege in self.privileges: 
            if privilege.lower() == "can ban other administrators":
                print("{" + privilege.title() + "}" " = False")
            else:
                print("{" + privilege.title() + "}" " = True") 

class Admin(User):
    """ A Child of the Parent(User)! """ 
    
    def __init__(self, forename, location, other, surname=""): 
        """ Administrator Inheriting from the User Class """ 
        super().__init__(forename, location, other, surname="") 
        self.privilege = Privileges() 
