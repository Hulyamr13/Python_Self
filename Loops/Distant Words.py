target = int(input())
n = int(input())

words = []
total_distance = 0

for i in range(n):
    word = input().strip()
    distance = sum([ord(c.lower()) - 96 for c in word])
    distance_diff = abs(distance - target)
    words.append((word, distance_diff))
    total_distance += distance_diff

for word, distance_diff in words:
    print(word, distance_diff)

average_distance = total_distance / n
print("{:.2f}".format(average_distance))
