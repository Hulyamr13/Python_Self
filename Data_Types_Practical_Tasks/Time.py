d = int(input())
h = int(input())
m = int(input())
s = int(input())

total_seconds = s + m * 60 + h * 60 * 60 + d * 24 * 60 * 60

print(total_seconds)