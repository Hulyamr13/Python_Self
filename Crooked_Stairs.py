# Read the first three brick heights and the number of layers
B1 = int(input())
B2 = int(input())
B3 = int(input())
L = int(input())

# Print the first three bricks
print(B1)
print(B2, B3)

# Generate the remaining layers
for i in range(3, L+1):
    # Calculate the heights of the current layer
    Bh1 = B3
    Bh2 = B1 + B2 + B3
    Bh3 = Bh1 + Bh2 + B3

    # Print the heights of the current layer
    print(Bh1, Bh2, Bh3)

    # Update the brick heights for the next layer
    B1 = Bh1
    B2 = Bh2
    B3 = Bh3
