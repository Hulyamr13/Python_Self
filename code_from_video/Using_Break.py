hidden_letter = 'h'
while True:
    your_letter = input()
    if hidden_letter == your_letter:
        print('Correct')
        break
    elif hidden_letter > your_letter:
        print('Hidden is larger')
    else:
        print('Hidden is smaller')