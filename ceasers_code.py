EN_LOW_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
EN_UP_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
RU_LOW_LETTERS = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
RU_UP_LETTERS = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'


def shifrator(stroka,alpLOW,alpUP,sdvig):
    new_stroka = ''
    for i in range(len(stroka)):
        if stroka[i] in alpLOW:
            num = alpLOW.find(stroka[i])
            new_stroka += alpLOW[(num + sdvig) % len(alpLOW)]
        elif stroka[i] in alpUP:
            num = alpUP.find(stroka[i])
            new_stroka += alpUP[(num + sdvig) % len(alpUP)]
        else:
            new_stroka += stroka[i]
    return new_stroka
    pass


def deshifrator(stroka,alpLOW,alpUP,sdvig):
    new_stroka = ''
    for i in range(len(stroka)):
        if stroka[i] in alpLOW:
            num = alpLOW.find(stroka[i])
            new_stroka += alpLOW[(num - sdvig) % len(alpLOW)]
        elif stroka[i] in alpUP:
            num = alpUP.find(stroka[i])
            new_stroka += alpUP[(num - sdvig) % len(alpUP)]
        else:
            new_stroka += stroka[i]
    return new_stroka
    pass


def is_ru_or_en(choice):
    if choice == 'ru' or choice == 'en':
        return True
    else:
        return False


def is_k_or_d(choice):
    if choice == 'k' or choice == 'd':
        return True
    else:
        return False


print('Добро пожаловать в шифрованный чат с Цезарем!)')
while True:
    k_or_d = input('Вы хотите отправить(кодировать) сообщение или получить(декодировать) \n напишите "k" или "d" '
                   'соответственно: ')
    if is_k_or_d(k_or_d):
        break
    else:
        print('Может все-таки стоило написать "k" или "d"? Попробуем еще раз...')

while True:
    language = input('На каком языке ваше сообщение? ru-русский en-английский: ')
    if is_ru_or_en(language):
        break
    else:
        print('Может все-таки стоило написать "ru" или "en"? Попробуем еще раз...')

while True:
        sdvig = input('Введите сдвиг:')
        if sdvig.isdigit():
            sdvig = int(sdvig)
            break
        else:
            print('пока я так не умею, может попробуете ввести число?) ')
            continue

str = input('Введите строку:')

if k_or_d == 'k':
    if language == 'en':
        print(shifrator(str, EN_LOW_LETTERS, EN_UP_LETTERS, sdvig))
    if language == 'ru':
        print(shifrator(str, RU_LOW_LETTERS, RU_UP_LETTERS, sdvig))
if k_or_d == 'd':
    if language == 'en':
        print(deshifrator(str, EN_LOW_LETTERS, EN_UP_LETTERS, sdvig))
    if language == 'ru':
        print(deshifrator(str, RU_LOW_LETTERS, RU_UP_LETTERS, sdvig))
