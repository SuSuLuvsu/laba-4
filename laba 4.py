def lab41():
    try:
        a = int(input('Введите число, чтобы проверить деление на 3: '))
        b = a % 3
    except ValueError:
        print('Введено не число!')
    else:
        if b == 0 and a != 0:
            print('Число', a, 'делится на 3')
        elif a == 0:
            print('Введен ноль!')
        else:
            print('Число', a, 'не делится на 3')


def lab42():
    try:
        a = int(input('Введите число:'))
        b = 100 / a
    except ZeroDivisionError:
        print('Введен ноль!')
    except ValueError:
        print('Введено не число!')
    else:
        print('Результат деления 100 на введенное число: ', b)


def lab43():
    date = input('Введите дату в формате дд.мм.гг: ')
    date = date.split(('.'))
    if int(date[0]) * int(date[1]) == int(date[2][2:4]):
        print('Дата магическая!')
    else:
        print('Дата не магическая!((((')

def lab44():
    s = input('')
    if len(s) % 2 == 0:
        res1 = 0
        res2 = 0
        for i in range(len(s) // 2):
            res1 += int(s[i])
            res2 += int(s[len(s) // 2 + i])
        if res1 == res2:
            print(res1, res2, 'билет счастливый')
        else:
            print(res1, res2, 'билет не счастливый')
    else:
        print('введите четное количество символов')