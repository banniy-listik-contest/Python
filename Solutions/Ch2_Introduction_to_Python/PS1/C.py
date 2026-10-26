# -*- coding: utf-8 -*-

import sys


sys.stdin = open("test_C.txt")
down_payment = 200000
init_depozit = float(input())
months = 36
eps = 100

r_min, r_max = 0, 1
r = (r_min + r_max) / 2
steps = 1


if (temp := (1 + r_max / 12) ** 36 * init_depozit) - down_payment < 0:
    print('None 0')
else:
    while abs(temp := (1 + r / 12) ** 36 * init_depozit - down_payment) > eps:
        steps += 1
        if temp > 0:
            r_max = r
        else:
            r_min = r
        r = (r_min + r_max) / 2
    print(r, steps)
print(input(), input())