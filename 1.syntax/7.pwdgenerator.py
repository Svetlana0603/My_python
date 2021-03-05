# *** Генератор паролей ***

import hashlib
from tkinter import Tk, StringVar, Label, Entry, Button

def hashing():
    """
    Функция шифрования (хеширование)
    """
    # строка пароли
    origin_str = pwd.get() #"password"
    # кодирование в байт-строку
    byte_str = origin_str.encode()
    # хеширование
    hash_str = hashlib.sha256(byte_str)
    # преобразование хеш-строки в обычную строку
    hex_str = hash_str.hexdigest()[:10]
    # print(hex_str)

    pwd_hash.set(hex_str)
# тестирование функции хеширования
# hashing()

# объект окна
window = Tk()
# заголовок окна
window.title("Password generator v.0.1")

# переменные с объектами класса StringVar
pwd = StringVar()
pwd_hash = StringVar()

# текстовая метка, созданная виджетом Label
Label(text="Пароль:").grid(row=0, column=0, padx=5, pady=5)

# поле ввода, созданная виджетом Entry
Entry(textvariable=pwd).grid(row=0, column=1, padx=5, pady=5)

# кнопка, созданная виджетом Button
Button(text="Кликни", command=hashing).grid(row=1, column=0, padx=5, pady=5)

# вывод, созданная виджетом Entry
Entry(textvariable=pwd_hash).grid(row=1, column=1, padx=5, pady=5)

# запуск программы (точка входа программы)
window.mainloop()