nums = [int(num_str) for num_str in input('Numbers (Space separated):').split()]

'''
max_num=max(nums)
min_num=min(nums)
'''
max_num = nums[0]
min_num = nums[0]

for n in nums:
    if n > max_num:
        max_num = n
    if n < min_num:
        min_num = n

with open("minmax_data.txt", "w") as out_file:
    out_file.write(f"Numbers: {nums}\n")
    out_file.write(f"Maximum: {max_num}\n")
    out_file.write(f"Minimum: {min_num}\n")

with open("minmax_data.txt", "r") as in_file:
    line1 = in_file.readline()
    line2 = in_file.readline()
    line3 = in_file.readline()

    print(line1, end='')
    print(line2, end='')
    print(line3, end='')