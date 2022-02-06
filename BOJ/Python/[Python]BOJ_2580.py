#-*- coding: utf-8 -*-

#2580 스도쿠.py

import sys

def find_col(x, y, target):
    for i in range(9):
        if y != i and matrix[i][x] == target:
            return -1
    return 1


def square(x, y, target):
    for i in range(3):
        for j in range(3):
            nx, ny = 3*(x//3)+j, 3*(y//3)+i
            if y != ny and x != nx and matrix[ny][nx] == target:
                return -1
    return 1


def dfs():
    if not idx_lst:
        for i in range(9):
            print(*matrix[i])
        exit()

    x, y = idx_lst.pop()

    for i in range(1,10):
        if i not in matrix[y]:
            matrix[y][x] = i
            if find_col(x, y, i) == 1 and square(x, y, i) == 1:
                dfs()
            matrix[y][x] = 0

    idx_lst.append([x, y])


if __name__=="__main__":
    input = sys.stdin.readline
    matrix = [list(map(int, input().split())) for _ in range(9)]
    idx_lst = []
    for i in reversed(range(9)):
        for j in reversed(range(9)):
            if matrix[i][j] == 0:
                idx_lst.append([j, i])

    dfs()