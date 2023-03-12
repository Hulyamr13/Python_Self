input_list = input().split(",")
input_set = set(map(int, input_list))
n = len(input_list)
all_set = set(range(1, n+1))
missing_set = all_set - input_set
missing_list = sorted(list(missing_set))
print(",".join(map(str, missing_list)))
