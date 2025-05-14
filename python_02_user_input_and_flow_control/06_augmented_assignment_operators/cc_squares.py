nums = [1, 2, 3, 4] # this will work as any type of iterable (tuple, range, etc)

# create a list of squares of the numbers in nums
squares = []

for num in nums:
  squares.append(num ** 2)

#compute the product of each square in squares using an augmented assignment operator and create a new list with values as strings
product = 1
join_squares = []
for square in squares: 
  product *= square
  join_squares.append(str(square))


#print the product of the squares
print(f"{' * '.join(join_squares)} = {product}")