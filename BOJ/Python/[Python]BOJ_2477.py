#-*- coding: utf-8 -*-

#2477 참외밭.py

K = int(input())
lst = [list(map(int, input().split())) for _ in range(6)]
x_max_idx, y_max_idx = -1, -1
nx, ny = 0, 0


for idx, i in enumerate(lst):
    if i[0] == 1 or i[0] == 2:
        if x_max_idx == -1:
            x_max_idx = idx
        elif lst[x_max_idx][1] < i[1]:
            x_max_idx = idx
    else:
        if y_max_idx == -1:
            y_max_idx = idx
        elif lst[y_max_idx][1] < i[1]:
            y_max_idx = idx


if x_max_idx == (y_max_idx + 7) % 6:
    nx = lst[(x_max_idx + 8) % 6][1]
    ny = lst[(y_max_idx + 4) % 6][1]
else:
    ny = lst[(y_max_idx + 8) % 6][1]
    nx = lst[(x_max_idx + 4) % 6][1]


print(K * (lst[y_max_idx][1] * lst[x_max_idx][1] - nx * ny))