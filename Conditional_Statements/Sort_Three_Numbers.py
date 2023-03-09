# Read in the three numbers
num1 = int(input())
num2 = int(input())
num3 = int(input())

# Sort the numbers using nested if statements
if num1 >= num2:
    if num2 >= num3:
        print(num1, num2, num3)
    elif num1 >= num3:
        print(num1, num3, num2)
    else:
        print(num3, num1, num2)
else:
    if num1 >= num3:
        print(num2, num1, num3)
    elif num2 >= num3:
        print(num2, num3, num1)
    else:
        print(num3, num2, num1)
