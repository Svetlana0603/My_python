# ***** комментарии *****

# Ctrl = / - открытие односточного комментария

""" qwerty
многострочный 
комментарий
qwerty
"""

a = 10
b = 20


# ***** встоенные функции ввода и вывода *****

# вызов функции печати в терминал (print)

# print("Привет, мир")

# PEP8

#  вызов функции из терминала (input)
# print(input("Введите что-то: "))


# ***** переменные *****

my_var = 100
myVar = 200

# операция сложения
r = my_var + myVar

# print(r)



# ****** типы данных *****
# простые типы

int_num = 1000 # целое число (integer)

float_num = 3.14 # числа с плавающей точкой (вещественные числа) (float)

my_str = "Привет, мир!" # строки (строковые значения) (string)

boolean = True # False - булевы значения (boolean, bool)


# print(int_num * 2)

# print(int_num * float_num)

result = my_str * 3 # умножение строк

result = my_str + " " + "Python" # конкатенация

# print(result)

# Способ форматирования строк f-string (f-строка) *****

name = "John"
age = 25

s = f"My name is {name}. Age: {age}."

# print(s)

# ****** Арифметические операции *****

x = 10
y = 3

res_1 = x + y

res_2 = x * y

res_3 = x / y

res_4 = x // y # целочисленное деление

res_5 = x % y # деление по остатку

res_6 = x ** y # возведение в степень

import math # импортирование модуля

res_7 = math.sqrt(100) # извлечение квадратного корня 

# print(res_7)


# ****** Логические операции *****

x = 2
y = 5

res_1 = x != y # оператор "не равно" 

res_2 = x == y # оператор "равно"

res_3 = x > y # оператор "больше"

res_4 = x < y # оператор "меньше"

res_5 = x >= y # оператор "больше или равно"

print(res_5)