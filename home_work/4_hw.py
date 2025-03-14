# #Задача №1
#
# class Rectangle:
#
#     def __init__(self, width, height):
#         self.widht = width
#         self.height = height
#
#     def S(self):
#         return self.widht * self.height // 2
#
#     def P(self):
#         return 2 * (self.widht + self.height)
#
# rectangle_1 = Rectangle(5, 4)
# rectangle_2 = Rectangle(10, 13)
# rectangle_3 = Rectangle(135, 437)
#
# print('Площадь прямоугольника №1 ', rectangle_1.S())
# print('Периметр прямоугольника №1 ', rectangle_1.P())
#
# print('Площадь прямоугольника №2 ', rectangle_2.S())
# print('Периметр прямоугольника №2 ', rectangle_2.P())
#
# print('Площадь прямоугольника №3 ', rectangle_3.S())
# print('Периметр прямоугольника №3 ', rectangle_3.P())
#
# #Задача №2
#
# class Math:
#
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def addition(self):
#         return self.a + self.b
#
#     def multiplication(self):
#         return self.a * self.b
#
#     def division(self):
#         return self.a // self.b
#
#     def subtraction(self):
#         return self.a - self.b
#
# addition = Math(5, 7)
# multiplication = Math(6, 8)
# division = Math(4, 2)
# subtraction = Math(15, 6)
#
# print(str(addition.a) + ' + ' + str(addition.b) + ' = ' + str(addition.addition()))
# print(str(multiplication.a) + ' * ' + str(multiplication.b) + ' = ' + str(multiplication.multiplication()))
# print(str(division.a) + ' / ' + str(division.b) + ' = ' + str(division.division()))
# print(str(subtraction.a) + ' - ' + str(subtraction.b) + ' = ' + str(subtraction.subtraction()))
#
# #Задача №3
#
# class Object:
#
#     def __init__(self, text):
#         self.text = text
#         self.type = 'Кнопка'
#         self.loc = ' '
#
#     def click(self):
#         return f"Клик по кнопке {self.text}"
#
# Text_Box = Object('Text Box')
# Check_Box = Object('Check Box')
# Radio_Button = Object('Radio Button')
# Web_Tables = Object('Web Tables')
# Buttons = Object('Buttons')
# Links = Object('Links')
# Broken_Links_Images = Object('Broken Links - Images')
# Upload_and_Download = Object('Upload and Download')
# Dynamic_Properties = Object('Dynamic Properties')
#
# Button_list = [Text_Box, Check_Box, Radio_Button,
#                Web_Tables, Buttons, Links, Broken_Links_Images,
#                Upload_and_Download, Dynamic_Properties]
#
# for elem in Button_list:
#     print(elem.text)
#
# for elem in Button_list:
#     print(elem.click())

#Задача №4

class Car:

    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def start(self):
        print('Автомобиль заведен')

    def stop(self):
        print('Автомобиль заглушен')

    def assigned_1(self):
        print('Присвоен год выпуска ' + self.year)

    def assigned_2(self):
        print('Присвоен тип' + self.type)

    def assigned_3(self):
        print('Присвоен цвет ' + self.color)

car = Car('black', ' sedan ', '2013')

car.start()
car.stop()
car.assigned_1()
car.assigned_2()
car.assigned_3()
