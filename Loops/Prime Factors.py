# Get input value
N = int(input())

# Initialize list of prime factors
prime_factors = []

# Find prime factors of N
factor = 2
while N > 1:
    if N % factor == 0:
        prime_factors.append(factor)
        N //= factor
    else:
        factor += 1

# Print the prime factors in ascending order
for factor in prime_factors:
    print(factor)
