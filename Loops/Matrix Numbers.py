# Get input value
N = int(input())

# Initialize matrix
matrix = [[0 for j in range(N)] for i in range(N)]

# Fill matrix with values
for i in range(N):
    for j in range(N):
        matrix[i][j] = i + j + 1

# Print matrix
for i in range(N):
    for j in range(N):
        print(matrix[i][j], end=" ")
    print()
