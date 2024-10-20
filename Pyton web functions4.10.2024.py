# синтаксис функции
# def имя_функции(аргументы):
#     инструкции
#     return список_выражений None
# имя_функции()



# def greet(name):
#     print('Привет ' + name + '. Доброе утро!')
# greet('Джон')


# возвращаемое значение - return

# def absolute_value(num):
#     if num >= 0:
#         return num
#     else:
#         return -num
# print(absolute_value(2))
# print(absolute_value(-4))


# область видимости (scope) и время жизни переменной

# def my_func():
#     x = 10
#     print('значение внутри функции', x)
# x = 20
# my_func()
# print('значение вне функции', x)


# аргументы фунуции
# фиксированное колличество аргументов

# def greet(name, age):
#     print('Привет ' + name + '. Доброе утро!' + ' мне ' + age + ' лет')
# greet('Джон', '23')

# аргументы по умолчанию

# def greet(name, age = '23'):
#     print('Привет ' + name + '. Доброе утро!' + ' мне ' + age + ' лет')
# greet('Джон')

# именованный аргумент

# def greet(name, age):
#      print('Привет ' + name + '. Доброе утро!' + ' мне ' + age + ' лет')
# greet(name= 'Джон', age='23')
# greet(name= 'Иван', age='54')


# произвольный список аргументов
# *

# def greet(*names):
#     for name in names
#         print('hello', name)
# greet('kate', 'john', 'boris')

# def adder(*nums)
#     sum = 0
#     for n in nums:
#         sum += n
#     print('sum = ', sum)
# adder(3,5,6,7,8)


# x = 'глобальная переменная'
# def foo():
#     x = x * 2
#     print(x)
#     # print('x внутри функции', x)
# foo()
# # print('x вне функции', x)

# локальные переменные

# def foo():
#     y = 'локальная переменная'
#     print(y)
# foo()

# x = 'global variable'
# def foo():
#     global x
#     y = 'local variable'
#     x = x * 2
#     print(x)
#     print(y)
# foo()

# x = 5
# def foo():
#     x = 10
#     print('local variable :', x)
# foo()
# print('global variable x:', x)


# нелокальные переменные nonlocal

# def outer():
#     x = 'локальныая переменная'
#     def inner():
#         nonlocal x
#         x = 'нелокальная переменная'
#         print('вложенная функция:', x)
#     inner()
#     print(':', x)
# outer()

# def say():
#     greeting = 'привет'
#     def display():
#         print(greeting)
#     display()
# say()

# вернуть функцию из функции
# def say():
#     # ЗАМЫКАНИЕ 3 строчки вниз
#     greeting = 'привет'
#     print(hex(id(greeting)))
#     def display():
#         print(hex(id(greeting)))
#         print(greeting)
#     return display
# fn = say()
# fn()

# print(fn.__closure__)

# 1. Функции say()
# 2. замыкание


# # декораторы
# def currency(fn):
#     def wrapper(*args, **kwargs):
#         result = fn(*args, **kwargs)
#         return f'${result}'
#     return wrapper
#
# @currency
# def net_price(price, tax):
#     return price * (1 + tax)
# $ 100

# print(net_price(100, 0.05))

# декоратор синтаксис
# функция = декоратор(функция)

# @декоратор
# def функция():
#   тело функции


# lambda аргументы: выражение

# double = lambda x: x * 2
# print(double(6))

# filter(), map()

# my_list = [2,5,56,7,8,9,6]
# new_list =  list(map(lambda x: x * 2, my_list))
# print(new_list)
