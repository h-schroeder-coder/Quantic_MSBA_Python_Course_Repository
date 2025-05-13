user = (" ray", "  li", 27, 40.5)

height = 63

print("Height: ", height, " in")

print(f"That's {height * 2.54} cm")

request = "2 green and 1 red"

dusty_cms = [40, 50, 70]
fresh_cms = dusty_cms.copy()
fresh_cms[0] = 30
print(dusty_cms[0])

orders = []
orders.append("jeans")
orders.append("t-shirt")

orders.insert(1, "dress")
print(orders)

orders.append("hat")
orders.append("socks")
orders.append("sweater")
orders.append("shoes")
orders.append("dress")
orders.append("dress")
print(orders.count("dress"))
print(orders)