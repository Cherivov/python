# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
import random, math
N = int(input('Введите количество элементов: '))
numbers = []
for i in range(1, N+1):
    numbers.append(round(random.uniform(1, 10),2))
print(numbers)
max=0
min=1
for i in numbers:
    k=math.modf(i)
    if max<k[0]:
        max=k[0]
    elif min>k[0]:
        min=k[0]
print(round(max-min,2))