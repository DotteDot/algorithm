#-*- coding: utf-8 -*-

#2578 빙고.py

#1 숫자 놓기
#2 가로5 세로5 대각2 체크
matrix = [list(map(int, input().split())) for _ in range(5)]


def solve():
    cnt = 0
    bingo = []

    for _ in range(5):
        for i in list(map(int, input().split())):
            if len(bingo) >= 3:
                print(cnt)
                return
            cnt += 1

            flag = False
            for x in range(5):
                if flag: break
                for y in range(5):
                    if flag: break
                    if matrix[x][y] == i:
                        matrix[x][y] = -1
                        flag = True
            
            for n in range(1,13):
                if n not in bingo:
                    if 1 <= n < 6:
                        if matrix[n-1].count(-1) == 5: bingo.append(n)
                    elif 6 <= n < 11:
                        for i in range(5):
                            if matrix[i][n-6] != -1: break
                        else: bingo.append(n)
                    elif n == 11:
                        for i in range(5):
                            if matrix[i][i] != -1: break
                        else: bingo.append(n)
                    else:
                        for i in range(5):
                            if matrix[i][-i-1] != -1: break
                        else: bingo.append(n)


solve()