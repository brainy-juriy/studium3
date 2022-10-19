# первый список: 1,5,17,9
# второй список: 1,2,7,5

num_1 = input("введите цифры первого списка:")
num_2 = input('введите цифры второго списка:')
num_list1 = num_1.split(',')
num_list2 = num_2.split(',')
for i in num_list1:
    if i in num_list2:
        num_list1.remove(i)
    else:
        num_list2.append(i)
print(num_list2)
