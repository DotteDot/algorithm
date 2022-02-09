#-*- coding: utf-8 -*-

#14890 경사로.py

N, L = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
result = 0

for x in range(N):
    cnt = 0
    stair = L
    s_num = matrix[0][x]
    for y in range(N):

        # 줄어드는 경우 판별
        if stair != L:
            if matrix[y][x] == s_num: stair -= 1
            else: break
            if stair == 0: stair = L

        # 일반적인 경우
        else:
            # 같은 높이
            if matrix[y][x] == s_num: cnt += 1

            # 다음이 높을때
            elif matrix[y][x] > s_num:
                if matrix[y][x] - 1 == s_num and cnt >= L:
                    s_num = matrix[y][x]
                    cnt = 1
                else: break
            
            # 다음이 낮을때
            else:
                if matrix[y][x] + 1 == s_num:
                    s_num = matrix[y][x]
                    cnt  = 0
                    stair -= 1
                else: break
                if stair == 0: stair = L
    else:
        if stair == L: result += 1

for y in range(N):
    cnt = 0
    stair = L
    s_num = matrix[y][0]

    for x in range(N):

        # 줄어드는 경우 판별
        if stair != L:
            if matrix[y][x] == s_num: stair -= 1
            else: break
            if stair == 0: stair = L

        # 일반적인 경우
        else:
            # 같은 높이
            if matrix[y][x] == s_num: cnt += 1

            # 다음이 높을때
            elif matrix[y][x] > s_num:
                if matrix[y][x] - 1 == s_num and cnt >= L:
                    s_num = matrix[y][x]
                    cnt = 1
                else: break
            
            # 다음이 낮을때 : flag = True
            else:
                if matrix[y][x] + 1 == s_num:
                    s_num = matrix[y][x]
                    cnt  = 0
                    stair -= 1
                else: break
                if stair == 0: stair = L
    else:
        if stair == L: result += 1

print(result)