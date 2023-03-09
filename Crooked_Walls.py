# Step 1: Read the sequence of wall heights from input
wall_heights = list(map(int, input().split()))

# Step 2: Calculate the absolute differences between consecutive walls
differences = [abs(wall_heights[i] - wall_heights[i-1]) for i in range(1, len(wall_heights))]

# Step 3-6: Calculate the sum of even distances using the given rules
even_sum = 0
i = 1
while i < len(differences):
    if i % 2 == 1:
        i += 1
    elif differences[i] % 2 == 0:
        even_sum += differences[i]
        i += 2
    else:
        i += 1

# Step 7: Output the sum of even distances
print(even_sum)
