user = input("Please enter your name: ")

print(f"Welcome {user}, to Beary Creamy Ice Cream!")

flavors = []

for i in range(4):
  flavor = input("Enter a flavor: ")
  flavors.append(flavor)
    
print(f"Your favorite flavors are: {flavors}")