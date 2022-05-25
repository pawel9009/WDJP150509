import collections as c
import random as r


def a(arg):
    znak = chr(r.randint(97, 122))
    print(znak)
    liczba = c.Counter(arg)
    print(liczba[znak])


def b(arg):
    losowa_cyfra = str(r.randint(0, 9))
    print(losowa_cyfra)
    arg = str(arg)
    while True:
        if losowa_cyfra in c.Counter(arg):
            ind = arg.find(losowa_cyfra)
            arg = arg[:ind]+arg[ind+1:]
        else:
            break
    print(arg)
