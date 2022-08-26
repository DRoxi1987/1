import datetime


def print_signs(signs: str) -> None:
    """ Выводит на экран ответ в формате: Ваш знак Зодиака: ..."""

    print(f"Ваш знак Зодиака: {signs}.\n")


def sign_finding(birthday_datetime: datetime) -> None:
    """ Сравнивает объект Datetime с интервалами времени, соответствующими
    определенному знаку в цикле for. При найденном интервале, вызывает функцию print_signs."""

    dict_sign = [["Козерог", datetime.date(birthday_datetime.year, 12, 22),
                  datetime.date(birthday_datetime.year, 12, 31)],
                 ["Козерог", datetime.date(birthday_datetime.year, 1, 1),
                  datetime.date(birthday_datetime.year, 1, 19)],
                 ["Водолей", datetime.date(birthday_datetime.year, 1, 20),
                  datetime.date(birthday_datetime.year, 2, 18)],
                 ["Рыбы", datetime.date(birthday_datetime.year, 2, 19),
                  datetime.date(birthday_datetime.year, 3, 20)],
                 ["Овен", datetime.date(birthday_datetime.year, 3, 21),
                  datetime.date(birthday_datetime.year, 4, 19)],
                 ["Телец", datetime.date(birthday_datetime.year, 4, 20),
                  datetime.date(birthday_datetime.year, 5, 20)],
                 ['Близнецы', datetime.date(birthday_datetime.year, 5, 21),
                  datetime.date(birthday_datetime.year, 6, 20)],
                 ["Рак", datetime.date(birthday_datetime.year, 6, 21),
                  datetime.date(birthday_datetime.year, 7, 22)],
                 ["Лев", datetime.date(birthday_datetime.year, 7, 23),
                  datetime.date(birthday_datetime.year, 8, 22)],
                 ["Дева", datetime.date(birthday_datetime.year, 8, 23),
                  datetime.date(birthday_datetime.year, 9, 22)],
                 ["Весы", datetime.date(birthday_datetime.year, 9, 23),
                  datetime.date(birthday_datetime.year, 10, 22)],
                 ["Скорпион", datetime.date(birthday_datetime.year, 10, 23),
                  datetime.date(birthday_datetime.year, 11, 30)],
                 ["Стрелец", datetime.date(birthday_datetime.year, 11, 22),
                  datetime.date(birthday_datetime.year, 12, 21)]]

    for i in range(len(dict_sign)):
        if dict_sign[i][1] <= birthday_datetime <= dict_sign[i][2]:
            print_signs(dict_sign[i][0])


def main() -> None:
    """ Функция запрашивает от пользователя дату рождения в формате "день/месяц/год".
    Проверяет ошибки ввода пользователя. Проверяет, является ли год високосным.

    Если проверка не прошла, выдает строку: "Введите верную дату" и заново запрашивает дату рождения.

    После проверок переводит строку в объект Datetime и передает функции sign_finding,
    которая ищет знак Зодиака по полученному объекту. Далее мы получаем на выходе строку:
    "Ваш знак зодиака: 'Найденное соответствие'.".

    После этого, программа спрашивает: "Выйти из программы y/n?".

    По нажатию клавиши n, опять запрашивает дату рождения от пользователя, либо, по нажатию y,
    завершает свою работу"""

    print("Введите дату рождения: день/месяц/год\n")
    birthday = input()

    try:
        birthday_datetime = datetime.datetime.strptime(birthday,
                                                       '%d/%m/%Y').date()
        sign_finding(birthday_datetime)
    except ValueError:
        print("Введите верную дату")
        main()
    except AttributeError:
        print("Введите верную дату")
        main()

    """ Реализация выхода из программы по нажатию "y" или продолжения использования по нажатию "n". """

    print("Выйти из программы y/n?\n")
    exit_function = input()

    if exit_function == "n":
        print()
        main()
    elif exit_function == "y":
        raise SystemExit


if __name__ == '__main__':
    main()
