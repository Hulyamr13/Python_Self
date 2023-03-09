n = int(input())
array = [int(input()) for i in range(n)]

merging_numbers = []
for i in range(1, n):
    n1 = (array[i-1] % 10) * 10
    n2 = array[i] // 10
    merging_numbers.append(n1 + n2)

squashed_numbers = []
for i in range(1, n):
    n1 = (array[i-1] // 10) * 100
    mid = (array[i-1] % 10) + (array[i] // 10)
    if mid > 10:
        n2 = (mid - 10) * 10
    elif mid < 10:
        n2 = mid * 10
    else:
        n2 = 0
    n3 = array[i] % 10
    squashed_numbers.append(n1 + n2 + n3)

print(' '.join(str(x) for x in merging_numbers))
print(' '.join(str(x) for x in squashed_numbers))
