numbers = input().split(', ')
numbers = [int(num) for num in numbers]
numbers.sort(reverse=True)
sorted_numbers = ', '.join(str(num) for num in numbers)
print(sorted_numbers)
