num_float = 3.4

# num_float = 0 или num_float = -4.5

if num_float > 0:
    print('Положительное число')
elif num_float == 0:
    print('Ноль')
else:
    print('Отрицательное число')

permit_print = True
num = 9

if num > 0 and permit_print:
    print('num - положительное число')
elif not permit_print:
    print('Печать запрещена')

#Задача

def student_rang(year_of_study):
    if year_of_study == 1 or year_of_study == 2 or year_of_study == 3 or year_of_study == 4:
        print('Бакалавр')
    elif year_of_study in range (5,7):
        print('Магистр')
    elif 7<= year_of_study <= 9:
        print('Аспирант')
    else:
        print('Введите корректный год обучения')

student_rang(10)

#Задача

num = 5

if num > 100 or num < -100:
    print('-')
else:
    print('+')