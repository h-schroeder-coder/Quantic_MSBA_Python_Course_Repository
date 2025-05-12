name = "SAM"
print("Hi, " + name.title() + "!")
# the name variable is a string and the name.title() method is used to capitalize the first letter of the string

#methods use the syntax: string.method()
# the .capitalize() method is used to capitalize the first letter of a string
# the .title() method is used to capitalize the first letter of each word in a string
# the .upper() method is used to convert all letters in a string to uppercase
# the .lower() method is used to convert all letters in a string to lowercase
# the .strip() method is used to remove any leading or trailing whitespace from a string
# the .replace() method is used to replace a substring with another substring in a string
# the .find() method is used to find the index of a substring in a string
# the .count() method is used to count the number of occurrences of a substring in a string
# the .split() method is used to split a string into a list of substrings
# the .join() method is used to join a list of strings into a single string
# the .format() method is used to format a string by replacing placeholders with values
# the .f-string method is used to format a string by embedding expressions inside curly braces

name = name.title
# the name variable is a string and the name.title() method is used to capitalize the first letter of the string; here we have reassigned the name variable to the name.title() method

print("Hi, " + name + "!")
# the name variable is a string and the name.title() method is used to capitalize the first letter of the string

device = "iPhone"
print(device.title())
print(device.upper())
print(device.lower())
# the device variable is a string and the device.title() method is used to capitalize the first letter of the string

#the backslash character is used to escape special characters in a string
# the \n character is used to create a new line in a string

print("Included:\nDrinks\nSnacks\nFood")
#the \n character is used to create a new line in a string

# the strip() method is used to remove any leading or trailing whitespace from a string
# the lstrip() method is used to remove any leading (left) whitespace from a string
# the rstrip() method is used to remove any trailing (right) whitespace from a string

print(f"Hi, {name.title()}!")
# the f-string method is used to format a string by embedding expressions inside curly braces
# in an f-string you can use any expression inside the curly braces, including variables, method calls, and arithmetic expressions
# in an f-string you can use either single or double quotes to define the string
# in an f-string, to get an actual curly brace in the output, you need to use double curly braces {{ and }}. This is because the single curly braces are used to define the expressions inside the f-string
# in an f-string you can use escape sequences anywhere in the string, except inside an expression