n = int(input())

# Initialize sum of odd and even digits to 0
odd_sum = 0
even_sum = 0

# Iterate over the digits of n
for digit in str(n):
    if int(digit) % 2 == 0:
        even_sum += int(digit)
    else:
        odd_sum += int(digit)

# Compare odd_sum and even_sum
if odd_sum > even_sum:
    print(str(odd_sum) + " cups of coffee")
elif even_sum > odd_sum:
    print(str(even_sum) + " energy drinks")
else:
    print(str(even_sum) + " of both")

