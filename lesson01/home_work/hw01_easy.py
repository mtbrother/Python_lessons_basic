
__author__ = 'Лаптев Сергей Федорович'

# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.

# код пишем тут...
num = int(input("Введите число: "))
for i in range(num + 1):
    print(i, end=" ")


# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную 
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

a = int(input("Введите значение а: "))
b = int(input("Введите значение b: "))
tmp = a
a = b
b = tmp
print("a =", a)
print("b =", b)


# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

age = int(input("Укажите ваш возраст: "))
if age >= 18:
    print("Доступ разрешен.")
else:
    print("Извините, пользование данным ресурсом только с 18 лет")
