import math
# zadania rozdzielone nowa linią oraz zakomentowane

# print("Witaj Swiecie")
#
# print(5 + 5)
#
# print(10 // 2)
#
# zad4 = input().split(' ')
# print(f'{zad4[1]}\n{zad4[0]}')
#
# zad5 = input().split(' ')
# print(int(zad5[0]) * int(zad5[1]) * int(zad5[2]))
#
# for q in range(6):
#     for w in range(6):
#         print(q * w)
#
# zad7 = input().split(' ')
# zad7_a, zad7_b, zad7_c = int(zad7[0]), int(zad7[1]), int(zad7[2])
# sredna_arytmetyczna = (zad7_a + zad7_b + zad7_c) / 3
# sredna_geometryczna = math.pow((zad7_a * zad7_b * zad7_c), 1 / 3)
# print("srednia ary", sredna_arytmetyczna)
# print("srednia geo", sredna_geometryczna)
#
# stopnie = input("Podaj ilosc stopni")
# print("Fahrenheit", (float(stopnie) * 1.8) + 32)
# print("Kelvin", float(stopnie) + 273.15)
#
# zad9 = input()
# zad9 = zad9[0] + zad9[2:]
# print(zad9)
#
# zad10 = input()
# pom = zad10[0]
# zad10 = zad10[-1] + zad10[1:]
# zad10 = zad10[:-1] + pom
# print(zad10)
#
# zad11 = input()
# print(zad11.lower())
#
# for x in range(1, 100, 2):
#     print(x)
#
# suma = 0
# for x in range(0, 200, 2):
#     suma += x
#     print(suma)
# print(suma)
#
# zad14 = input()
# suma = 0
# for x in zad14:
#     suma += int(x)
# print(suma)
#
# zad15 = input().split(' ')
# zad15_a, zad15_b, zad15_c = int(zad15[0]), int(zad15[1]), int(zad15[2])
# lista = [zad15_a, zad15_b, zad15_c]
# minimum = zad15_a
# maximum = zad15_a
# for x in lista:
#     if x < minimum:
#         minimum = x
#     if x > maximum:
#         maximum = x
# print(minimum, maximum)
#
# zad16 = int(input())
# for x in range(zad16, 0, -1):
#     print(x * str(zad16))
#
# wiek = 20
# wiek = 23
# print("wiek", wiek)
#
# print("""
#               *
# *             *             *
#    *          *         *
#         *     *     *
#             * * *
#             * * *
#         *     *    *
#      *        *       *
#   *           *           *
# *             *               *
#
# """)
#
# zad19 = input()
# print((float(zad19) * math.pi) / 180)
#
# zad20 = input().split(' ')
# zad20_a, zad20_b, zad20_c = float(zad20[0]), float(zad20[1]), float(zad20[2])
# o = zad20_a + zad20_b + zad20_c
# p = o / 2
# print(f'obwod = {o} a pole = {math.sqrt(p * (p - zad20_a) * (p - zad20_b) * (p - zad20_c))}')
#
# zadania
# 21 - 27
# a = 5
# b = 10
# c = 6
# r = 7
# h = 5
# l = 5
# print(f'pole kwadratu {a * a} obwod = {4 * a}')
# print(f'pole prostokata {a * b} obwod = {2 * a + 2 * b}')
# print(f'pole kuli {4 * math.pi * r * r} objetosc = {(4 * math.pi * r * r * r) / 3}')
# print(f'pole szescianu {a * a * 6} objetosc = {a * a * a}')
# print(f'pole walca {2 * (math.pi * r * r) + 2 * math.pi * r * h} objetosc = {math.pi * r * r * h}')
# print(f'pole prostopadloscianu {2 * (a * b + a * c + b * c)} objetosc = {a * b * c}')
# print(f'pole stozka {math.pi * r * (r + l)} objetosc = {(math.pi * r * r * h) / 3}')
#
# zad28 = input().split(' ')
# zad28_a, zad28_b = int(zad28[0]), int(zad28[1])
# if zad28_b:
#     print(f'wynik dzielenia = {zad28_a / zad28_b}')
# else:
#     print('dzielisz przez zero')
#
# zad29 = int(input())
# if zad29 < 0:
#     print("liczba mniejsza od zera")
# else:
#     print(math.sqrt(zad29))
#
# zad30 = int(input())
# if zad30 % 2 == 0:
#     print('liczba parzysta')
# else:
#     print('liczba nieparzysta')
#
# zad31 = input().split(' ')
# zad31_a, zad31_b = int(zad31[0]), int(zad31[1])
# if zad31_a % zad31_b == 0:
#     print(f'liczba {zad31_a} jest podzielna przez {zad31_b}')
# else:
#     print(f'liczba {zad31_a} nie jest podzielna przez {zad31_b}')
#
# zad32 = input().split(' ')
# zad32_a, zad32_b, zad32_c = int(zad32[0]), int(zad32[1]), int(zad32[2])
# lista = [zad32_a, zad32_b, zad32_c]
# posortowana = []
# for a in range(2):
#     for x in range(2):
#         if lista[x] < lista[x + 1]:
#             pom = lista[x]
#             lista[x] = lista[x + 1]
#             lista[x + 1] = pom
# print(lista)

