EN_LOW_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
EN_UP_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


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


print('Добро пожаловать в шифрованный чат с Цезарем!)')
k_or_d = 'k'
language = 'en'
str = input('Введите строку:').split()

new_str = []
for i in range(len(str)):
    count = 0
    for a in str[i]:
        if a in EN_UP_LETTERS or a in EN_LOW_LETTERS:
            count += 1
    new_str.append(shifrator(str[i], EN_LOW_LETTERS, EN_UP_LETTERS, count))

print(*new_str)


