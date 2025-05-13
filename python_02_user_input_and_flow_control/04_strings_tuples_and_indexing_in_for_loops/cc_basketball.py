my_string = "NBA"
for char in my_string:
    print(char.lower())

weights = [190, 185, 250, 190]

for i in range(len(weights)):
  weights[i] = weights[i] * 0.4535923 # convert to kg

heights = [1.98, 1.75, 2.03, 1.91]

bmis = []

#calculate BMI
for i in range(len(heights)):
  bmi = weights[i] / (heights[i] ** 2)
  bmi = round(bmi, 2)
  bmis.append(bmi)