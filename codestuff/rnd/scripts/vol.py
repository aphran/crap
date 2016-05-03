#!/usr/bin/env python2
from math import pi
def volume_of_piz(z,a):
    return pi*z*z*a
def __main__():
    print("Welcome to the pizza volume calculator")
    z = int(raw_input("Enter radius: "))
    a = int(raw_input("Enter depth: "))
    v = volume_of_piz(z,a)
    print("The volume of your pizza is: %s " % v)
__main__()
