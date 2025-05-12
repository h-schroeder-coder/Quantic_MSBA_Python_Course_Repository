vin = "1HGBH41J8MN109186"

print(f"Country code: {vin[0]}")
# The first character of the VIN is the country code, which can be accessed using indexing.
# In this case, it returns "Country code: 1".
print(f"Manufacturer: {vin[1:3]}")
# The next two characters represent the manufacturer, which can be accessed using slicing.
# In this case, it returns "Manufacturer: HG".

print(f"Model year: {vin[9]}")

print(f"Serial number: {vin[-6:]}")