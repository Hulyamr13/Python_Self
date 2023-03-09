products = [
    'apple',
    'banana',
    'coffee',
    'cheese',
    'sausages',
    'spaghetti'
]

for x in range(2):
    search = input()
    if search in products:
        print(f'We have {search}')
    else:
        print(f'We do not have {search}')
