from motorsykkel import Motorsykkel


def hovedprogram():
    Frida = Motorsykkel("Vespa", 344122, 71.5)
    Raceren = Motorsykkel("Harley Davidson", 666666, 32789.6)
    Skrotet = Motorsykkel("Mitsubishi", 918273, 169783.4)

    Skrotet.kjør(120)
    print(Skrotet.hentKilometeravstand())


hovedprogram()
