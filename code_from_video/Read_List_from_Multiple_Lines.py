total_number_of_letters = int(input())

letters = []
for _ in range(total_number_of_letters):
    letters.append(input())

print(sorted(letters))