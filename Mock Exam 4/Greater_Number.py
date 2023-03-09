first_arr = list(map(int, input().split(',')))
second_arr = list(map(int, input().split(',')))

result = []
for num in first_arr:
    index = second_arr.index(num)
    for i in range(index, len(second_arr)):
        if second_arr[i] > num:
            result.append(second_arr[i])
            break
    else:
        result.append(-1)

print(','.join(map(str, result)))