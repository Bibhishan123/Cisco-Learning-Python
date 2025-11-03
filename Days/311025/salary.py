salaries = [] #list() => this is called constructor of list i.e init

salaries.append(33000)
salaries.append(40000)
salaries.append(99000)

print(salaries)

#To remove the last salary
# salaries.pop()

# To remove the salary based on Index
# salaries.pop(1)

# to remove the salary (figugre)
# salaries.remove(40000)

i=0
search = 40000
search_index =-1
for salary in salaries:
    if salary == search:
        search_index = i
        break
    i+=1

print(search_index)

