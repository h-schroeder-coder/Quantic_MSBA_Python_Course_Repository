trail = input("Which trail are you taking? ")

length = float(input("How many kms? "))
days = int(input("How many days?"))
daily = round(length / days, ndigits=1)

print(f"Welcome to the {trail}!")
print(f"You should hike {daily} kms/day.")