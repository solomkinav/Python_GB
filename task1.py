# 1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя
# несколько чисел и строк и сохраните в переменные, выведите на экран.

# Создание нескольких переменных
str_var = "first var"
int_var = 461
float_var = 7.49
list_var = [1, 3, 'book']
dict_var = {1: 'А', 2: 'Б', 3: 'В'}

# вывод созданных переменных на экран
print(str_var)
print(int_var)
print(float_var)
print(list_var)
print(dict_var)

# запрос у пользователя нескольких чисел:
num_1 = int(input('Введите целое число: '))
num_2 = int(input('Введите целое число: '))
num_3 = int(input('Введите целое число: '))

# запрос у пользователя нескольких строк:
str_1 = input('Введите строку: ')
str_2 = input('Введите строку: ')
str_3 = input('Введите строку: ')

# вывод сохраненных данных:
print("Вы ввели числа:", num_1, num_2, num_3)
print("Вы ввели строки:", str_1, str_2, str_3)
