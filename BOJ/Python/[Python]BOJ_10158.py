#-*- coding: utf-8 -*-

#10158 개미.py

row, col = map(int, input().split())
sx, sy = map(int, input().split())
N = int(input())

# dx, dy = 1, 1
# for i in range(N):
#     if 0 > sx + dx or row < sx + dx: dx *= -1
#     if 0 > sy + dy or col < sy + dy: dy *= -1
    
#     sx, sy = sx + dx, sy + dy

# print(sx, sy)

# rx = N % (2 * row)
# ry = N % (2 * col)
# nx, ny = sx + rx, sy + ry
# if rx > row - sx:
#     if rx-(row-sx) > row:
#         nx = rx + sx - 2 * row
#     else:
#         nx = 2 * row - rx - sx

# if ry > col - sy:
#     if ry-(col-sy) > col:
#         ny = ry + sy - 2 * col
#     else:
#         ny = 2 * col - ry - sy

rx = N % (2 * row)
ry = N % (2 * col)
nx, ny = sx + rx, sy + ry
nx = abs(2 * row - rx - sx)

ny = abs(2 * col - ry - sy)

print(nx, ny)