celsius_list = input().split()

for celsius in celsius_list:
    fahrenheit = (int(celsius) * 9/5) + 32
    print(round(fahrenheit))
