n = input()

# If n is negative, remove the negative sign temporarily
if n.startswith('-'):
    is_negative = True
    n = n[1:]
else:
    is_negative = False

# Convert n to a list of digits
digits = [int(d) for d in n if d.isdigit()]

# Calculate the crooked digit
while len(digits) > 1:
    n = sum(digits)
    digits = [int(d) for d in str(n)]

# If the original number was negative, add the negative sign back
if is_negative:
    print('-' + str(digits[0]))
else:
    print(digits[0])
