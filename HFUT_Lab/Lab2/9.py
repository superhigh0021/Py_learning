str = input("Please input a string of password: ")
print_list = []
list_str = str.split(',')
#第一个是总标志，后面五个是细分的标准
for sstr in list_str:
    list_flag = [0, 0, 0, 0, 0]
    if len(sstr) >= 6 and len(sstr) <= 12:
        list_flag[0] = 1
    for item in sstr:
        if item.islower():
            list_flag[1] = 1
        elif item.isdigit():
            list_flag[2] = 1
        elif item.isupper():
            list_flag[3] = 1
        elif item == '$' or item == '#' or item == '@':
            list_flag[4] = 1
    for x in list_flag:
        if x != 1:
            break
    else:
        print_list.append(sstr)
    del list_flag
print_str = ','.join(print_list)
print(print_str)