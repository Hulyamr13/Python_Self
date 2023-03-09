n = input()

max_result = 0
for op1 in ['+', '*']:
    for op2 in ['+', '*']:
        expr = n[0] + op1 + n[1] + op2 + n[2]
        result = eval(expr)
        max_result = max(max_result, result)

print(max_result)
