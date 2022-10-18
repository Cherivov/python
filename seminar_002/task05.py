import random
N = int(input('Введите количество элементов: '))
numbers = []
for i in range(1, N+1):
    numbers.append(random.randint(-N, N+1))
print(numbers)
M = int(input('Введите количество перемешиваний: '))
for i in range(M):
    j = random.randint(0, len(numbers))
    k = random.randint(0, len(numbers))
    temp = numbers[j]
    numbers[j] = numbers[k]
    numbers[k] = temp
print(numbers)