label = input()
rank = int(input())

if label == 'a' or label == 'c' or label == 'e' or label == 'g':
    if rank % 2 == 0:
        print('light')
    else:
        print('dark')
else:
    if rank % 2 == 0:
        print('dark')
    else:
        print('light')