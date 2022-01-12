#-*- coding: utf-8 -*-

#1011.py

'''
1  1		1	1
2  11		2	1
3  111		3	2
4  121		3
5  1211		4	2
6  1221		4
7  12211	5	3
8  12221	5
9  12321	5
10 123211	6	3
11 123221	6
12 123321	6
13 1233211	7	4
14 1233221	7	
15 1233321	7	
16 1234321	7	
'''

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    x, y = map(int, input().split())
    i = 1
    mx, mn = 2, 0
    while True:
        if mn < y-x <= mx:
            if mn < y-x <= mn + i: print(i*2-1)
            else: print(i*2)
            break
        else:
            i += 1
            mx, mn = mx + i*2, mx