# *** Основы объектно-ориентированного программирования (ООП) ***

# Объект обладает свойствами и методами (функции)
# Каждый объект должен принадлежать определенному классу.
# Класс - это некий "чертеж" объектов.
# Объект определенного класса называется экземпляром класса.

# Создание класса. Название класса принято писать с заглавной буквы.
class Cat:
    def __init__(self):
        # метод-конструктор

        # свойства (атрибуты, поля) - спец.переменная
        self.name = None

    def mur(self):
        # метод
        return f"Mur-mur! My name is {self.name}"

# создание экземпляра (объекта) класса Cat
cat_1 = Cat()
cat_2 = Cat()

# работа с свойствами (атрибутами)

# присвоение значения атрибуту
cat_1.name = "Barsik"
cat_2.name = "Murka"

# чтение значения атрибута name
# print(cat_1.name)
# print(cat_2.name)

# Работа с методом

# Вызов метода
# print(cat_1.mur())
# print(cat_2.mur())

# ***  Принцип Наследование ***

# создаем родительский (предковый) класс
class Animal:
    def __init__(self, num_legs):
        self.num_legs = num_legs

# создание дочерних классов
class Insect(Animal):
    def __init__(self, num_legs):
        super().__init__(num_legs)

    def info(self):
        print(f"I am Insect. Legs: {self.num_legs}")

class Mammal(Animal):
    def __init__(self, num_legs):
        super().__init__(num_legs)

    def info(self):
        print(f"I am Mammal. Legs: {self.num_legs}")

# экземпляр класса Insect
# bug = Insect(6)
# bug.info()

# экземпляр класса Mammal
cat = Mammal(4)
# cat.info()

class Human(Mammal):
    def __init__(self, num_legs, name):
        super().__init__(num_legs)
        self.name = name

    def hello(self):
        print(f"My name is {self.name}")

person_1 = Human(2, "John")

# print(person_1.num_legs)
# person_1.info()
# person_1.hello

# *** Принцип Полиморфизма ***

# поли + морф - разные формы чего-то

# дочерний класс переопределяет метод родительского класса
# родительский класс
class A:
    def func(self, arg):
        res = arg + 2
        print(f"Result: {res}")

# дочерний класс
class B(A):
    def func(self, a, b):
        res = a ** b
        print(f"Result: {res}")

# экземпляры классов
a = A()
b = B()

# a.func(10)
# b.func(2, 8)

# применение методов перегрузки операторов ("магических" методов)

class MyClass:
    def __init__(self, param):
        self.param = param
# метод для возврата строки
    def __str__(self):
        return f"My param = {self.param}"

    # метод позволяющий вызывать экземпляры класса
    def __call__(self):
        res = self.param * 10
        print(res)

x = MyClass(100)

# передаем объект как строку
# print(x)

# вызов объекта как функцию
# x()

# *** Принцип Инкапсуляции ***

# инкапсуляция - это сокрытие доступа к свойствам и методам

# не строгая инкапсуляция
class C:
    def __init__(self):
        # не строго инкапсулированное свойство
        self._attr = 100
    
    # не строго инкапсулированное свойство
    def _met(self):
        print("Hello!:)")

c_1 = C()

# print(c_1._attr)
# c_1._met()

# строгая инкапсуляция
class D:
    def __init__(self):
        # строго инкапсулированное свойство
        self.__attr = 100
    
    # строго инкапсулированное свойство
    def __met(self):
        print("Hello!:)")

    def public_met(self):
        return self.__attr

d_1 = D()

# попытка доступа к инкапсулированным атрибуту и методу
# print(d_1.__attr)
# d_1.__met()

#  обход инкапсуляции
# print(d_1._D__attr)
# d_1._D__met()

# доступ к значению инкапсулированного атрибута через публичный метод
# print(d_1.public_met())

# *** принцип композиции (агрегации) ***

class E:
    def __call__(self, a):
        return a ** 3

class F:
    def met(self, b):
        # создается объект класса E
        e = E()
        res = e(b) + b
        print(res)

f = F()

f.met(5)