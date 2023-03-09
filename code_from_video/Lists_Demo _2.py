products = [
    'apple',
    'banana',
    'coffee',
    'cheese',
    'sausages',
    'spaghetti'
]

for x in range(3):
    search = input()
    matches = []
    for product in products:
        if search in product:
            matches.append(product)

    count = len(matches)
    if count == 0:
        print(f'No matches for {search}')
    else:
        print(f'{count} matches found for "{search}"')
        for match in matches:
            print(f'  {match}')