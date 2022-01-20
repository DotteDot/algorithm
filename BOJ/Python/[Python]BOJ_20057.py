#-*- coding: utf-8 -*-

#20057 마법사 상어와 토네이도.py

def tornado(push_sand, N):
    x = y = N // 2
    dir = 0
    result = 0

    for i in range(1, N + 1):
        for _ in range(2):
            for _ in range(i):
                if x == y and x == 0: return result

                dx, dy = push_sand[dir]['ewsn']
                nx, ny = x + dx, y + dy
                move_sand = 0

                for j in list(push_sand[dir].keys())[1:]:
                    sx, sy = j
                    p_sand = int(sand[ny][nx] * push_sand[dir][j])
                    if 0 <= nx + sx < N and 0 <= ny + sy < N and p_sand:
                        sand[ny+sy][nx+sx] += p_sand
                        move_sand += p_sand
                    
                    elif p_sand:
                        result += p_sand
                        move_sand += p_sand
                if 0 <= nx + dx < N and 0 <= ny + dy < N:
                    sand[ny+dy][nx+dx] += sand[ny][nx] - move_sand

                else:
                    result += sand[ny][nx] - move_sand

                sand[ny][nx] = 0

                x, y = nx, ny
            dir = (dir + 5) % 4
    return result

push_sand = [
    {
        'ewsn' : (-1,0),
        (0,1) : 0.07, (1, 1) : 0.01, (-1, 1) : 0.1, (0, 2) : 0.02,
        (0,-1) : 0.07, (1, -1) : 0.01, (-1, -1) : 0.1, (0, -2) : 0.02,
        (-2,0) : 0.05
    }, {
        'ewsn' : (0,1),
        (1,0) : 0.07, (1, -1) : 0.01, (1, 1) : 0.1, (2, 0) : 0.02,
        (-1,0) : 0.07, (-1, -1) : 0.01, (-1, 1) : 0.1, (-2, 0) : 0.02,
        (0,2) : 0.05
    }, {
        'ewsn' : (1,0),
        (0,1) : 0.07, (-1, 1) : 0.01, (1, 1) : 0.1, (0, 2) : 0.02,
        (0,-1) : 0.07, (-1, -1) : 0.01, (1, -1) : 0.1, (0, -2) : 0.02,
        (2,0) : 0.05
    }, {
        'ewsn' : (0,-1),
        (1,0) : 0.07, (1, 1) : 0.01, (1, -1) : 0.1, (2, 0) : 0.02,
        (-1,0) : 0.07, (-1, 1) : 0.01, (-1, -1) : 0.1, (-2, 0) : 0.02,
        (0,-2) : 0.05
    }]


N = int(input())
sand = [list(map(int, input().split())) for _ in range(N)]

print((tornado(push_sand, N)))