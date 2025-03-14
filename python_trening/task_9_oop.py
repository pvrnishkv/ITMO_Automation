# class Button:                       #Ключевое слово создания класса + Имя класса
#
#     type: str = 'Button'
#
#     def __init__(self, text, link): #Метод создания атрибутов + Атрибуты
#         self.text = text            #Аргументы
#         self.link = link
#
# #Создаем экземпляры класса
# home = Button('Домой', '/home')
# catalog_msk = Button('Каталог', '/msk/catalog')
#
# #Получаем доступ к атрибутам
# print(home.text)
# print('Кнопка ' + home.text + ' имеет ссылку ' + home.link)
#
# print('\n')
#
# print(catalog_msk.text)
# print('Кнопка ' + catalog_msk.text + ' имеет ссылку ' + catalog_msk.link)
from re import search
#
#
# class ButtonTwo:
#
#     def __init__(self, text, link, loc):
#         self.text = text
#         self.link = link
#         self.loc = loc
#
#     def click(self):
#         return "Клик по локатору - {}".format(self.loc)
#
# #Создаем экземпляры класса
# home_two = ButtonTwo('Домой', '/home', 'button#home')
#
# #Вызываем метод
# print(home_two.click())

#Задача

class Input:

    def __init__(self, loc, text):
        self.loc = loc
        self.text = text

search = Input('Input#search', 'Поиск')

print(search.loc + ' ' + search.text)

class Button:

    def __init__(self, loc, text):
        self.loc = loc
        self.text = text

search_2 = Button('Button#search', 'Поиск_Кнопка')

print(search_2.loc + ' ' + search_2.text)

class Title:

    def __init__(self, loc, text):
        self.loc = loc
        self.text = text

search_3 = Title('Title#search', 'Поиск_Заголовок')

print(search_3.loc + ' ' + search_3.text)

class Link:

    def __init__(self, loc, text):
        self.loc = loc
        self.text = text

search_4 = Link('Link#search', 'Поиск_Cсылка')

print(search_4.loc + ' ' + search_4.text)

#Задача

class Page:

    def __init__(self, url):
        self.url = url

    def get(self):
        print(self.url)

home = Page('https//')

home.get()

#Задача

class Soda:

    def __init__(self, additive=None):
        self.additive = additive

    def show_my_drink(self):
        if self.additive:
            print(f'Газировка и {self.additive}')

        else:
            print('Обычная газировка')

soda_1 = Soda()
soda_2 = Soda('Лайм')

soda_1.show_my_drink()
soda_2.show_my_drink()


