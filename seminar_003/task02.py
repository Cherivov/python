# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
import random
N = int(input('Введите количество элементов: '))
numbers = []
for i in range(1, N+1):
    numbers.append(random.randint(1, 10))
print(numbers)
prod=[]
j=-1
i=0
while i<=(len(numbers)-1)/2:
    prod.append((numbers[i]*numbers[j]))
    j-=1
    i+=1
print(prod)