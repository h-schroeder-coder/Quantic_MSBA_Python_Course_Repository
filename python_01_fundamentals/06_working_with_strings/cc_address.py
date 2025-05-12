address = "123 Rainbow Road    "
print(address)
print(address.title())
print(address.upper())
print(address.lower())
# the address variable is a string and the address.title() method is used to capitalize the first letter of the string


print(address.strip())

# the strip() method is used to remove any leading or trailing whitespace from a string

city = "Rainbow City"

print(f'My address is: \n {address.strip()}, {city}' )


#returns 
# "My address is:
#   123 Rainbow Road, Rainbow City"