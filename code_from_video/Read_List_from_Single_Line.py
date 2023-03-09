letters = input().split(',')

seen = []
for letter in letters:
    if letter in seen:
        print(f'{letter} is a duplicate!')
    else:
        seen.append(letter)