#-*- coding: utf-8 -*-

#2527 직사각형.py

for _ in range(4):
    x1, y1, x2, y2, X1, Y1, X2, Y2 = map(int, input().split())


    # D
    if x1 > X2 or X1 > x2 or Y1 > y2 or y1 > Y2:
        print('d')


    # B, C
    elif X1 == x2 or X2 == x1:
        print('c') if (y1 == Y2 or y2 == Y1) else print('b')
    elif Y1 == y2 or Y2 == y1:
        print('c') if (x1 == X2 or x2 == X1) else print('b')


    # A
    else:
        print('a')