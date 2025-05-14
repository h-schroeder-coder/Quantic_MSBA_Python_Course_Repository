rates = [0.07, 0.04, 0.12, 0.06, 0.08]

balance = 1000

for rate in rates:
  balance *= 1 + rate
  print(balance)

payments = [250, 250, 185]
total = 0
for payment in payments:
  total += payment
print(total)