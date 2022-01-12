#-*- coding: utf-8 -*-

#9375 패션왕 신해빈.py

import sys
input = sys.stdin.readline

def make_dic(n):
    dic = {}

    for _ in range(n):
        _, b = input().split()

        if b in dic:
            dic[b] += 1
        else:
            dic[b] = 1

    return dic


for _ in range(int(input())):

    wear = make_dic(int(input()))
    answer = 1
    for i in wear.values():
        answer *= (1+i)

    print(answer-1)