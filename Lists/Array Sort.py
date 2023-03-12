numbers = input().split(',')
zeros = []
non_zeros = []

for num in numbers:
    if num == '0':
        zeros.append(num)
    else:
        non_zeros.append(num)

print(','.join(non_zeros + zeros))
