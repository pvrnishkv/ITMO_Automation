#Определяем функцию
def add(x, y):
    return x + y

#Вызываем функцию
print(add(1, 2))

print(add('I a', 'm tester'))

def arg(a, b, c=2, d=3):
    return a + b + c + d


print(arg(1, 1, 1, 1))

print(arg(2,2))

print(arg(1, 1, 1))

print(arg(2, 2, 4.5))

# print(arg(2,2, '1', 2))

def range_arg(a, b, c, d):
    return a + ' ' + b + ' ' + c + ' ' + d

print(range_arg('1', '2', '3', '4'))

print(range_arg('1', '2', d='3', c='4'))

#Задача

def task_func(a=(1, 2, 3, 4)):
    return a[1]
print(task_func())

#Задача

def compute_surface(radius, pi=3.14159):
    return pi * radius * radius
print(compute_surface(2))

#Задача

def append_list(my_list: list):
    my_list.append('test')
    return my_list
print(append_list(a=[1, 2]))

#Задача

def sum_list(my_list: list):
    return sum(my_list)
print(sum_list([1, 2, 3, 4]))