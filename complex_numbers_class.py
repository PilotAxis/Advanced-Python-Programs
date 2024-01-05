from os import *
from sys import *
from collections import *
from math import *



class ComplexNumbers:
    def __init__(self, r1, i1, r2, i2):
        self.r1 = r1
        self.i1 = i1
        self.r2 = r2
        self.i2 = i2
    def plus(self):
        real = self.r1 + self.r2
        imag = self.i1 + self.i2
        print(str(real), "+", "i" + str(imag))
    def mult(self):
        real = (self.r1 * self.r2) - (self.i1 * self.i2)
        imag = (self.r1 * self.i2) + (self.i1 * self.r2)
        print(str(real), "+", "i" + str(imag))
#Driver's code goes here.
r1, i1 = map(int, input().split())
r2, i2 = map(int, input().split())
choice = int(input())
c = ComplexNumbers(r1, i1, r2, i2)
if choice == 1:
    c.plus()
elif choice == 2:
    c.mult()
else:
    print("")