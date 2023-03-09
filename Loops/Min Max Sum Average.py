n = int(input())
numbers = []
for i in range(n):
    number = float(input())
    numbers.append(number)

min_num = min(numbers)
max_num = max(numbers)
sum_num = sum(numbers)
avg_num = sum_num / n

print("min={:.2f}".format(min_num))
print("max={:.2f}".format(max_num))
print("sum={:.2f}".format(sum_num))
print("avg={:.2f}".format(avg_num))
