import random


def is_valid(choice, gr):
    if choice.isdigit() and 1 <= int(choice) <= gr:
        return True
    else:
        return False


def is_valid_str(choice):
    if choice == 'да' or choice == 'нет':
        return True
    else:
        return False


def ran(gr):
    return random.randint(1, gr)


print('Добро пожаловать в числовую угадайку')
s = ''
n = 0
f = True
while f:
    count_p = 0
    num = input('введите верхнюю границу: ')
    if num.isdigit():
        num = int(num)
        ugaday = ran(num)
        print('Загадываю число от 1 до', num)
    else:
        print('пока я так не умею, может попробуете ввести число?) ')
        continue
    print()
    while n != ugaday:
        n = input('ваше предположение: ')
        if is_valid(n, num):
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
        question = input('Хотите сыграть еще? (да/нет): ')
        if is_valid_str(question):
            if question == 'да':
                ugaday = random.randint(1, 100)
                print()
                print('хмм, хорошо, я загадал новое число')
                break
            else:
                f = False
                break
        else:
            print('Может все-таки стоило написать "да" или "нет"? Попробуем еще раз...')
        print()

print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
