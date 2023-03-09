n = int(input())

# read the integers and count their occurrences
occurrences = {}
for i in range(n):
    num = int(input())
    if num in occurrences:
        occurrences[num] += 1
    else:
        occurrences[num] = 1

# find the number with the maximum occurrences
max_occurrences = 0
most_frequent = 0
for num in occurrences:
    if occurrences[num] > max_occurrences or (occurrences[num] == max_occurrences and num < most_frequent):
        max_occurrences = occurrences[num]
        most_frequent = num

# print the most frequent number
print(most_frequent)
