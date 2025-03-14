#Задача

from task_9_checks import Checks

class Input(Checks):

    def __init__(self, loc, text):
       super().__init__(loc)
       self.text = text

search = Input('Input#search', 'Поиск')

print(search.loc + ' ' + search.text)
print(search.check_text())

class Button(Checks):

    def __init__(self, loc, text):
        super().__init__(loc)
        self.text = text

search_2 = Button('Button#search', 'Поиск_Кнопка')

print(search_2.loc + ' ' + search_2.text)
print(search_2.check_text())

class Title(Checks):

    def __init__(self, loc, text):
        super().__init__(loc)
        self.text = text

search_3 = Title('Title#search', 'Поиск_Заголовок')

print(search_3.loc + ' ' + search_3.text)
print(search_3.check_text())

class Link(Checks):

    def __init__(self, loc, text):
        super().__init__(loc)
        self.text = text

search_4 = Link('Link#search', 'Поиск_Cсылка')

print(search_4.loc + ' ' + search_4.text)
print(search_4.check_text())