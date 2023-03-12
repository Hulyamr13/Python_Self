# Get input value
N = int(input())

# Initialize maximum value to minimum integer value
max_num = -2**31

# Find maximum value in sequence
for i in range(N):
    num = int(input())
    if num > max_num:
        max_num = num

# Print the maximum value
print(max_num)
