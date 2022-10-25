lst = list(map(int, input("Введите числа через пробел:\n").split()))
print(f"Исходный список: {lst}")
new_lst = []
for i in lst:
    if i not in new_lst:
        new_lst.append(i)
print(f"Список из неповторяющихся элементов: {new_lst}")