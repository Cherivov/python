a = int(input('Введите день недели: '))
if 0 < a and a < 6:
    print('не выходной')
elif 5 < a and a < 8:
    print('выходной')
else:
    print('Я вас не понимаю')