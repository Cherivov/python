a = int(input('Введите день: '))
b = int(input('Введите месяц: '))
if (a>0 and a<8) and (b>0 and b<13):
    if a == 1 and b == 1:
        print('Новый год')
    elif a ==2 and b==2:
        print('День Защитника отечества')
    elif a ==1 and b==3:
        print('Международный женский день')
    elif a==2 and b==5:
        print('День победы')
    else:
        if 0 < a and a < 6:
            print('не выходной')
        elif 5 < a and a < 8:
            print('выходной')
else:
    print('Я вас не понимаю')