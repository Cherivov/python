# Задайте список из n чисел последовательности (1+1/n)n и выведите на экран их сумму
n=int(input())
d={a: round((1+1/a)**a, 2) for a in range(1, n+1)}
sum=0
for i in range (1, n+1):
    sum=sum+d[i]
print(sum)