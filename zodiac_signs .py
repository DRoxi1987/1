import datetime


def printsigns(signs: str) -> None:
    """ Выводит на экран ответ в формате: Ваш знак Зодиака: ..."""
    print(f"Ваш знак Зодиака: {signs}.")


def main() -> None:
    print("Введите дату рождения: день/месяц/год")
    birthday = input()

    if 0 <= int(birthday.split("/")[1]) <= 12:
        global birthday_datetime
        birthday_datetime = datetime.datetime.strptime(birthday,
                                                       '%d/%m/%Y').date()
    else:
        print("Введите правильную дату")
        main()
    # Получаем строку от пользователя в формате "день/месяц/год" и переводим в
    # datetime.

    # Списки для каждого знака в формате datetime.date. [дата начала знака, Дата конца знака]

    capricorn1 = [datetime.date(birthday_datetime.year, 12, 22),
                  datetime.date(birthday_datetime.year, 12, 31)]

    capricorn2 = [datetime.date(birthday_datetime.year, 1, 1),
                  datetime.date(birthday_datetime.year, 1, 19)]

    sagittarius1 = [datetime.date(birthday_datetime.year, 12, 1),
                    datetime.date(birthday_datetime.year, 12, 21)]

    sagittarius2 = [datetime.date(birthday_datetime.year, 11, 22),
                    datetime.date(birthday_datetime.year, 11, 30)]

    aquarius = [datetime.date(birthday_datetime.year, 1, 20),
                datetime.date(birthday_datetime.year, 1, 31)]

    pisces = [datetime.date(birthday_datetime.year, 2, 19),
              datetime.date(birthday_datetime.year, 3, 20)]

    aries = [datetime.date(birthday_datetime.year, 3, 21),
             datetime.date(birthday_datetime.year, 4, 19)]

    taurus = [datetime.date(birthday_datetime.year, 4, 20),
              datetime.date(birthday_datetime.year, 5, 20)]

    twins = [datetime.date(birthday_datetime.year, 5, 21),
             datetime.date(birthday_datetime.year, 6, 20)]

    crayfish = [datetime.date(birthday_datetime.year, 6, 21),
                datetime.date(birthday_datetime.year, 7, 22)]

    lion = [datetime.date(birthday_datetime.year, 7, 23),
            datetime.date(birthday_datetime.year, 8, 22)]

    virgo = [datetime.date(birthday_datetime.year, 8, 23),
             datetime.date(birthday_datetime.year, 9, 22)]

    scales = [datetime.date(birthday_datetime.year, 9, 23),
              datetime.date(birthday_datetime.year, 10, 22)]

    scorpion = [datetime.date(birthday_datetime.year, 10, 23),
                datetime.date(birthday_datetime.year, 11, 30)]

    if capricorn1[0] <= birthday_datetime <= capricorn1[1] or \
            capricorn2[0] <= birthday_datetime <= capricorn2[1]:
        printsigns("Козерог")

    elif sagittarius1[0] <= birthday_datetime <= sagittarius1[1] or \
            sagittarius2[0] <= birthday_datetime <= sagittarius2[1]:
        printsigns("Стрелец")

    elif aquarius[0] <= birthday_datetime <= aquarius[1]:
        printsigns("Водолей")

    elif pisces[0] <= birthday_datetime <= pisces[1]:
        printsigns("Рыбы")

    elif aries[0] <= birthday_datetime <= aries[1]:
        printsigns("Овен")

    elif taurus[0] <= birthday_datetime <= taurus[1]:
        printsigns("Телец")

    elif twins[0] <= birthday_datetime <= twins[1]:
        printsigns("Близнецы")

    elif crayfish[0] <= birthday_datetime <= crayfish[1]:
        printsigns("Рак")

    elif lion[1] <= birthday_datetime <= lion[1]:
        printsigns("Лев")

    elif virgo[0] <= birthday_datetime <= virgo[1]:
        printsigns("Дева")

    elif scales[0] <= birthday_datetime <= scales[1]:
        printsigns("Весы")

    elif scorpion[0] <= birthday_datetime <= scorpion[1]:
        printsigns("Скорпион")


if __name__ == '__main__':
    main()
    print("Нажмите Enter для выхода из программы")
    input()
