n = int(input())
sum_of_digits = 0

# Extract each digit from the number and add it to the sum_of_digits variable
for digit in str(n):
    sum_of_digits += int(digit)

print(sum_of_digits)