model = "IF7680C"
# The mattress model is a string, and we can access its characters using indexing.


print(model[1])
# The last character can be accessed using a negative index, which counts from the end of the string.

print(model[6])

print(model[0])
# The first character is at index 0, the second at index 1, and so on.

print(model[-3])
# The last characters can be accessed using a negative index, which counts from the end of the string.
# for example, the third to last character can be accessed using -3, the second to last using -2, and so on.
# print(model[-3]) returns the character at index -3, which is the 3rd character from the end of the string (in this case it returns '8').

print(model[2:4])
# We can also slice the string to get a substring. 
# the slice you return is dependentup on the start and end index put into the slice brackets.
# The slice [2:4] returns the characters at index 2 and 3, but not 4, in this case '76'.
# The slice starts at index 2 and goes up to, but does not include, index 4.

# variable[x: ] where x is the starting index and the slice goes to the end of the string.
# variable [:y] where y is the ending index and the slice starts at the beginning of the string.

inquiry = "Topper? Yes/No"

print(f"You chose: {inquiry[-2:]} {inquiry[0:6]}")
# returns "You chose: No Topper"

total = int(model[4:6]) + 4
# The slice [4:6] returns the characters at index 4 and 5, but not 6, in this case '80'.
# this then converts the string '80' to the integer 80 and adds 4 to it, resulting in 84.
print(f"Total length: {total} inches")
# returns "Total length: 84 inches"

print(f"Quality level: {model[-1].lower()}")
# the case and whitespace of the string can be changed too. This is done using the methods .lower() and .upper() and .strip()

category = "budget"
print(f"Category: {category[0]}")
#returns "Category: b"

print(f"Category: {category[2:4]}")
#returns "Category: dg"

print(f"Category: {category[-2:]}")
#returns "Category: et"

print(f"Category: {category[0:3]}")
#returns "Category: bud"