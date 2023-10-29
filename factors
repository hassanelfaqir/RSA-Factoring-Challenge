# !/usr/bin/python3?
from sys import argv

def _fact(vall):
    """"print a simple descomposition of an integer > 1"""

    s = 2

    if (vall < 2):
        return
    print()
    print(vall, "<- value-bef")
    while vall % s:
        s += 1
    print("{:.0f}={:.0f}*{:.0f}".format(vall, vall / s, s))
    print(vall, "<- value-aft")
    print()

if len(argv) != 2:
    exit()

try:
    with open(argv[1]) as file:
        Line = file.readline()

        while Line != "":
            value = int(Line.split('\n')[0])
            _fact(value)
            Line = file.readline()
except:
    pass
