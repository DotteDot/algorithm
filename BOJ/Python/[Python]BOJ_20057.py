#-*- coding: utf-8 -*-

#20057 마법사 상어와 토네이도.py

def tornado(push_sand, N):
    x = y = N // 2
    dir = 0
    result = 0

    for i in range(1, N + 1):												# 1 ~ N + 1 회 앞으로 전진
        for _ in range(2):													# 같은 방향을 2회 반복
            for _ in range(i):												# i회 만큼 앞으로 1칸 전진
                if x == y and x == 0: return result

                dx, dy = push_sand[dir]['ewsn']
                nx, ny = x + dx, y + dy
                move_sand = 0

                for j in list(push_sand[dir].keys())[1:]:                 	# 7가지 방향으로 모래가 흩어진다
                    sx, sy = j
                    p_sand = int(sand[ny][nx] * push_sand[dir][j])
                    
                    if 0 <= nx + sx < N and 0 <= ny + sy < N and p_sand:	# 밖으로 나가지 않고 이동하는 모래 양이
                        sand[ny+sy][nx+sx] += p_sand						# 정수로 표현했을 때 0이 아니면
                        move_sand += p_sand
                    
                    elif p_sand:											# 밖으로 나갔는데 이동하는 모래 양이
                        result += p_sand									# 정수로 표현했을 때 0이 아니면
                        move_sand += p_sand

                if 0 <= nx + dx < N and 0 <= ny + dy < N:					# a가 밖으로 나가지 않았을때
                    sand[ny+dy][nx+dx] += sand[ny][nx] - move_sand

                else:														# a가 밖으로 나갔을 때
                    result += sand[ny][nx] - move_sand

                x, y = nx, ny
                
            dir = (dir + 5) % 4												# 2회 반복후 방향을 돌린다
            
    return result


push_sand = [
    {
        'ewsn' : (-1,0),													# 서쪽
        (0,1) : 0.07, (1, 1) : 0.01, (-1, 1) : 0.1, (0, 2) : 0.02,
        (0,-1) : 0.07, (1, -1) : 0.01, (-1, -1) : 0.1, (0, -2) : 0.02,
        (-2,0) : 0.05
    }, {
        'ewsn' : (0,1),														# 남쪽
        (1,0) : 0.07, (1, -1) : 0.01, (1, 1) : 0.1, (2, 0) : 0.02,
        (-1,0) : 0.07, (-1, -1) : 0.01, (-1, 1) : 0.1, (-2, 0) : 0.02,
        (0,2) : 0.05
    }, {
        'ewsn' : (1,0),														# 동쪽
        (0,1) : 0.07, (-1, 1) : 0.01, (1, 1) : 0.1, (0, 2) : 0.02,
        (0,-1) : 0.07, (-1, -1) : 0.01, (1, -1) : 0.1, (0, -2) : 0.02,
        (2,0) : 0.05
    }, {
        'ewsn' : (0,-1),													# 북쪽
        (1,0) : 0.07, (1, 1) : 0.01, (1, -1) : 0.1, (2, 0) : 0.02,
        (-1,0) : 0.07, (-1, 1) : 0.01, (-1, -1) : 0.1, (-2, 0) : 0.02,
        (0,-2) : 0.05
    }]

N = int(input())
sand = [list(map(int, input().split())) for _ in range(N)]

print((tornado(push_sand, N)))