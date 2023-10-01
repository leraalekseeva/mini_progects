import random


def is_valid(num):
    if num.isdigit() and 1 < int(num) < 100:
        return True
    else:
        return False


def is_valid_str(num):
    if num == 'да' or num == 'нет':
        return True
    else:
        return False


ugaday = random.randint(1, 100)
print('Добро пожаловать в числовую угадайку')
s = ''
n = 0
count_p = 0
f=True
while f==True:
    while n != ugaday:
        n = input('ваше предположение: ')
        if is_valid(n):
            n = int(n)
            count_p += 1
            if n == ugaday:
                print('Вы угадали, поздравляем!', 'Мое число:', ugaday)
                print(f'Вам понадобилось {count_p} попыток')
                break
            if n < ugaday:
                print('Слишком мало, попробуйте еще раз')
            if n > ugaday:
                print('Слишком много, попробуйте еще раз')
        else:
            print('А может быть все-таки введем целое число от 1 до 100?')
            continue

    while True:
        qustion = input('Хотите сыграть еще? (да/нет): ')
        if is_valid_str(qustion):
            if qustion == 'да':
                ugaday = random.randint(1, 100)
                print()
                print('хмм, хорошо, я загадал новое число')
                break
            else:
                f = False
                break
        else:
            print('Может все-таки стоило написать "да" или "нет"? Попробуем еще раз...')

print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
