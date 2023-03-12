list1 = input().split(',')
list2 = input().split(',')
combined_list = []

for i in range(len(list1)):
    combined_list.append(list1[i])
    combined_list.append(list2[i])

print(','.join(combined_list))
