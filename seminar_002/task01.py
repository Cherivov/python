# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
n = input('Введите число: ')
summa = 0

for i in str(n):
    if i != '.':
        summa += int(i)
print(f'Сумма цифр числа: {n}, равна: {summa}')