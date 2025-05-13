temps = [65, 32, 50, -2]

for i in range(len(temps)):
  temps[i] = round((temps[i] * 9 / 5 + 32), 1)

print(temps)


temps = [65, 32, 50, -2]

for i in range(len(temps)):
  temps[i] = (temps[i] – 32)/1.8
  temps[i] = round(temps[i], 1)

print(temps)