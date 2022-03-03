#-*- coding: utf-8 -*-

#13460 구슬 탈출 2.py

# r_loc: r의 위치, b_loc: b의 위치
# direction: 동남서북( [[1,0],[0,1],[-1,0],[0,-1]] )
# 0 <= cnt < 11
def dfs(r_loc, b_loc, direction, cnt):
    global MIN

    if cnt > 10:
        return

    r_sx, r_sy = r_loc[0], r_loc[1]
    b_sx, b_sy = b_loc[0], b_loc[1]
    out = 0
    
    while True:
        r_nx, r_ny = r_sx + direction[0], r_sy + direction[1]
        b_nx, b_ny = b_sx + direction[0], b_sy + direction[1]

        flag = 0
        if 1 <= r_nx < n[0]-1 and 1 <= r_ny < n[0]-1:
            if (r_nx, r_ny) != (b_sx, b_sy):
                if mat[r_ny][r_nx] == '.':
                    r_sx = r_nx
                    r_sy = r_ny
                    flag += 1
                elif mat[r_ny][r_nx] == 'O':
                    out = cnt
                    r_sx = -10
                    r_sy = -10
                    flag += 1

        if 1 <= b_nx < n[0]-1 and 1 <= b_ny < n[0]-1:
            if (b_nx, b_ny) != (r_sx, r_sy):
                if mat[b_ny][b_nx] == '.':
                    b_sx = b_nx
                    b_sy = b_ny
                    flag += 1
                elif mat[b_ny][b_nx] == 'O':
                    return

        if flag == 0:
            break

    if out > 0:
        MIN = min(MIN, out)

    for i in d:
        dfs((r_sx, r_sy), (b_sx, b_sy), i, cnt+1)


n = list(map(int, input().split()))
n = [n[1],n[0]]
mat = [list(input().strip()) for _ in range(n[1])]
d = [[1,0],[0,1],[-1,0],[0,-1]]
MIN = 11

for i in range(n[1]):
    for j in range(n[0]):
        if mat[i][j] == 'B':
            b_loc = j, i
            mat[i][j] = '.'
        if mat[i][j] == 'R':
            r_loc = j, i
            mat[i][j] = '.'

for i in d:
    dfs(r_loc, b_loc, i, 1)

if MIN == 11:
    print(-1)
else:
    print(MIN)