n = int(input())
best_ratio = float('inf')
best_food = ''

for i in range(n):
    food = input()
    letters = len(food)
    vowels = sum(1 for c in food if c in 'aeiou')
    ratio = vowels / letters
    if ratio < best_ratio:
        best_ratio = ratio
        best_food = food
    elif ratio == best_ratio:
        if vowels > sum(1 for c in best_food if c in 'aeiou'):
            best_food = food
        elif vowels == sum(1 for c in best_food if c in 'aeiou'):
            if letters > len(best_food):
                best_food = food

print(best_food, f'{sum(1 for c in best_food if c in "aeiou")}/{len(best_food)}')
