function string.title(a) 
    return a:sub(1,1):upper()..a:sub(2)
end



Name = "ada lovelace"
print(string.title(Name)) --#string.title() Displays the Start of each Word with a Capital Letter.
print(string.upper(Name)) --#string.upper() Displays all Words in Capital Letters.
print(string.lower(Name)) --#string.lower() Displays all Words in Lower Case Letters.

First_name = "ada"
Last_name = "lovelace"
Full_name = First_name.." "..Last_name
Full_name = string.title(Full_name)

print("Greetings, "..Full_name.."!,".."I Hope all is Well!") --#Concatenation is Combining of Multiple Strings.

Message = "Hello, "..Full_name.."!"
print(Message)

print("\tLua") --#\t when used places a Tab to the Word infront of it. Whitespace.
print("\nLua\nIs\nThe\nBest!\n") --#\n when used Creates a New Line Displaying the Word infront. Whitespace.
print("Programming Languages:\n\tPython\n\tJavascript\n\tC#\n\tC++\n\tLua\n\tHTML\n\tCSS") --#\n\t can be used to Perform a New Line and a Tab for the Word infront.

Favourite_language = 'lua ' --#Terminal Exercise introducing .rstrip() to Erase Whitespace on the Right Side.
Favourite_language = ' lua' --#Terminal Exercise intrdoucing .lstrip() to Erase Whitespace on the Left Side.
Favourite_language = ' lua ' --#Terminal Exercise introducing .strip() to Erase Whitespace on Both Sides.


