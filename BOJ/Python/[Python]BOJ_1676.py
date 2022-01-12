#-*- coding: utf-8 -*-

#1676 팩토리얼 0의 개수.py

num = 1
n = 0

for i in range(1, int(input())+1): num *= i

for j in reversed(str(num)):
    if j != '0': print(n); break
    else: n += 1