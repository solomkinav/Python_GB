# 4. Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать итоговый
# массив чисел, соответствующих требованию. Элементы вывести в порядке их следования в исходном списке.
# Для выполнения задания обязательно использовать генератор.
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]

# формирование исходного списка
num = int(input('Введите необходимое количество элементов списка: '))
initial_list = [int(input(f'Введите {i + 1} элемент списка: ')) for i in range(num)]

# формирование результирующего списка
result_list = [i for i in initial_list if initial_list.count(i) == 1]

# вывод на экран обоих списков
print(initial_list)
print(result_list)