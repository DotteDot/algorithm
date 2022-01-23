#-*- coding: utf-8 -*-

#17142 연구소 3.py

from collections import deque

global minimum, wall_count
n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
virous = []                                     # 활성화, 비활성화 바이러스의 위치
act_virous = []                                 # 활성화 바이러스의 위치
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
minimum, wall_count = 2501, 0                   # min은 50 * 50 + 1로 잡아줬다.

for i in range(n):                              # 벽의 갯수를 count하고,
    wall_count += matrix[i].count(1)            # 바이러스의 위치를 저장

    for j in range(n):
        if matrix[i][j] == 2:
            virous.append((j, i, 0))            # 마지막에 0이 들어가는 이유는 bfs돌릴때 퍼지는 시간 저장을 위해


def check_result(check, result):                # 결과값을 출력하는 함수
    global minimum, wall_count

    if check == wall_count:                     # 벽의 개수와 '*'의 개수에 따라 결과값을 저장한다.
        minimum = result                        # 빈곳 없이 바이러스가 퍼졌다면 벽개수 == '*'개수
    else:
        if minimum == 2501:                     # 벽의 개수가 다르고, minumum에 값이 없다면
            minimum = -1                        # minumum = -1이다.


def make_virous(virous_loc):                    # 바이러스 퍼져나감을 위한 bfs
    global minimum
    queue = deque(virous_loc)
    check = [['*'] * n for _ in range(n)]
    maximum = 0
    star_cnt = n ** 2                           # '*'갯수를 파악하기 위해 초기화
    
    while queue:
        x, y, cnt = queue.popleft()
        if check[y][x] == '*':                  # 이 부분은 나중에 '*'인 부분을 count 함수를
            check[y][x] = cnt                   # 돌려도 되긴 한데 시간 더 걸려서 이렇게 처리.
            star_cnt -= 1
        else:                                   # 시간초과 해결
            continue

        if (x, y, 0) not in virous:             # 비활성화 바이러스를 거칠때는
            maximum = max(maximum, cnt)         # max를 갱신하지 않는다.

        if minimum != -1 and cnt == minimum and (x, y, 0) not in virous:
            break                               # 비활성화 바이러스에 있다면 break를 하면 안된다.

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if matrix[ny][nx] != 1 and check[ny][nx] == '*':
                    queue.append((nx, ny, cnt + 1))

    check_result(star_cnt, maximum)


def active(s):                                  # 일반적인 combinaton을 구현
                                                # 바이러스에 활성화되는 모든 조합을 구한다.
    if len(act_virous) == m:
        make_virous(act_virous)
        return
    else:
        for act in range(s, len(virous)):
            if virous[act] not in act_virous:
                act_virous.append(virous[act])
                active(act + 1)
                act_virous.pop()

active(0)
print(minimum)