import pymysql


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def check_str(first_str):
    first_str = first_str.replace(' ', '')
    first_str = first_str.lower()
    second_str = ''
    for i in range(len(first_str)-1, -1, -1):
        second_str = second_str + first_str[i]
    if first_str == second_str:
        print('Палиндром.')
    else:
        print('Не палиндром.')
    new_num = int(input('Укажите номер задачи:'))
    choose_ex()


def find_min():
    new_string = ''
    string_list = []
    max_list = []
    i = 0
    while new_string != 'end':
        new_string = input('Введите числа или "end"')
        string_list.append(new_string)
        i += i
    for i in range(0, len(string_list) - 1):
        temp_string = string_list[i]
        string_list[i] = temp_string.split()
        local_max = int(string_list[i][0])
        for j in range(0, len(string_list[i])):
            if int(string_list[i][j]) > local_max:
                local_max = int(string_list[i][j])
        max_list.append(local_max)
    for i in range(0, len(max_list)):
        print(max_list[i])
    print('end.')
    new_num = int(input('Укажите номер задачи:'))
    choose_ex()


def count_names():
    names_str = input('Введите строку:')
    names_list = names_str.lower().split()
    names_dict = {names_list[0]: 1}
    for i in range(1, len(names_list)):
        if names_list[i] in names_dict:
            names_dict[names_list[i]] += 1
        else:
            names_dict[names_list[i]] = 1
    i = 0
    for key, value in names_dict.items():
        i += 1
        print(str(i) + ') ' + key, value)


def mysql_call():
    connect = pymysql.connect(host='localhost', user='root', password='pass', database='my_db')
    year = input('Введите год:')
    sql = f'select first_name, last_name, date_of_birth from user where year(date_of_birth) = {year}'
    curs = connect.cursor()
    curs.execute(sql)
    for rec in curs:
        print(rec[0], rec[1], rec[2])


def choose_ex():
    num = int(input('Укажите номер задачи:'))
    if num == 1:
        check_str(input('Введите строку:'))
    elif num == 2:
        find_min()
    elif num == 3:
        count_names()
    elif num == 4:
        mysql_call()
    else:
        print('Неверный номер задачи.')
    choose_ex()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    choose_ex()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
