#-*- coding: utf-8 -*-

#23288 주사위 굴리기 2.py

from collections import deque

#1 (dfs / bfs)
# 먼저 나를 밟으면 몇점을 획득할 수 있는지 구해야한다. 
# (동일 번호 면적 몇개 구해서) 따로 matrix만들기 => 1000 * 1000 = 1,000,000
def calculate_score(x, y, map):
    matrix = [[0]*x for _ in range(y)]
    check = [[0]*x for _ in range(y)]
    xx, yy = [0, 0, 1, -1], [1, -1, 0, 0]
    queue = deque()

    for i in range(x):
        for j in range(y):
            start_num = 0
            tmp = []

            if not queue and matrix[j][i] == 0:
                queue.append([i, j])
                start_num = map[j][i]
                tmp.append([i,j])
                check[j][i] = 1

            while queue:                                    # 여기서부터 bfs --
                dx, dy = queue.popleft()

                for k in range(4):
                    nx, ny = dx+xx[k], dy+yy[k]

                    if 0 <= nx < x and 0 <= ny < y :
                        if map[ny][nx] == map[dy][dx]:
                            if check[ny][nx] == 0:
                                tmp.append([nx, ny])
                                check[ny][nx] = 1
                                queue.append([nx, ny])      # -- bfs 끝 --
            
            for k in tmp:                                   # matrix에 합을 채워넣는 부분
                matrix[k[1]][k[0]] = len(tmp) * start_num

    return matrix


import sys

input = sys.stdin.readline
y, x, n = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(y)]
map_score = calculate_score(x, y, map)

#2 (구현)
# map과 주사위 숫자를 비교해서 회전 or 변화x 판단
# 점수는 map_score[x][y]에서 가져오기.
# 반복 횟수는 k번.

#2-1 주사위 굴리기
# 1 2 3 4 5 6 {0:동쪽} 4 2 1 6 5 3
# 1 2 3 4 5 6 {1:남쪽} 2 6 3 4 1 5
# 1 2 3 4 5 6 {2:서쪽} 3 2 6 1 5 4
# 1 2 3 4 5 6 {3:북쪽} 5 1 3 4 6 2
# 바닥자리는 [-1]을 확인하면 된다
ewsn = 0
roll_dic = {
    0:[3,1,0,5,4,2],
    1:[1,5,2,3,0,4],
    2:[2,1,5,0,4,3],
    3:[4,0,2,3,5,1]
    }
dice = [1,2,3,4,5,6]
start_x, start_y = 0, 0
result = 0

for _ in range(n):
    if ewsn == 0:                                       # 끝점에 도달했을때를 다뤄준다
        next_x = start_x + 1                            # === 동쪽 ===
        if next_x < x:
            start_x = next_x
        else:
            ewsn = 2
            start_x -= 1
    elif ewsn == 2:                                     # === 남쪽 ===
        next_x = start_x - 1
        if 0 <= next_x:
            start_x = next_x
        else:
            ewsn = 0
            start_x += 1
    elif ewsn == 1:                                     # === 서쪽 ===
        next_y = start_y + 1
        if next_y < y:
            start_y = next_y
        else:
            ewsn = 3
            start_y -= 1
    else:                                               # === 북쪽 ===
        next_y = start_y - 1
        if 0 <= next_y:
            start_y = next_y
        else:
            ewsn = 1
            start_y += 1                                # 여기까지

    roll = roll_dic[ewsn]                               
    next_dice = [dice[i] for i in roll]
    dice_floor_num = next_dice[-1]
    result += map_score[start_y][start_x]

    if dice_floor_num > map[start_y][start_x]:          # 4 이상 처리해주기 위해
        ewsn = (ewsn + 5) % 4                           # (a + 1 + 4) % 4
    elif dice_floor_num < map[start_y][start_x]:
        ewsn = (ewsn + 3) % 4                           # 음수 처리해주기위해
                                                        # (a - 1 + 4) % 4
    dice = next_dice
    
print(result)