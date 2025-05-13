temps = [65,  32, 50, -2]
cels_temps = []
for temp in temps:
  cels_temps.append((temp - 32) * 5 / 9)
print(cels_temps)

kel_temps = []
for temp in cels_temps:
  temp = temp + 273.15
  kel_temps.append(temp)
print(kel_temps)