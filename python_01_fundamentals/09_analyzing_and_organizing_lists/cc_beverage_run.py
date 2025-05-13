drink_orders = ["tea", "coffee", "water", "soda", "juice", "tea", "smoothie", "protein shake", "water", "soda", "tea", "coffee", "juice", "smoothie", "protein shake"]
print(drink_orders)

print(f"There are {len(drink_orders)} orders in total.")
#len() returns the number of elements in a list
#this print function will print a string with the number of total elements in the list

print(f"There are {drink_orders.count('tea')} tea orders.")
#count() returns the number of times a value appears in a list
#this print function will print a string with the number of times "tea" appears in the list

drink_orders[1] = "cactus water"
#this will change the second element in the list to "cactus water"
#this will modify the original list
print(drink_orders)

tomorrow = drink_orders.copy()
#this will create a copy of the original list
#this will not modify the original list
print(tomorrow)

deleted_order = tomorrow.pop(3)
#this will remove the fourth element in the list and return it
#this will modify the original list
print(deleted_order)
#this will print the deleted order
print(tomorrow)
#this will print the list after the deleted order has been removed