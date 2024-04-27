import time
import sys
import random


def parser() -> list[str]:  # читаем данные из файла
    try:
        with open('data.txt', 'r') as new_data:
            new_data = new_data.readlines()
    except Exception as ex:
        print(ex)
    return new_data


def change_data() -> list[str]:  # функция изменения данных в файле на
    with open('expressions_list.txt', 'r') as expressions:  # рандомное выражение из файла expressions_list.txt
        expressions = expressions.readlines()
    random_index = random.randint(0, len(expressions)-1)
    expression = []
    expression.append(expressions[random_index])
    try:
        with open('data.txt', 'w') as data:
            data.writelines(expression)
    except Exception as ex:
        print(ex)
    return expression


def main():
    new_data = None
    var_timer = 0
    var_expression = None
    while True:
        start = time.time()
        time.sleep(1)
        var_timer += int(time.time() - start)
        sys.stdout.write('\rИгрок не менял данные {} сек.'.format(var_timer))
        if parser() != new_data and parser() != []:  # если данные изменились, то обнуляем счетчик
            new_data = parser()
        elif var_timer == 10:  # через 10 сек. проверка если данные изменили не мы, то меняем на свои данные
            if parser() != var_expression:
                var_expression = change_data()  # если данные другие, то меняем на свои данные
                print('\nКомрьютер изменил данные на выражение из списка.')
            else:
                continue   # если наши данные, то ждем дальше
        elif var_timer == 15:  # если счетчик 15 сек., то выиграли
            break  # выходим из программы
    print('\nComputer win!')


if __name__ == '__main__':
    main()
