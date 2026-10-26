# -*- coding: utf-8 -*-

import sys


sys.stdin = open('test_B.txt')
yearly_salary = float(input())
portion_saved = float(input())
cost_of_dream_house = float(input())
semi_annual_raise = float(input())
portion_down_payment = 0.25
r = 0.05

monthly_saved = yearly_salary * portion_saved / 12
total_saved = monthly_saved
down_payment = cost_of_dream_house * portion_down_payment
months = 1
i = 1
while down_payment > total_saved:
    total_saved = total_saved * (1 + r / 12) + monthly_saved
    months += 1
    i += 1
    if i == 6:
        i = 0
        monthly_saved *= (1 + semi_annual_raise)

print(months, input())