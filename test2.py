

class Title():
    def __init__(self, x, y, text):
        self.text = text
        self.x = x
        self.y = y
        self.bool = True

    def hide(self):
        self.bool = False
        print(f'{self.text} - приховано')

    def print_info(self):
        print(f'Кнопка: {self.text}')
        print(f'Розташування: ({self.x}, {self.y})')
        print(f'Видимість: {self.bool}')


b1 = Title(150, 50, 'Дізнатися переможця прямо зараз!')
b2 = Title(150, -100, 'Переможець може бути тільки один')
b1.print_info()
b2.print_info()
b2.hide()     