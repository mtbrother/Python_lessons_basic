
__author__ = 'Лаптев Сергей Федорович'

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.

x = list(input("Введите целое число: "))
maxValue = " "
for i in x:
    if maxValue > i:
        continue
    else:
        maxValue = i
print("Максимальная цифра введенного числа:", maxValue)

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.

a = int(input("Введите значение а: "))
b = int(input("Введите значение b: "))
a,b = b,a
print("a =", a)
print("b =", b)

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4

import math
while True:
    a = float(input("Введите коэффициет а: "))
    b = float(input("Введите коэффициет b: "))
    c = float(input("Введите коэффициет с: "))
    d = b**2 - 4 * a * c #вычисляем дискриминант
    if d > 0:
        x_1 = (- b + math.sqrt(d)) / (2 * a)
        x_2 = (- b - math.sqrt(d)) / (2 * a)
        print("x_1 =","%.2f" % x_1)
        print("x_2 =","%.2f" % x_2)
        break
    elif d == 0:
        x = (-b) / (2 * a)
        print("Так как дискриминант равен нулю, \nто уравнение имеет один действительный корень: \nХ =", x)
        break
    else:
        print("Дискриминант меньше нуля, \nуравнение не имеет действительных решений, \nвведите другие значения.")
