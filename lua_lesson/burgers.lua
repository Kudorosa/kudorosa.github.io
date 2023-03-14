M = require("helpful_functions") 
B = {}

function B.Make_burgers(fillings, sauce) 
    --[[Making a Burger]]--
    print("Alright, so you want "..fillings.." with "..sauce.." Sauce on your Burger?")
end

function B.Make_gun(...) -- ... to Create a Variable Parameter.
    --[[A Variety of Weapon Attachments]]--
    print("\nSo you want a Weapon with ".. #{...} .." Attachments which consist of a: ") 
    for i, item in pairs({...}) do -- Placing Curly Brackets converts it into a Table.
        print("- ".. item..".") 
    end
end

function B.Make_decision(language, reason, current_language) 
    --[[Making a Decision about a Language]]--
    print("\nShould I Learn "..language.."? "..reason..", or maybe I should"..
    " stay with "..current_language.." instead...decisions...decisions...")
end

B.Make_burgers("Steak","Ketchup")
B.Make_gun("Suppressor","Acog","Extended Magazine","Laser Sight")
B.Make_decision("C#","It will allow me to make Games","Lua") 

return B