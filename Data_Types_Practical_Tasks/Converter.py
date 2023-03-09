import math

mpg = float(input())

consumption = (100 * 4.54) / (1.6 * mpg)
consumption = math.floor(consumption)

print(f"{consumption} litres per 100 km")