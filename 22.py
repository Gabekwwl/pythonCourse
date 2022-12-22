'''
import math


def prostokat(a, b):
    print(f'Przekątna : {math.sqrt((math.pow(a, 2)) + math.pow(b, 2))}')
    return
a = float(input("Podaj długość pierwszego boku: "))
b = float(input("Podaj długość drugiego boku: "))
prostokat(a, b)

string = "1"
lstring = ("a", "b", "c", "d")
def funkcja(string, lstring):
    x = string.join(lstring)
    print(x)
    return
funkcja(string, lstring)


def funk(imie, wiek, wzrost_m):
    print(f"{imie}, lat {wiek}, {wzrost_m} m wzrostu")
    pass
funk("Jan", "20", "1.75")
'''

import time
x = time.localtime()
print(x)