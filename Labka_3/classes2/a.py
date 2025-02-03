# Определяем класс
class StringProcessor:
    # Метод для получения строки от пользователя
    def getString(self):
        self.text = input("Введите строку: ")  # Сохраняем строку в атрибут text

    # Метод для вывода строки в верхнем регистре
    def printString(self):
        print(self.text.upper())  # Выводим строку в верхнем регистре

# Создание объекта класса
sp = StringProcessor()

# Вызов методов
sp.getString()    # Пользователь вводит строку
sp.printString()  # Вывод этой строки в верхнем регистре