# zad33 = input().split(' ')
# zad33_a, zad33_b = int(zad33[0]), int(zad33[1])
# if zad33_a==0:
#     if zad33_b==0:
#         print('rownanie tozsamosciowe')
#     else:
#         print('rownanie sprzeczne')
# else:
#     print(-zad33_b/zad33_a)

# zad34 = input().split(' ')
# zad34_a, zad34_b, zad34_c = int(zad34[0]), int(zad34[1]), int(zad34[2])
# if zad34_a==0:
#     print(-zad34_c/zad34_b)
# else:
#     delta = zad34_b*zad34_b - 4*zad34_a*zad34_c
#     if delta < 0:
#         print('brak rozwiazan')
#     elif delta == 0:
#         print('rozwiazanie',-zad34_b/(2*zad34_a))
#     else:
#         x1 = (-zad34_b + math.sqrt(delta))/(2*zad34_a)
#         x2 = (-zad34_b - math.sqrt(delta))/(2*zad34_a)
#         print(f'rozwiazania = {x1} oraz {x2}')

#
# zad35 = int(input())
# if zad35 >= 1 and zad35 <= 31:
#     print("poprawny dzien")
# else:
#     print('bledna liczba')
#
# zad36 = int(input())
# if zad36 >= 1 and zad36 <= 12:
#     print("poprawny miesiac")
# else:
#     print('bledna liczba')
#
# zad37 = int(input())
# if zad37 % 4 == 0 and (zad37 % 100 != 0 or zad37 % 400 == 0):
#     print('rok przestepny')
# else:
#     print('normalny rok')
#
# zad
# 38
# dzien = int(input())
# miesiac = int(input())
# rok = int(input())
# if rok % 4 == 0 and (rok % 100 != 0 or rok % 400 == 0):
#     pom = [1, 3, 5, 7, 8, 10, 12]
#     if miesiac >= 1 and miesiac <= 12:
#         if miesiac == 2:
#             if dzien >= 1 and dzien <= 29:
#                 print('poprawna')
#             else:
#                 print('blad')
#         elif miesiac in pom:
#             if dzien >= 1 and dzien <= 31:
#                 print('poprawna')
#             else:
#                 print('blad')
#         else:
#             if dzien >= 1 and dzien <= 30:
#                 print('poprawna')
#             else:
#                 print('blad')
#     else:
#         print('blad')
# else:
#     pom = [1, 3, 5, 7, 8, 10, 12]
#     if miesiac >= 1 and miesiac <= 12:
#         if miesiac == 2:
#             if dzien >= 1 and dzien <= 28:
#                 print('poprawna')
#             else:
#                 print('blad')
#         elif miesiac in pom:
#             if dzien >= 1 and dzien <= 31:
#                 print('poprawna')
#             else:
#                 print('blad')
#         else:
#             if dzien >= 1 and dzien <= 30:
#                 print('poprawna')
#             else:
#                 print('blad')
#     else:
#         print('blad')
#
# zad
# 39
# godzina = int(input())
# minuta = int(input())
# sekunda = int(input())
# ok = None
# if godzina >= 0 and godzina <= 23:
#     if minuta >= 0 and minuta <= 59:
#         if sekunda >= 0 and sekunda <= 59:
#             ok = True
# if ok:
#     print('poprawna godzina')
# else:
#     print('zla godzina')
#
# zad40 = input()
# if zad40 == zad40[::-1]:
#     print('palindrom')
# else:
#     print('to nie palindrom')
#
# zad41
# for x in range(17):
#     print('*', end=' ')
#
# zad42
# for y in range(4):
#     print('P' * 25)
#
# zad43 = int(input())
# i = 2
# for x in range(zad43):
#     print(end='\n')
#     for y in range(1, i):
#         print(y, end=' ')
#     i += 1
#
# zad 44
# t = int(input())
# l = []
# for x in range(t):
#     l.append([1 for q in range(len(l) + 1)])
# for x in range(len(l)):
#     if x > 1:
#         for a in range(1, len(l[x]) - 1):
#             l[x][a] = l[x - 1][a - 1] + l[x - 1][a]
#     print('  ' * (t - x), l[x])
#
# 45
# nie
# rozumiem
#
# zad46 = int(input())
# suma = 0
# for x in range(zad46):
#     suma += x
# print(suma)
#
# zad47 = int(input())
# suma = 0
# for x in range(1, zad47 * 2, 2):
#     suma += x
# print(suma)
#
# zad48 = int(input())
# suma = 0
# for x in range(2, zad48 * 2 + 1, 2):
#     suma += x
# print(suma)
