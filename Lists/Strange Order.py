numbers = list(map(int, input().split(',')))

negative = []
zero = []
positive = []

for num in numbers:
    if num < 0:
        negative.append(num)
    elif num == 0:
        zero.append(num)
    elif num > 0:
        positive.append(num)

sumLists = negative + zero + positive

print(','.join(map(str, sumLists)))
