# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
import math
ax = int(input('Введите координату X точки A: '))
ay = int(input('Введите координату Y точки A: '))
bx = int(input('Введите координату X точки B: '))
by = int(input('Введите координату Y точки B: '))
distance_AB = round(abs(math.sqrt(pow(bx-ax, 2)+pow(by-ay, 2))), 2)
print(distance_AB)
