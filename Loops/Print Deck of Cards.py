sign = input()
number = 0

if sign == "J":
    number = 11
elif sign == "Q":
    number = 12
elif sign == "K":
    number = 13
elif sign == "A":
    number = 14
else:
    number = int(sign)

for i in range(2, number+1):
    if i == 11:
        str_card = "J"
    elif i == 12:
        str_card = "Q"
    elif i == 13:
        str_card = "K"
    elif i == 14:
        str_card = "A"
    else:
        str_card = str(i)

    print(f"{str_card} of spades, {str_card} of clubs, {str_card} of hearts, {str_card} of diamonds")
