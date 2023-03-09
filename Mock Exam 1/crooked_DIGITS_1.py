num = input().strip()

while len(num) > 1:
    digit_sum = 0
    for digit in num:
        if digit.isdigit():
            digit_sum += int(digit)
    num = str(digit_sum)

print(num)
