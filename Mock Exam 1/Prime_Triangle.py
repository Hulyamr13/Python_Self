n = int(input())
prime_nums = []

for i in range(1, n + 1):
    counter = 0

    for j in range(1, i + 1):
        if i % j == 0:
            counter += 1

    if counter <= 2:
        prime_nums.append(i)

max_n = max(prime_nums)
binary = [0] * max_n

for i in range(1, max_n + 1):
    counter = 0

    for j in range(1, i + 1):
        if i % j == 0:
            counter += 1

    if counter > 2:
        binary[i - 1] = 0
    else:
        binary[i - 1] = 1

for i in range(len(prime_nums)):
    for index_j in range(prime_nums[i]):
        print(binary[index_j], end='')
    print()
