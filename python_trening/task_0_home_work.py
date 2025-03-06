#ДОМАШНЕЕ ЗАДАНИЕ №2
#Задача №1

def task_1(a: int, b: float, c: str, d: list, e: bool) -> None:
    return a, type(a), b, type(b), c, type(c), d, type(d), e, type(e)
result = task_1(4, 0.06, 'слово', [1, 2], True)

print(result)

#Задача №2

def task_2(a=[1, 2, 3, 5, 8, 13, 21]) -> list:
    return a[0:3]

print(task_2())
#Последовательность чисел Фибоначчи

#Задача №3

def task_3(a: int) -> int:
    return a**2

print(task_3(5))