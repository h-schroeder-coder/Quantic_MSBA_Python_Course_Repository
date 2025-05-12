# integer division is a mathematical operation that divides one integer by another and returns the quotient without the remainder.
# In Python, integer division is performed using the double forward slash (//) operator.
# The syntax for integer division is:
#   result = a // b
# where 'a' is the dividend and 'b' is the divisor.
# The result will be the quotient of the division of 'a' by 'b', rounded down to the nearest integer.
# Example of integer division
a = 10
b = 3
result = a // b
print(f"The result of {a} // {b} is: {result}")  # Output: The result of 10 // 3 is: 3
# The result is 3 because 10 divided by 3 is 3.333..., and the integer division rounds it down to 3.

# The integer division operator can also be used with negative numbers.
# Example with negative numbers
a = -10
b = 3
result = a // b
print(f"The result of {a} // {b} is: {result}")  # Output: The result of -10 // 3 is: -4
# The result is -4 because -10 divided by 3 is -3.333..., and the integer division rounds it down to -4.

# The integer division operator can also be used with floating-point numbers.
# Example with floating-point numbers
a = 10.5
b = 3.2
result = a // b
print(f"The result of {a} // {b} is: {result}")  # Output: The result of 10.5 // 3.2 is: 3.0
# The result is 3.0 because 10.5 divided by 3.2 is 3.28125, and the integer division rounds it down to 3.0.

# The integer division operator can also be used with negative floating-point numbers.
# Example with negative floating-point numbers
a = -10.5
b = 3.2
result = a // b
print(f"The result of {a} // {b} is: {result}")  # Output: The result of -10.5 // 3.2 is: -4.0
# The result is -4.0 because -10.5 divided by 3.2 is -3.28125, and the integer division rounds it down to -4.0.
