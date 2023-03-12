numbers = input().split(",")
numbers = [int(num) for num in numbers]

avg = sum(numbers) / len(numbers)
print(f"avg: {avg:.2f}")

below_avg = [num for num in numbers if num < avg]
above_avg = [num for num in numbers if num > avg]

print("below:", end=" ")
print(*below_avg, sep=",")

print("above:", end=" ")
print(*above_avg, sep=",")