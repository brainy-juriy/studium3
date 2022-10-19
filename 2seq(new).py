import re
numbers = input('введите цифры:')
numbers = re.split("[,!?:/;]", numbers)
uniq_num_list = list(set(numbers))
print(uniq_num_list)
