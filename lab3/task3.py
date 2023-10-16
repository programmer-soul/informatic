import re


def solve(string):
    """ 408215 % 5 = 0 =>
    Написать регулярное выражение, которое проверяет корректность email и в качестве
    ответа выдаёт почтовый сервер (почтовый сервер – часть email идущая после «@»).
    Для простоты будем считать, что почтовый адрес может содержать в себе буквы,
    цифры, «.» и «_», а почтовый сервер только буквы и «.». При этом почтовый сервер,
    обязательно должен содержать верхний уровень домена («.ru», «.com», etc.)
    """
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    if len(re.findall(pattern, string)) == 1:
        dog = re.findall(pattern, string)[0].find('@')
        email_client = re.findall(pattern, string)[0][dog+1:]
        return f'Email введен верно! Почтовый сервер: {email_client}'
    return 'Email введен неверно! Исправьте ошибку и повторите ввод!'

res = int(input('Показать тесты или нет? 0 - нет, 1 - да: '))
if res == 1:
    print('Test № 1')
    data = 'admin@icloud.com'
    result = 'Email введен верно! Почтовый сервер: icloud.com'
    print(solve(data), '\n')

    print('Test № 2')
    data = 'admingmail.com'
    result = 'Email введен неверно! Исправьте ошибку и повторите ввод!'
    print(solve(data), '\n')

    print('Test № 3')
    data = 'admi n@yandex.ru'
    result = 'Email введен неверно! Исправьте ошибку и повторите ввод!'
    print(solve(data), '\n')

    print('Test № 4')
    data = 'admin@mailru'
    result = 'Email введен неверно! Исправьте ошибку и повторите ввод!'
    print(solve(data), '\n')

    print('Test № 5')
    data = 'admin@itmo.ru'
    result = 'Email введен верно! Почтовый сервер: itmo.ru'
    print(solve(data), '\n')
else:
    print('Заходи в следующий раз!')
