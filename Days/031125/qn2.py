numbers_input = input("Enter the integers separated by spaces: ")

numbers_list = [int(num) for num in numbers_input.split()]

numbers_sum = sum(numbers_list)
numbers_avg = numbers_sum/len(numbers_list)

print(numbers_list)
print(numbers_sum)
print(numbers_avg)

with open('qn02_data.txt', 'w') as output_file:
    output_file.write(f'list: {numbers_list}\n')
    output_file.write(f'sum: {numbers_sum}\n')
    output_file.write(f'average: {numbers_sum}\n')
