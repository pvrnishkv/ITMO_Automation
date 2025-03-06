# #ЗАНЯТИЕ №2
# #Задача №1
#
# def task_func(a=(1, 2, 3, 4)):
#     return a[1]
# print(task_func())
#
# #Задача №2
#
# def compute_surface(radius, pi=3.14159):
#     return pi * radius * radius
# print(compute_surface(2))
#
# #Задача №3
#
# def string_lenght(s: str = '') -> int:
#     return len(s)
# print(string_lenght(s='    '))
#
# #Задача №4
#
# def max_list(a: list, b: list) -> int:
#     return max(len(a), len(b))
# print(max_list([1, 2, 3, 4], [5,6]))
#
# #Задача №5
#
# def append_list(my_list: list):
#     my_list.append('test')
#     return my_list
# print(append_list(a=[1, 2]))
#
# #Задача №6
#
# def sum_list(my_list: list):
#     return sum(my_list)
# print(sum_list([1, 2, 3, 4]))
#
#ДОМАШНЕЕ ЗАДАНИЕ
# #Задача №1
#
# def task_1(a: int, b: float, c: str, d: list, e: bool) -> None:
#     return a, type(a), b, type(b), c, type(c), d, type(d), e, type(e)
# result = task_1(4, 0.06, 'слово', [1, 2], True)
#
# print(result)
#
# #Задача №2
#
# def task_2(a=[1, 2, 3, 5, 8, 13, 21]) -> list:
#     return a[0:3]
#
# print(task_2())
# #Последовательность чисел Фибоначчи
#
# #Задача №3
#
# def task_3(a: int) -> int:
#     return a**2
#
# print(task_3(5))