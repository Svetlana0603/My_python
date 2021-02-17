# *** Циклы (операторы циклов) ***

# Оператор цикла while

# Бесконечный цикл (прерывается спомощью сочетания Ctrl+C)
# while True:
#     print("Hi")


# Бесконечный цикл while с прерыванием
# while True:
#     _in_data = input("Введите что-нибудь: ")
#     if _in_data == "stop":
#         print("Buy buy!")
#         break
#     print("Hi")

# Цикл с условием

number = 0

# while number < 10:
#     print(f"Number: {number}")
#     # number = number + 1 # инкремент
#     number += 1 # инкремент

number_2 = 10

# while number_2 > 0:
#     print(f"Number: {number_2}")
#     number_2 -= 1 # декремент

# Цикл с условием и с прерыванием

number_3 = 0
treshold = 7

# while number_3 < 15:
#     print(f"Num: {number_3}")
#     if number_3 == treshold:
#         print("Loop terminated")
#         break
#     number_3 += 1


# *** Оператор цикла for

# 1. Читает значение элемента итерируемого объекта по порядку
# 2. присваивает это значение в свою переменную
# 3. выполняет блок кода своего тела

# for item in [10,20,30,40,50]:
#     print(item)

my_str = "Hello!"

# for char in my_str:
#     print(char)

my_list = [10, 20, 30, 40, 50]
my_list_2 = []

# for i in my_list:
#     # i += 2
#     res = i ** 2
#     my_list_2.append(res)

# for i in my_list[1:4]:
#     # i += 2
#     res = i ** 2
#     my_list_2.append(res)

# for i in range(0, 20):
#     print(i)

# for i in range(20):
#     print(i)

# for с безымянной переменной (_)
# for _ in range(5):
#     print("Hi")

# for val in range(10, 100, 10):
#     if val == 50:
#         break
#     print(val)


# *** Генератор списка ***

# создание списка с числами в диапазоне от 0 до 9
# my_list = [num for num in range(9)]

# создание списка с числами в диапазоне от 10 до 90 с шагом 10
my_list = [num for num in range(10, 100, 10)]

#  то же самое но в обратоном порядке
my_list = [num for num in range(10, 100, 10)[::-1]]

my_list = [num for num in range(10, 100, 10)]
my_list.reverse()

# print(my_list)