# Get input value
N = int(input())

# Initialize products for odd and even lines
odd_product = 1
even_product = 1

# Calculate products for odd and even lines
for i in range(1, N+1):
    num = int(input())
    if i % 2 == 1:
        odd_product *= num
    else:
        even_product *= num

# Check if products are equal and print result
if odd_product == even_product:
    print("yes {}".format(odd_product))
else:
    print("no {} {}".format(odd_product, even_product))
