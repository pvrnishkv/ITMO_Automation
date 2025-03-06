a: int = 5
b: str = 'строка'
c: list = [1, 2]

def indent(s: str, widht: int) -> str:
    return " " * (max(0, widht - len(s)))  + s

print(indent('123', 123))

#Задача

def string_lenght(s: str = '') -> int:
    return len(s)
print(string_lenght(s='    '))

#Задача

def max_list(a: list, b: list) -> int:
    return max(len(a), len(b))
print(max_list([1, 2, 3, 4], [5,6]))