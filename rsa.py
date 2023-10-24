#!/usr/bin/python3

# library to get arguments
import sys

# _facto unpack number factorial
def _facto():
    """
    function _facto to search file to convert number and format n=p*q
    """
    try:
        r_file = sys.argv[1]
        with open(r_file) as file:
            for r_number in file:
                r_number = int(r_number)
                if r_number % 2 == 0:
                        print("{}={}*{}".format(r_number, r_number // 2, 2))
                        continue
                s = 3
                while s < r_number // 2:
                    if r_number % s == 0:
                        print("{}={}*{}".format(r_number, r_number // s, s))
                        break
                    s = s + 2
                if s == (r_number // 2) + 1:
                    print("{}={}*{}".format(r_number, r_number, 1))
    except (IndexError):
        pass

# autostart
_facto()
