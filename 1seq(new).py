my_list = []
a = int(input('введите количество цифр:'))
for i in range(a):
    new_number = int(input('введите цифру:'))
    my_list.append(new_number)
my_list.sort()
print(my_list)