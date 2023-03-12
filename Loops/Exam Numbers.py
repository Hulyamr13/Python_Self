# Read input
x = int(input())
y = int(input())
t = int(input())

# Loop through all 3-digit numbers in the interval
for i in range(x, y+1):
    # Calculate the sum of digits of the current number
    sum_digits = sum(int(digit) for digit in str(i))
    # Check if the sum of digits is equal to the target sum
    if sum_digits == t:
        # If so, print the number
        print(i)
