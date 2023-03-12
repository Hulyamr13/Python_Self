# Initialize variables
longest_food = ""
max_length = 0

# Read input until "END"
while True:
    food = input().strip()
    if food == "END":
        break
    if len(food) >= max_length:
        max_length = len(food)
        longest_food = food

# Print the longest food
print(longest_food)
