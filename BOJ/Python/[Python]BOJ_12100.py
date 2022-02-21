#-*- coding: utf-8 -*-

#12100 2048 (Easy).py

from copy import deepcopy

def move(lst, num, cnt):
    global MAX, N

    if cnt == 5:
        for i in range(N):
            for j in range(N):
                if MAX < lst[i][j]:
                    MAX = max(MAX, lst[i][j])
        return

    lst = deepcopy(lst)


    # 위로 모으기
    if num == 1:
        for x in range(N):
            s = 0
            for y in range(N-1):
                i = 1
                for j in range(1,N):
                    if y+j < N and lst[y+j][x]:
                        i = j;
                        break
                if lst[y][x]:
                    if lst[y][x] == lst[y+i][x]:
                        lst[y][x] *= 2
                        lst[y+i][x] = 0
                    lst[s][x] = lst[y][x]
                    s += 1
            lst[s][x] = lst[N-1][x]
            while N-1 > s:
                s += 1
                lst[s][x] = 0


    # 아래로 모으기
    if num == 2:
        for x in range(N):
            s = N-1
            for y in range(1,N)[::-1]:
                i = 1
                for j in range(1,N):
                    if 0 <= y-j and lst[y-j][x]:
                        i = j;
                        break
                if lst[y][x]:
                    if lst[y][x] == lst[y-i][x]:
                        lst[y][x] *= 2
                        lst[y-i][x] = 0
                    lst[s][x] = lst[y][x]
                    s -= 1
            lst[s][x] = lst[0][x]
            while s > 0:
                s -= 1
                lst[s][x] = 0


    # 왼쪽으로 모으기
    if num == 3:
        for y in range(N):
            s = 0
            for x in range(N-1):
                i = 1
                for j in range(1,N):
                    if x+j < N and lst[y][x+j]:
                        i = j;
                        break
                if lst[y][x]:
                    if lst[y][x] == lst[y][x+i]:
                        lst[y][x] *= 2
                        lst[y][x+i] = 0
                    lst[y][s] = lst[y][x]
                    s += 1
            lst[y][s] = lst[y][N-1]
            while N-1 > s:
                s += 1
                lst[y][s] = 0


    # 오른쪽으로 모으기
    if num == 4:
        for y in range(N):
            s = N-1
            for x in range(1,N)[::-1]:
                i = 1
                for j in range(1,N):
                    if 0 <= x-j and lst[y][x-j]:
                        i = j;
                        break
                if lst[y][x]:
                    if lst[y][x] == lst[y][x-i]:
                        lst[y][x] *= 2
                        lst[y][x-i] = 0
                    lst[y][s] = lst[y][x]
                    s -= 1
            lst[y][s] = lst[y][0]
            while s > 0:
                s -= 1
                lst[y][s] = 0

    move(lst, 1, cnt+1)
    move(lst, 2, cnt+1)
    move(lst, 3, cnt+1)
    move(lst, 4, cnt+1)


if __name__=="__main__":
    global MAX, N
    MAX = 0
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]

    move(mat, 1, 0)
    move(mat, 2, 0)
    move(mat, 3, 0)
    move(mat, 4, 0)
    print(MAX)