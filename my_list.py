my_list = []
# print(my_list)
my_list.append (10)
my_list.append (20)
my_list.append (30)
my_list.append (40)
my_list.insert(1, 15)
list2 = [50, 60, 70]
my_list.extend(list2)
del my_list[-1]
my_list.sort(reverse=False)

print(my_list)
print(my_list[3])