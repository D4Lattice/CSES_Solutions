num_of_nums = int(input())

num_list = list(map(int,input().split(" ")))

sum_of_num_list = sum(num_list)

full_sum = sum([x for x in range(num_of_nums+1)])

missing = full_sum - sum_of_num_list
print(missing)
