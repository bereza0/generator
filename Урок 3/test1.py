
class Widget():
    def __init__(self, text, x, y):
        self.text = text
        self.x = x 
        self.y = y

    def print_info(self):
        print(f'Напис: {self.text}')
        print(f'Розташування: {self.x}, {self.y}')


class Button(Widget):
    def __init__(self, text, x, y, bool):
        super().__init__(text, x, y)
        self.bool = bool

    def click(self):
        if self.bool == False:
            self.bool = True
            print('Ви зареєстровані!')

        else: 
            self.bool = False

button = Button('Брати участь', 100, 100, False)
button.print_info()

da = input('Хочете зареєструватися? (так / ні):').lower()

if da == 'так':
    button.click()

else:
    print('А шкода!')




