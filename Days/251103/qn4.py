names = input("Enter names (space separated): ").split()

#bubble sort logic
for i in range(len(names)):
    for j in range(i + 1, len(names)):
        if names[i].lower() > names[j].lower():
            names[i], names[j] = names[j], names[i]

sorted_list = names
# or Use 
# sorted_list = sorted(names)

names_tuple = tuple(sorted_list)

with open("names_data.txt", "w") as out_file:
    out_file.write(f"Sorted List: {sorted_list}\n")
    out_file.write(f"Tuple: {names_tuple}\n")

with open("names_data.txt", "r") as in_file:
    line1 = in_file.readline()
    line2 = in_file.readline()
   
    print(line1, end='')
    print(line2, end='')   
