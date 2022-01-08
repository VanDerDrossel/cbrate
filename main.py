from cbrate import get_quotes


def main():
    """for example"""
    usd = get_quotes('USD')
    eur = get_quotes('EUR')
    print(f'Курс "{usd.name}" по данным ЦБ на {usd.date} составляет {usd.value}')
    print(f'Курс "{eur.name}" по данным ЦБ на {eur.date} составляет {eur.value}')


if __name__ == '__main__':
    main()
