#  Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.
import random
N = int(input('Введите количество элементов: '))
numbers = []
for i in range(1, N+1):
    numbers.append(random.randint(-N, N+1))
print(numbers)

f = open('file.txt', 'w')
while True:
    s = input(
        f'Укажите позицию для вычисления от 0 до {N-1}, для прекращения ввода позиций, отправьте пустое значение ')
    if s == "":
        break
    elif int(s) > N-1:
        print('Введена некоректная позиция')
    else:
        f.write(s+"\n")
f.close()

f = open('file.txt', 'r')
prod = 1
for line in f:
    prod = prod*numbers[int(line)]
print(prod)
