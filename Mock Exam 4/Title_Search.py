the_phrase = input().strip()
num = int(input())
all_words = []
for i in range(num):
    all_words.append(input().strip())

for word in all_words:
    letters = list(word)

    j = 0
    count = 0

    for i in range(len(letters)):
        letter_found = False
        while j < len(the_phrase):
            if letters[i] == the_phrase[j]:
                count += 1
                j += 1
                letter_found = True
                break
            j += 1
        if not letter_found:
            break

    if count < len(letters):
        print("No such title found!")
        continue

    j = 0
    if count == len(letters):
        for i in range(len(letters)):
            while j < len(the_phrase):
                if letters[i] == the_phrase[j]:
                    the_phrase = the_phrase[:j] + "#" + the_phrase[j+1:]
                    j += 1
                    break
                j += 1

    modified_title = ""
    for i in range(len(the_phrase)):
        if the_phrase[i] == "#":
            continue
        modified_title += the_phrase[i]

    print(modified_title)