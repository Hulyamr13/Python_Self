year = int(input())

# calculate the remainder of the year divided by 12
zodiac_index = year % 12

# create a list of zodiac signs
zodiac_signs = ['Monkey', 'Rooster', 'Dog', 'Pig', 'Rat', 'Ox', 'Tiger', 'Hare', 'Dragon', 'Snake', 'Horse', 'Sheep']

# print the corresponding zodiac sign
print(zodiac_signs[zodiac_index])
