import time
from tkinter import messagebox


# Задача 1
def calc():
    #2+2
    print(2+2)
    print(37/10)
    print(37//10)
    print(37%10)


# Задача 2
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hello, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Задача 3
def show_types():
    a = 3
    print(type(a))
    a = 3.5
    print(type(a))
    a = 'qwerty'
    print(type(a))
    a = True
    print(type(a))
    a = '123'
    print(type(a))


# Задача 4
def change_type():
    a = 5.7
    print(int(a))
    b = -5.7
    print(int(b))
    c = 3**39 - int(float(3**39))
    print(c, type(c))


# Задача 5
def ask_name():
    name = input('Введите имя:')
    print('Приветствую,', name)


# Задача 6
def solve_ex():
    print('Доктор Иванов добирается на машине X часов до частной клиники, где работает.')
    print('После обеда он идёт работать в поликлинику и доходит за Y минут.')
    x = int(input('Введите X:'))
    y = int(input('Введите Y:'))
    time = x * 60 * 2 + y * 2
    print('В дороге доктор проводит', time, 'минут.')


# Задача 7
def solve_bool():
    a = False
    b = True
    c = False
    result = not a or b and c
    print(result)
    result = (not a or b) and c
    print(result)


# Задача 8
def check_year():
    year = int(input('Введите год от 1900 до 3000:'))
    if (year < 1900) or (year > 3000):
        print('Неверный год.')
    elif (year % 400 == 0) or (year % 4 == 0) and (year % 100 != 0):
        print('С днём рождения!')
    else:
        print('Год обычный.')


# Задача 9
def print_even(last_num):
    i = 1
    while i <= last_num:
        if i % 2 == 0:
            print(i, end=' ')
        i += 1


# Задача 10
def sum_numbers(i):
    sum_of = 0
    while i != 0:
        sum_of += i
        i = int(input('Введите число:'))
    else:
        print(sum_of)


# Задача 11
def count_noc():
    print('Доктор Иванов 29 февраля испек дома огромную пиццу, чтобы угостить своих коллег. \n'
          'Но он не знает заранее куда его сегодня вызовут на работу, если в клинику, то там будет X коллег, \n'
          'а если в поликлинику – то Y коллег. Он хочет разрезать пиццу дома на столько кусочков, \n'
          'чтобы каждому досталось поровну, но при этом кусочки должны быть максимально большие.')
    x = int(input('Введите X:'))
    y = int(input('Введите Y:'))
    mult_x = 1
    mult_y = 1
    while x * mult_x != y * mult_y:
        if x * mult_x > y * mult_y:
            mult_y += 1
            # print('mult y = ', mult_y)
        elif x * mult_x < y * mult_y:
            mult_x += 1
            # print('mult x = ', mult_x)
    print('Необходимо ', x * mult_x, ' кусочков.')


# Задача 12
def print_even_2(last_num):
    for i in range(1, last_num + 1):
        if i % 2 == 0:
            print(i, end=' ')


# Задача 13
def print_table():
    print('Вывести таблицу умножения [a, b]x[c,d].')
    a = int(input('Введите a:'))
    b = int(input('Введите b:'))
    c = int(input('Введите c:'))
    d = int(input('Введите d:'))
    print(' ', end='\t')
    for k in range(c, d + 1):
        print(k, end='\t')
    print()
    for i in range(a, b + 1):
        print(i, end='\t')
        for j in range(c, d + 1):
            print(i * j, end='\t')
        print()


# Задача 14
def calc_matrix(m_size):
    matrix = [[0 for i in range(m_size)] for j in range(m_size)]
    direction = 1
    i = 0
    j = 0
    for k in range(1, m_size * m_size + 1):
        matrix[j][i] = k
        if direction % 4 == 1:
            if i < m_size - (direction // 4) - 1:
                i += 1
            else:
                direction += 1
                j += 1
        elif direction % 4 == 2:
            if j < m_size - (direction // 4) - 1:
                j += 1
            else:
                direction += 1
                i -= 1
        elif direction % 4 == 3:
            if i > 0 + (direction // 4):
                i -= 1
            else:
                direction += 1
                j -= 1
        elif direction % 4 == 0:
            if j > 0 + (direction // 4):
                j -= 1
            else:
                direction += 1
                i += 1
    for i in range(m_size):
        for j in range(m_size):
            print(matrix[i][j], end='\t')
        print()


# Задача 15
def show_reminder():
    messagebox.showinfo('Useful Python', 'Пора отдохнуть от экрана.')
    time.sleep(5)
    show_reminder()


def choose_ex(a):
    if a == 1:
        calc()
    elif a == 2:
        print_hi('World')
    elif a == 3:
        show_types()
    elif a == 4:
        change_type()
    elif a == 5:
        ask_name()
    elif a == 6:
        solve_ex()
    elif a == 7:
        solve_bool()
    elif a == 8:
        check_year()
    elif a == 9:
        print_even(20)
    elif a == 10:
        first_i = int(input('Введите число:'))
        sum_numbers(first_i)
    elif a == 11:
        count_noc()
    elif a == 12:
        print_even_2(20)
    elif a == 13:
        print_table()
    elif a == 14:
        m_size = int(input('Введите размерность:'))
        calc_matrix(m_size)
    elif a == 15:
        show_reminder()
    else:
        print('Неверный номер задачи.')
    new_num = int(input('Укажите номер задачи:'))
    choose_ex(new_num)


if __name__ == '__main__':
    num = int(input('Укажите номер задачи:'))
    choose_ex(num)
