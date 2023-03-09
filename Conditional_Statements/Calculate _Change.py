# Get price and payment inputs
price = float(input())
payment = float(input())

# Calculate the change amount in stotinki
change = int((payment - price) * 100)

# Calculate the number of coins for each denomination
lev = change // 100
change %= 100

fifty = change // 50
change %= 50

twenty = change // 20
change %= 20

ten = change // 10
change %= 10

five = change // 5
change %= 5

two = change // 2
change %= 2

one = change

# Output the number of coins for each denomination
if lev > 0:
    print(lev, "x 1 lev")
if fifty > 0:
    print(fifty, "x 50 stotinki")
if twenty > 0:
    print(twenty, "x 20 stotinki")
if ten > 0:
    print(ten, "x 10 stotinki")
if five > 0:
    print(five, "x 5 stotinki")
if two > 0:
    print(two, "x 2 stotinki")
if one > 0:
    print(one, "x 1 stotinka")
