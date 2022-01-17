#-*- coding: utf-8 -*-

#14889 스타트와 링크.py

#  => 최대 20C10 / 2 = 92,378이 최대
def team(matrix, check, start, minteam):

    if len(check) == N//2:
        sub_check = list(set(range(N)) - set(check))
        team1, team2 = 0, 0

        for i in range(N//2):
            for j in range(i, N//2):
                team1 += matrix[check[i]][check[j]] + matrix[check[j]][check[i]]
        
        for i in range(N//2):
            for j in range(i, N//2):
                team2 += matrix[sub_check[i]][sub_check[j]] + matrix[sub_check[j]][sub_check[i]]

        return abs(team1 - team2)

    else:
        for i in range(start, N):
            if i in check:
                continue
            else:
                check.append(i)
            sub = team(matrix, check, i+1, minteam)
            if minteam > sub: minteam = sub
            check.pop()

        return minteam

import sys
 
input = sys.stdin.readline

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
min_team = 100

print(team(matrix, [0], 1, min_team))