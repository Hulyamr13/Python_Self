def is_sorted(array):
    s = True
    for i in range(len(array)-1):
        if array[i] > array[i+1]:
            s = False
            break
    return s


n = int(input())
print_arr = []
for i in range(n):
    lst = input().strip().split(',')
    conv = [int(x) for x in lst]
    print_arr.append(str(is_sorted(conv)).lower())

print('\n'.join(print_arr))
