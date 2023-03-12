import math

# Get input values
N = int(input())
X = float(input())

# Initialize sum and previous element
sum = 1
prev_element = 1

# Calculate sum using one loop
for i in range(1, N+1):
    # Calculate current element
    curr_element = prev_element * i / X
    # Add current element to sum
    sum += curr_element
    # Update previous element for next iteration
    prev_element = curr_element

# Print the sum with 5 digits after the decimal point
print("{:.5f}".format(sum))
