first_name = input("Enter your first name: ")
#this uses a function input() to get user input
# and stores it in a variable called first_name
# the text in the parentheses is a prompt for the user
# the input() function will wait for the user to type something and press enter
# the input will be stored in the variable first_name

print(f"Hello, {first_name.title()}!")
#this uses an f-string to format the output
# the .title() method capitalizes the first letter of each word in the string
# the f-string allows us to insert the value of the variable first_name into the string
# the print() function displays the output on the screen

surname = input("Enter your surname: ")

adults = input("How many adult tickets?")
adults = int(adults)
#this converts the input from a string to an integer

kids = input("How many kids under 12?")
kids = int(kids)
#this converts the input from a string to an integer

cost = 17*adults + 14*kids
print(f"Total cost: ${cost}")

tax = round(cost*1.078, ndigits=2)
print(f"With tax: ${tax}")
#this calculates the tax by multiplying the cost by 1.078
#and rounds it to 2 decimal places because ndigits=2
#the round() function takes two arguments: the number to round and the number of decimal places
#the ndigits argument is optional and defaults to 0
#if you don't specify it, the round() function will round to the nearest integer
#the round() function rounds to the nearest even number if the number is halfway between two integers
#the print() function displays the output on the screen
#the f-string allows us to insert the value of the variable tax into the string
# you can also write the tax calculation as:
# tax = round(cost*1.078, 2)
# this will round the number to 2 decimal places

