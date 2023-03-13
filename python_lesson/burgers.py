def make_burgers(fillings,sauce): 
    """ Making a Burger with Fillings and Sauce """ 
    print(("Alright, so you want, " + fillings + " with " + sauce + " sauce on" 
   " your burger?").title()) 


def make_gun(*attachments): 
    """ A Variety of Sandwiches """
    print(("\nso you want a weapon with " + str(len(attachments)) + 
    " attachments which consist of a:").title()) 
    for item in attachments:
        print("- " + item.title())

def decisions(language,reason,current_language):
    """ ------ """ 
    print(("should I learn " + language + "? " + reason + ", or maybe I should"
    " stay with " + current_language + " instead...decisions....").title()) 


