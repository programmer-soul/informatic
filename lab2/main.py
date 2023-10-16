def check_correct_input(code):
    if ((set(code) - {'1','0'}) == 1) or (len(code) != 7):
        print('Введённая строка должна состоять из 7 цифр "0" и "1". Вы ошиблись, исправьте ошибку и повторите ввод.')
        exit(1)

def check_step(sym):
    p1 = (sym[0] + sym[2] + sym[4] + sym[6]) % 2
    p2 = (sym[1] + sym[2] + sym[5] + sym[6]) % 2
    p3 = (sym[3] + sym[4] + sym[5] + sym[6]) % 2
    return (p1,p2,p3)

def incorrect_index(sym):
    return int(''.join(map(str, check_step(sym)[::-1])), 2)

def incorrect_symbol(sym):
    return {1: 'r1', 2: 'r2', 3: 'i1', 4: 'r3', 5: 'i2', 6: 'i3', 7: 'i4'}[incorrect_index(sym)]

def fixed_message(sym):
    if ((check_step(sym) != (0, 0, 0)) == 0) or (incorrect_symbol(sym)[0] == 'r'):
        return ''.join(map(str,[sym[2], sym[4], sym[5], sym[6]]))
    point = int(incorrect_symbol(sym)[1]) - 1
    result = [sym[2], sym[4], sym[5], sym[6]]
    result[point] = (result[point] + 1) % 2
    return ''.join(map(str, result))

code = input('Введите ваше число вместе с проверочными битами: ')
check_correct_input(code)

if incorrect_index(list(map(int, list(code)))):
    print(f'> Сообщение передано неверно!\nОшибка в символе {incorrect_symbol(list(map(int, list(code))))}')
else:
    print('> Сообщение передано верно!')

print(f'Верный вариант: {fixed_message(list(map(int, list(code))))}')
