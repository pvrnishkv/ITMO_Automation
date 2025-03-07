#ДОМАШНЕЕ ЗАДАНИЕ №3
#Задача №1
from itertools import count


def max_num(a, b):
    if a > b:
        print(a)
    else:
        print(b)

max_num(6,9)

#Задача №2

def diff_num(a, b):
    if a + 135 == b or b + 135 == a or a - 135 == b or b - 135 == a:
        print('Yes')
    else:
        print('No')

diff_num(-135, -270)

#Задача №3

def season(month_num):
    if month_num == 12 or month_num == 1 or month_num == 2:
        print('Зима')
    elif month_num in range(3, 6):
        print('Весна')
    elif month_num in range(6, 9):
        print('Лето')
    elif month_num in range(9, 12):
        print('Осень')
    else:
        print('Введите корректный номер месяца')

season(12)

#Задача №4

def num(a, b, c):
    if a > 10 and b > 10 and c > 10:
        print('Yes')
    else:
        print('No')

num(50, 12, 40)

#Задача №5

def positive(nums):
    count = 0
    for elem in nums:
        if elem > 0:
            count = count + 1
    return count

nums = [-9, 0, 6, 8, -1]
count_nums = positive(nums)
print('Количество положительных чисел', count_nums)

#Задача №6

def amount_days(a: int, b: int):
    return (a * 348) + (b * 29)

print ('Количество дней', amount_days(5, 6))

