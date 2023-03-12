# Get input value
N = int(input())

# Initialize list of numbers
nums = []

# Get N numbers and append to the list
for i in range(N):
    num = int(input())
    nums.append(num)

# Sort the list in descending order
nums.sort(reverse=True)

# Print the three largest numbers in the list in descending order
print("{}, {} and {}".format(nums[0], nums[1], nums[2]))
