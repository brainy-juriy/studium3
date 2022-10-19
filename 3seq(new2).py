# другой способ

# первый список: 1,5,17,9
# второй список: 1,2,7,5

num_1 = input("введите цифры первого списка:")
num_2 = input('введите цифры второго списка:')
num_list1 = num_1.split(',')
num_list2 = num_2.split(',')
num_list = num_list1 + num_list2
time_list = []
for i in num_list:
    if i not in time_list:
        time_list.append(i)
num_list = time_list
print(num_list)
