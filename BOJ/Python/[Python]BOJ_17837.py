#-*- coding: utf-8 -*-

#17837 새로운 게임2.py

N, K = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
pieces = []
for i in range(K):                                              # 내가 편한 x, y 형식대로 바꿈
    a, b, c = map(int, input().split())                         # matrix[y][x], start = 0
    pieces.append([b-1, a-1, c, i])
stack_list = [[i] for i in pieces]
delta = [[], [1, 0], [-1, 0], [0, -1], [0, 1]]                  # 부호는 동:1 서:2 북:3 남:4
cnt = 0
flag = False

'''
(1) [x, y]와 sequence를 넣으면 
    stack_list의 몇번째 index인지 return
(2) [nx, ny]를 넣으면 stack_list의 몇번째 index인지 return
(3) [nx, ny]를 넣었을때 찾지 못했다면 return -1
    return -1 은 다음 타일에 아무것도 없다는 말.'''
def find_xy(list, sequence = None):
    if sequence:                                                # (1)
        for i in range(K):
            for j in stack_list[i]: 
                if j[:2] == list and j[3] == sequence:
                    return i
    else:                                                       # (2)
        for i in range(K):
            for j in stack_list[i]: 
                if j[:2] == list:
                    return i
    return -1                                                   # (3)

'''
(1-1) 매개변수 red == 0 이면 다음 타일이 WHITE
(1-2) 매개변수 red == 1 이면 다음 타일이 RED
(2) (1)에 따라 tmp에 저장되는 순서가 바뀌게 된다
(3-1) find_xy == -1 이면 [nx, ny]에 아무것도 없는것
(3-1) find_xy == integer 이면 [nx, ny]에 뭔가 있다'''
def rotate_0(nx, ny, sidx, idx, red):
    stack_len = len(stack_list[sidx]) - idx
    next = find_xy([nx, ny])                                    # (2)
    tmp = []

    for i in range(idx, len(stack_list[sidx])):
        stack_list[sidx][i][0] = nx
        stack_list[sidx][i][1] = ny

    for _ in range(stack_len):
        if red:                                                 # (1-1)
            tmp.append(stack_list[sidx].pop())
        else:                                                   # (1-2)
            tmp.append(stack_list[sidx].pop(idx))

    if next == -1:                                              # (3-1)
        for i in range(K):
            if not stack_list[i]:
                stack_list[i] = tmp
                return 
    else:                                                       # (3-2)
        stack_list[next].extend(tmp)
        
'''
(1) 타일의 색깔이 BLUE거나 밖으로 나가면 방향을 반대로 돌린다
(2) 돌린 방향으로 [nx, ny]를 rotate_0을 진행'''
def rotate_180(sidx, idx, x, y, d):
    if d == 1: d = 2                                            # (1)
    elif d == 2: d = 1
    elif d == 3: d = 4
    elif d == 4: d = 3

    stack_list[sidx][idx][2] = d
    nx, ny = x + delta[d][0], y + delta[d][1]

    if 0 <= nx < N and 0 <= ny < N and matrix[ny][nx] != 2:
        rotate_0(nx, ny, stack_idx, idx, matrix[ny][nx])        # (2)

'''
(1) 종료조건 (4개 이상 겹친말이 있는가)를 판별'''
def check_flag():
    for j in stack_list:                                        # (1)
        if len(j) >= 4: return True
    return False


while cnt < 1000:
    cnt += 1

    for i in range(K):
        x, y, d, seq  = pieces[i]
        stack_idx = find_xy([x, y], seq)
        idx = stack_list[stack_idx].index(pieces[i])
        nx, ny = x + delta[d][0], y + delta[d][1]

        if 0 <= nx < N and 0 <= ny < N and matrix[ny][nx] != 2:
            rotate_0(nx, ny, stack_idx, idx, matrix[ny][nx])
        else:
            rotate_180(stack_idx, idx, x, y, d)

        flag = check_flag()
        if flag: break
    if flag: break

print(-1) if cnt >= 1000 else print(cnt)