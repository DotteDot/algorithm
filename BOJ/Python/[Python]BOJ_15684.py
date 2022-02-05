#-*- coding: utf-8 -*-

#15684 사다리 조작.py

global x, y
x, M, y = map(int, input().split())
matrix = [[0]*(x+1) for _ in range(y+2)]
stair = [0]*(x+1)
for _ in range(M):
    i, j = map(int, input().split())
    stair[j] += 1
    matrix[i][j] = j
    matrix[i][j+1] = j


for j in range(y+1):
    print(matrix[j])
def check_start(init_stair):
    cnt = 0
    result = []
    for idx, s in enumerate(init_stair):
        if cnt > 3: return 0
        if s % 2: 
            cnt += 1
            result.append(idx)
    return result

def down():
    global x, y
    
        
    for i in range(1, x + 1):
        sx, sy = i, 0
        print(f'\nSTART [{i}, 0] ====')
        for j in range(y+1):
            print(matrix[j])


        while True:
            nx, ny = sx, sy + 1
            # print(nx, ny)

            if sy == y + 1:
                # print(sx, i, sy, y+1)
                if sx == i: break
                else: return False

            if matrix[ny][nx] != 0:
                if nx + 1 <= x and matrix[ny][nx + 1] == matrix[ny][nx]:
                    sx = nx + 1
                elif 0 < nx - 1 and matrix[ny][nx - 1] == matrix[ny][nx]:
                    sx = nx - 1
            sy = ny

        print(f'END    [{i}] ====')
    return True

def dfs(cnt):
    if len(point) == 0:
        if down():
            print(cnt)
            return True
        return False
    p = point.pop()
    for i in range(1, y+1):
        if matrix[i][p] == 0 and matrix[i][p+1] == 0:
            matrix[i][p] = matrix[i][p+1] = p
            print(f'APPEND [{p}, {i}] and [{p+1}, {i}]')
            if dfs(cnt + 1):
                return True
            matrix[i][p] = matrix[i][p+1] = 0
    point.append(p)




point = check_start(stair)
print(point)
if type(point) == list:
    if not dfs(0):
        print(-1)
else:
    print(-1)