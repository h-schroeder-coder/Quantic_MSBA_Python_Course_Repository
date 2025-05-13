user_first_name = input("Enter your first name: ")
# this uses a function input() to get user input
# and stores it in a variable called user_first_name

print(f"Hello, {user_first_name.title()}! Welcome to the tip calculator!")
# this uses an f-string to format the output
# the .title() method capitalizes the first letter of each word in the string
# the f-string allows us to insert the value of the variable user_first_name into the string

total_restaurant_bill = input("Enter the total amount of the restaurant bill in USD: $")
# this uses a function input() to get user input    
# and stores it in a variable called total_restaurant_bill

desired_tip_percentage = int(input("Enter the desired tip percentage (e.g., 15 for 15%): "))
# this uses a function input() to get user input   
# and stores it in a variable called desired_tip_percentage
# the input() function will wait for the user to type something and press enter
# the input will be stored in the variable desired_tip_percentage
# the input() function will return a string
# the int() function converts the string to an integer

total_tip = round(float(total_restaurant_bill) * (desired_tip_percentage / 100), ndigits=2)
# this calculates the tip by multiplying the total_restaurant_bill by the desired_tip_percentage divided by 100
# and rounds it to 2 decimal places because ndigits=2

print(f"Hi, {user_first_name}! \n A {desired_tip_percentage} % tip on ${total_restaurant_bill} is ${total_tip}. \n Your total amount with tip included is ${float(total_restaurant_bill) + total_tip}.")
# this uses an f-string to format the output
# the f-string allows us to insert the value of the variable user_first_name into the string
# the f-string allows us to insert the value of the variable desired_tip_percentage into the string
# the f-string allows us to insert the value of the variable total_restaurant_bill into the string
# the f-string allows us to insert the value of the variable total_tip into the string
# the \n character is a newline character