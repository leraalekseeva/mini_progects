import random


def is_valid_str(choice):
    if choice == 'да' or choice == 'нет':
        return True
    else:
        return False


def generate_password(spisok, length):
    password = random.sample(spisok, length)
    return password


DIGITS = '0123456789'
LOWERCASE_LETTERS = 'abcdefgihjklmnopqrstuvwxyz'
UPPERCASE_LETTERS = 'ABCDEFGIHJKLMNOPQRSTUVWXYZ'
PUNCTUATION = '!#$%&*+-=?@^_'
AMBIVALENT_SIMBOLS = 'il1Lo0O'

chars = ''
s = ''

while True:
    while True:
        count_pass = input('Введите количество паролей для генерации: ')
        if count_pass.isdigit():
            count_pass = int(count_pass)
            break
        else:
            print('пока я так не умею, может попробуете ввести число?) ')
            continue
    while True:
        len_pass = input('Введите длину одного пароля: ')
        if len_pass.isdigit():
            len_pass = int(len_pass)
            break
        else:
            print('пока я так не умею, может попробуете ввести число?) ')
            continue
    while True:
        ans_dig = input('Включать ли цифры? (да/нет):')
        if is_valid_str(ans_dig):
            if ans_dig == 'да':
                ans_dig = True
                break
            else:
                ans_dig = False
                break
        else:
            print('Может все-таки стоило написать "да" или "нет"? Попробуем еще раз...')
    while True:
        ans_up_letters = input('Включать ли прописные(заглавные) буквы? (да/нет):')
        if is_valid_str(ans_up_letters):
            if ans_up_letters == 'да':
                ans_up_letters = True
                break
            else:
                ans_up_letters = False
                break
        else:
            print('Может все-таки стоило написать "да" или "нет"? Попробуем еще раз...')
    while True:
        ans_low_letters = input('Включать ли строчные буквы? (да/нет):')
        if is_valid_str(ans_low_letters):
            if ans_low_letters == 'да':
                ans_low_letters = True
                break
            else:
                ans_low_letters = False
                break
        else:
            print('Может все-таки стоило написать "да" или "нет"? Попробуем еще раз...')
    while True:
        ans_punctuation = input('Включать ли символы "!#$%&*+-=?@^_" ? (да/нет):')
        if is_valid_str(ans_punctuation):
            if ans_punctuation == 'да':
                ans_punctuation = True
                break
            else:
                ans_punctuation = False
                break
        else:
            print('Может все-таки стоило написать "да" или "нет"? Попробуем еще раз...')
    while True:
        ans_amb_sim = input('Исключать ли неоднозначные символы "il1Lo0O" (да/нет):')
        if is_valid_str(ans_amb_sim):
            if ans_amb_sim == 'да':
                ans_amb_sim = True
                break
            else:
                ans_amb_sim = False
                break
        else:
            print('Может все-таки стоило написать "да" или "нет"? Попробуем еще раз...')
    break

if ans_dig:
    s += DIGITS
if ans_up_letters:
    s += UPPERCASE_LETTERS
if ans_low_letters:
    s += LOWERCASE_LETTERS
if ans_punctuation:
    s += PUNCTUATION
if ans_amb_sim:
    for c in AMBIVALENT_SIMBOLS:
        s = s.replace(c, '')
print()

for i in range(count_pass):
    chars = generate_password(s, len_pass)
    chars = ''.join(chars)
    print(f'Пароль №{i+1}:', chars)
