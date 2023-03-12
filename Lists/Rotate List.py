lst = input().split(',')
n = int(input())

for i in range(n):
    lst.append(lst.pop(0))

print(','.join(lst))
