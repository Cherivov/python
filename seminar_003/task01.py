# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
import random
N = int(input('Введите количество элементов: '))
numbers = []
for i in range(1, N+1):
    numbers.append(random.randint(1, 10))
print(numbers)
sum = 0
for i in range(1, len(numbers), 2):
    sum = sum+numbers[i]
print(f'Сумма элементов списка, стоящих на нечётной позиции равна: {sum}')
