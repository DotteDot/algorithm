#-*- coding: utf-8 -*-

#10158 개미.py

row, col = map(int, input().split())
sx, sy = map(int, input().split())
N = int(input())

rx = N % (2 * row)
ry = N % (2 * col)
nx, ny = sx + rx, sy + ry

if rx > row - sx:
    nx = abs(2 * row - rx - sx)

if ry > col - sy:
    ny = abs(2 * col - ry - sy)

print(nx, ny)