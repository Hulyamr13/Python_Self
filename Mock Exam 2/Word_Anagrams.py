from collections import Counter

# Read input
w = input().strip()
n = int(input())
words = [input().strip() for _ in range(n)]

# Create a Counter object for the letters in w
w_counter = Counter(w)

# Check if each word in words is an anagram of w
for word in words:
    # Create a Counter object for the letters in the current word
    word_counter = Counter(word)
    if word_counter == w_counter:
        print("Yes")
    else:
        print("No")
