cart_items = ["milk", "eggs", "bread", "butter", "cinnnamon", "sugar"]
print(cart_items)

cart_items.insert(0, "chocolate")
print(cart_items)

del cart_items[-2]
print(cart_items)

cart_items.remove("eggs")
print(cart_items)

print(f"Okay, we've packed your {cart_items.pop(-1)}s.")