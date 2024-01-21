import os
import sys
import collections
import math

class Fraction:
    a, b = map(int, input().split())
    query = int(input())
    for i in range(query):
        operator, c, d = map(int, input().split())
        print()
        if operator == 1:
            x = (a*d)+(b*c)
            y = b*d
            z = math.gcd(x, y)
            a, b = int(x/z), int(y/z)
            print("{}/{}".format(a, b))
            print()
        if operator == 2:
            p = a*c
            q = b*d
            r = math.gcd(p, q)
            p, q = int(p/r), int(q/r)
            print("{}/{}".format(p, q))
            print()