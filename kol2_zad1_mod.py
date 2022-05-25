import collections as c

Book = c.namedtuple('Book', 'title price')


def ile_znakow(arg):
    i = 0
    for _ in arg.title:
        i += 1
    return i


def najdrozsza(args):
    cena_max = args[0].price
    for ks in args:
        if ks.price > cena_max:
            cena_max = ks.price
    return cena_max


