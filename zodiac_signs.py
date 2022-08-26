import datetime


def print_signs(signs: str) -> None:
    """ Выводит на экран ответ в формате: Ваш знак Зодиака: ..."""

    print(f"Ваш знак Зодиака: {signs}.\n")


def sign_finding(birthday_datetime):
    """ Сравнивает объект Datetime с интервалами времени, соответствующими
    определенному знаку в цикле for."""

    dict_sign = [["capricorn", datetime.date(birthday_datetime.year, 12, 22),
                  datetime.date(birthday_datetime.year, 12, 31)],
                 ["capricorn", datetime.date(birthday_datetime.year, 1, 1),
                  datetime.date(birthday_datetime.year, 1, 19)],
                 ["aquarius", datetime.date(birthday_datetime.year, 1, 20),
                  datetime.date(birthday_datetime.year, 2, 18)],
                 ["pisces", datetime.date(birthday_datetime.year, 2, 19),
                  datetime.date(birthday_datetime.year, 3, 20)],
                 ["aries", datetime.date(birthday_datetime.year, 3, 21),
                  datetime.date(birthday_datetime.year, 4, 19)],
                 ["taurus", datetime.date(birthday_datetime.year, 4, 20),
                  datetime.date(birthday_datetime.year, 5, 20)],
                 ['twins', datetime.date(birthday_datetime.year, 5, 21),
                  datetime.date(birthday_datetime.year, 6, 20)],
                 ["crayfish", datetime.date(birthday_datetime.year, 6, 21),
                  datetime.date(birthday_datetime.year, 7, 22)],
                 ["lion", datetime.date(birthday_datetime.year, 7, 23),
                  datetime.date(birthday_datetime.year, 8, 22)],
                 ["virgo", datetime.date(birthday_datetime.year, 8, 23),
                  datetime.date(birthday_datetime.year, 9, 22)],
                 ["scales", datetime.date(birthday_datetime.year, 9, 23),
                  datetime.date(birthday_datetime.year, 10, 22)],
                 ["scorpion", datetime.date(birthday_datetime.year, 10, 23),
                  datetime.date(birthday_datetime.year, 11, 30)],
                 ["sagittarius", datetime.date(birthday_datetime.year, 11, 22),
                  datetime.date(birthday_datetime.year, 12, 21)]]

    for i in range(len(dict_sign)):
        if dict_sign[i][1] <= birthday_datetime <= dict_sign[i][2]:
            print_signs(dict_sign[i][0])


def main() -> None:
    """ Получаем строку от пользователя в формате "день/месяц/год".
     Проверяем ошибки ввода пользователя. Проверяем является ли год високосным.
     После проверок переводим строку в объект Datetime и передаем функции
      sign_finding. """

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

    """ Реализация выхода из программы по нажатию y или n. """

    print("Выйти из программы y/n?\n")
    exit_function = input()

    if exit_function == "n":
        print()
        main()
    elif exit_function == "y":
        raise SystemExit


if __name__ == '__main__':
    main()
