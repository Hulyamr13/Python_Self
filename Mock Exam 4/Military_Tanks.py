# read tank moves from input
moves = input().strip()

# initialize tank position to (0, 0)
x, y = 0, 0

# process each move in the sequence
for move in moves:
    if move == 'R':
        x += 1
    elif move == 'L':
        x -= 1
    elif move == 'U':
        y += 1
    elif move == 'D':
        y -= 1

# output final tank position
print("({}, {})".format(x, y))
