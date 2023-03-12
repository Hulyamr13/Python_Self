input_list = input().split(',')

numbers = []
for x in input_list:
    numbers.append(int(x))

output_numbers = []
for i in range(1, len(numbers) + 1):
    if i not in numbers:
        output_numbers.append(str(i))


print(','.join(output_numbers))