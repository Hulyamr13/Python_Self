n = int(input())
total = 0
for i in range(n):
    value = float(input())
    total += value
average = total / n
print("{:.2f}".format(average))
