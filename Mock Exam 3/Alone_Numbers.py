def alone_elements(arr, target):
    n = len(arr)
    result = arr.copy()
    for i in range(1, n-1):
        if arr[i] == target and arr[i-1] != target and arr[i+1] != target:
            if arr[i-1] > arr[i+1]:
                result[i] = arr[i-1]
            else:
                result[i] = arr[i+1]
    return result

arr = list(map(int, input().split(',')))
target = int(input())
result = alone_elements(arr, target)
print(result)