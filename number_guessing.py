import random

ugaday = random.randint(1, 100)
s = ''
n = 0
while n != ugaday:
    n = int(input('ваше предположение: '))
    if n == ugaday:
        print('Вы угадали, поздравляем!', 'Мое число:', ugaday)
        break
    if n < ugaday:
        print('Слишком мало, попробуйте еще раз')
    if n > ugaday:
        print('Слишком много, попробуйте еще раз')
