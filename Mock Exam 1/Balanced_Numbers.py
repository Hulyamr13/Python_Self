def is_balanced(n):
    if n // 100 == 0:
        return False
    first_digit = n // 100
    last_digit = n % 10
    middle_digit = (n // 10) % 10
    return middle_digit == first_digit + last_digit

total_sum = 0
while True:
    n = int(input())
    if not is_balanced(n):
        break
    total_sum += n
print(total_sum)
