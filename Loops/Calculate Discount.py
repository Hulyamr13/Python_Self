n = int(input())

for i in range(n):
    price = float(input())
    discounted_price = price * 0.35 # 65% discount
    print("{:.2f}".format(discounted_price)) # format to 2 decimal places
