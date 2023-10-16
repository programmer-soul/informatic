import re

def solve(string):
    """ Возвращает количество смайликов вида ;-{| в строке
    408215 % 6 = 5 => Глаза: :
    408215 % 4 = 3 => Нос: -{
    408215 % 7 = 3 => Рот: |
    """
    pattern = r':-{\|'
    return len(re.findall(pattern, string))

res = int(input('Показать тесты или нет? 0 - нет, 1 - да: '))
if res == 1:
    print('Test № 1')
    data = 'Hello :-{| ;<0 ; <) ;<here)'
    result = 1
    print(solve(data), '\n')

    print('Test № 2')
    data = ':-{|'
    result = 1
    print(solve(data), '\n')

    print('Test № 3')
    data = ':-{|:-{|:-{|:-{|'
    result = 4
    print(solve(data), '\n')

    print('Test № 4')
    data = '[]:-{| hi ;;:-{|))      :-{|-:-{|-:-{|-<)'
    result = 5
    print(solve(data), '\n')

    print('Test № 5')
    data = 'nobody here'
    result = 0
    print(solve(data), '\n')
else:
    print('Заходи в следующий раз!')