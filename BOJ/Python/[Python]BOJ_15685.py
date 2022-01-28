#-*- coding: utf-8 -*-

#15685 드래곤 커브.py

def dragon_curve(d, g):

    start = { 0:[1,0], 1:[0,-1], 2:[-1,0], 3:[0,1]}
    direct = [start[d]]

    for _ in range(g):
        tmp = []

        for i in range(len(direct)):
            if direct[-i-1] == [1,0]:
                tmp.append([0,-1])
            if direct[-i-1] == [0,1]:
                tmp.append([1,0])
            if direct[-i-1] == [-1,0]:
                tmp.append([0,1])
            if direct[-i-1] == [0,-1]:
                tmp.append([-1,0])
        direct.extend(tmp)

    return direct


N = int(input())
cnt = 0
lst = [list(map(int, input().split())) for _ in range(N)]
matrix = [[0] * 300 for _ in range(300)]

for a in lst:
    x, y, d, g = a
    x, y = x + 100, y + 100
    matrix[y][x] = '*'

    for now in dragon_curve(d, g):
        nx, ny = x + now[0], y + now[1]
        matrix[ny][nx] = '*'
        x, y = nx, ny

for y in range(300):
    for x in range(300):
        if matrix[y][x] == '*' and matrix[y][x+1] == '*' and matrix[y+1][x] == '*' and matrix[y+1][x+1] == '*':
            cnt += 1

print(cnt)