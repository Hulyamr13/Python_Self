elements = input().strip().split(',')
unique_elements = []

for element in elements:
    if element not in unique_elements:
        unique_elements.append(element)

print(','.join(unique_elements))
